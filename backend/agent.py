from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
import os
from database import SessionLocal
import models
from datetime import datetime, date

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

def get_agent():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your-groq-api-key-here":
        raise ValueError("GROQ_API_KEY is not set or is invalid.")
        
    model = ChatGroq(model="gemma2-9b-it", api_key=api_key)
    agent = create_react_agent(model, tools)
    return agent
