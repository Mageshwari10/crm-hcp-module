from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage, AIMessage
from langchain_core.tools import tool
import json
import os
from database import SessionLocal
import models
from datetime import datetime, date
from typing import Any

# --- Define Tools ---

@tool
def log_interaction(hcp_name: str, date_str: str, notes: str, products_discussed: str) -> str:
    """
    Logs a new interaction with a Healthcare Professional (HCP).
    Args:
        hcp_name: The name of the HCP (e.g. Dr. Smith).
        date_str: Date of the interaction in YYYY-MM-DD format.
        notes: Summary of the discussion.
        products_discussed: Name of the products discussed.
    """
    db = SessionLocal()
    try:
        # Find HCP or create dummy
        hcp = db.query(models.HCP).filter(models.HCP.name.ilike(f"%{hcp_name}%")).first()
        if not hcp:
            hcp = models.HCP(name=hcp_name, specialty="Unknown", location="Unknown")
            db.add(hcp)
            db.commit()
            db.refresh(hcp)
        
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        interaction = models.Interaction(
            hcp_id=hcp.id,
            date=parsed_date,
            notes=notes,
            products_discussed=products_discussed
        )
        db.add(interaction)
        db.commit()
        return f"Successfully logged interaction with {hcp.name} on {date_str}."
    except Exception as e:
        return f"Error logging interaction: {str(e)}"
    finally:
        db.close()

@tool
def edit_interaction(interaction_id: int, field_to_update: str, new_value: str) -> str:
    """
    Edits an existing interaction record.
    Args:
        interaction_id: The ID of the interaction to edit.
        field_to_update: The name of the field to update (e.g., 'notes', 'products_discussed', 'date').
        new_value: The new value for the field.
    """
    db = SessionLocal()
    try:
        interaction = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
        if not interaction:
            return f"Interaction with ID {interaction_id} not found."
        
        if field_to_update == 'date':
             interaction.date = datetime.strptime(new_value, "%Y-%m-%d").date()
        elif field_to_update == 'notes':
             interaction.notes = new_value
        elif field_to_update == 'products_discussed':
             interaction.products_discussed = new_value
        else:
             return f"Field {field_to_update} cannot be updated."
             
        db.commit()
        return f"Successfully updated {field_to_update} for interaction {interaction_id}."
    except Exception as e:
        return f"Error updating interaction: {str(e)}"
    finally:
        db.close()

@tool
def get_hcp_profile(hcp_name: str) -> str:
    """
    Retrieves the profile information for a specific Healthcare Professional.
    Args:
        hcp_name: Profile name to search (e.g., Dr. Smith)
    """
    db = SessionLocal()
    try:
        hcp = db.query(models.HCP).filter(models.HCP.name.ilike(f"%{hcp_name}%")).first()
        if hcp:
            return f"HCP Profile: {hcp.name}, Specialty: {hcp.specialty}, Tier: {hcp.tier}, Location: {hcp.location}"
        return f"No profile found for HCP: {hcp_name}"
    finally:
        db.close()

@tool
def get_recent_interactions(hcp_name: str) -> str:
    """
    Retrieves recent interactions logged for a specific HCP.
    Args:
        hcp_name: The name of the HCP
    """
    db = SessionLocal()
    try:
        hcp = db.query(models.HCP).filter(models.HCP.name.ilike(f"%{hcp_name}%")).first()
        if not hcp:
            return f"HCP {hcp_name} not found."
        
        interactions = db.query(models.Interaction).filter(models.Interaction.hcp_id == hcp.id).order_by(models.Interaction.date.desc()).limit(3).all()
        if not interactions:
            return f"No recent interactions found for {hcp.name}."
            
        res = [f"ID {i.id} on {i.date}: Discussed {i.products_discussed} - Notes: {i.notes}" for i in interactions]
        return "\n".join(res)
    finally:
        db.close()

@tool
def schedule_followup(hcp_name: str, task_description: str, due_date: str) -> str:
    """
    Schedules a follow-up action for a specific HCP.
    Args:
        hcp_name: The name of the HCP.
        task_description: The description of the follow-up task.
        due_date: The due date in YYYY-MM-DD format.
    """
    db = SessionLocal()
    try:
        hcp = db.query(models.HCP).filter(models.HCP.name.ilike(f"%{hcp_name}%")).first()
        if not hcp:
            return f"HCP {hcp_name} not found. Cannot schedule follow-up."
            
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        action = models.FollowUpAction(
            hcp_id=hcp.id,
            description=task_description,
            due_date=parsed_date
        )
        db.add(action)
        db.commit()
        return f"Successfully scheduled follow-up: {task_description} for {hcp.name} on {due_date}."
    except Exception as e:
        return f"Error scheduling follow-up: {str(e)}"
    finally:
        db.close()


tools = [log_interaction, edit_interaction, get_hcp_profile, get_recent_interactions, schedule_followup]

class SimpleCRMAgent:
    def __init__(self, model):
        # Model not needed for simple routing
        self.model = None
        self.tools = {tool.name: tool for tool in tools}
    
    def invoke(self, input_data: dict, config: dict = None) -> dict:
        import re
        messages = input_data.get("messages", [])
        
        today_date = date.today().strftime("%Y-%m-%d")
        
        # Extract user message
        user_message = ""
        for sender, text in messages:
            if sender == "user":
                user_message = text
                break
        
        print(f"DEBUG: User message received: {user_message}")
        
        # Route based on keywords
        if ("log" in user_message.lower()) and ("meeting" in user_message.lower() or "interaction" in user_message.lower()):
            print("DEBUG: Routing to log_interaction handler")
            # Extract HCP name
            hcp_match = re.search(r'(?:with\s+)?(Dr\.?\s*\w+(?:\s+\w+)?)', user_message, re.IGNORECASE)
            hcp_name = hcp_match.group(1).strip() if hcp_match else "Healthcare Professional"
            
            # Extract date or use today
            date_str = today_date
            
            # Extract products
            products_str = "General discussion"
            if 'diabetes' in user_message.lower():
                products_str = "Diabetes"
            elif 'cardiovascular' in user_message.lower():
                products_str = "Cardiovascular"
            
            notes = user_message[:150]
            
            print(f"DEBUG: About to call log_interaction with hcp={hcp_name}, date={date_str}, products={products_str}")
            
            # Call tool directly
            try:
                result = self.tools['log_interaction'].invoke({
                    'hcp_name': hcp_name,
                    'date_str': date_str,
                    'notes': notes,
                    'products_discussed': products_str
                })
                print(f"DEBUG: Tool result: {result}")
                # Clean up the response message
                clean_response = result.replace(" about on ", " on ")
                return {"messages": [{"response": clean_response}]}
            except Exception as e:
                print(f"DEBUG: Tool error: {str(e)}")
                import traceback
                traceback.print_exc()
                return {"messages": [{"response": f"Error: {str(e)}"}]}
        elif ("profile" in user_message.lower() or "about" in user_message.lower() or "specialty" in user_message.lower() or "tier" in user_message.lower()) and "dr" in user_message.lower():
            print("DEBUG: Routing to get_profile handler")
            # Extract HCP name - simple approach: find "Dr." then get only the next capitalized word
            hcp_match = re.search(r'Dr\.?\s*([A-Z][a-z]+)', user_message)
            if hcp_match:
                hcp_name = f"Dr. {hcp_match.group(1)}"
                print(f"DEBUG: Extracted HCP name: {hcp_name}")
            else:
                hcp_name = ""
                print(f"DEBUG: No HCP match found")
            
            if hcp_name and hcp_name != "Dr. ":
                try:
                    result = self.tools['get_hcp_profile'].invoke({'hcp_name': hcp_name})
                    print(f"DEBUG: Profile result: {result}")
                    return {"messages": [{"response": result}]}
                except Exception as e:
                    print(f"DEBUG: Profile error: {str(e)}")
                    return {"messages": [{"response": f"Could not find profile for {hcp_name}"}]}
            else:
                return {"messages": [{"response": "I couldn't identify the HCP name. Please specify (e.g. Dr. Smith)."}]}
        elif ("recent" in user_message.lower() or "history" in user_message.lower() or "interactions" in user_message.lower()) and "dr" in user_message.lower():
            print("DEBUG: Routing to get_interactions handler")
            # Extract HCP name - simple approach: find "Dr." then get only the next capitalized word
            hcp_match = re.search(r'Dr\.?\s*([A-Z][a-z]+)', user_message)
            if hcp_match:
                hcp_name = f"Dr. {hcp_match.group(1)}"
                print(f"DEBUG: Extracted HCP name for interactions: {hcp_name}")
            else:
                hcp_name = ""
                print(f"DEBUG: No HCP match found for interactions")
            
            if hcp_name and hcp_name != "Dr. ":
                try:
                    result = self.tools['get_recent_interactions'].invoke({'hcp_name': hcp_name})
                    print(f"DEBUG: Interactions result: {result}")
                    return {"messages": [{"response": result}]}
                except Exception as e:
                    print(f"DEBUG: Interactions error: {str(e)}")
                    return {"messages": [{"response": f"No interactions found for {hcp_name}"}]}
            else:
                return {"messages": [{"response": "I couldn't identify the HCP name to fetch interactions for. Please specify (e.g. Dr. Smith)."}]}
        elif ("follow" in user_message.lower() or "schedule" in user_message.lower()) and "dr" in user_message.lower():
            print("DEBUG: Routing to schedule_followup handler")
            # Extract HCP name - simple approach: find "Dr." then get only the next capitalized word
            hcp_match = re.search(r'Dr\.?\s*([A-Z][a-z]+)', user_message)
            if hcp_match:
                hcp_name = f"Dr. {hcp_match.group(1)}"
                print(f"DEBUG: Extracted HCP name for followup: {hcp_name}")
            else:
                hcp_name = ""
                print(f"DEBUG: No HCP match found for followup")
            
            if hcp_name and hcp_name != "Dr. ":
                try:
                    result = self.tools['schedule_followup'].invoke({
                        'hcp_name': hcp_name,
                        'task_description': user_message[:150],
                        'due_date': today_date
                    })
                    print(f"DEBUG: Followup result: {result}")
                    return {"messages": [{"response": result}]}
                except Exception as e:
                    print(f"DEBUG: Followup error: {str(e)}")
                    return {"messages": [{"response": f"Could not schedule follow-up: {str(e)}"}]}
            else:
                return {"messages": [{"response": "I couldn't identify the HCP name to schedule a follow-up for. Please specify (e.g. Dr. Smith)."}]}
        else:
            print("DEBUG: Routing to general response")
            return {"messages": [{"response": f"Hi! I can help log interactions with HCPs. Try:\n• 'Log meeting with Dr. Smith about diabetes'\n• 'Tell me about Dr. Johnson'\n• 'Show interactions with Dr. Anderson'"}]}

def get_agent():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your-groq-api-key-here":
        raise ValueError("GROQ_API_KEY is not set or is invalid.")
        
    model = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
    agent = SimpleCRMAgent(model)
    return agent
