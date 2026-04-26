from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from dotenv import load_dotenv
import os

import models, schemas, agent
from database import engine, get_db, SessionLocal

# Load env variables
load_dotenv()

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM HCP API")

# Configure CORS based on environment
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
if allowed_origins == ["*"]:
    allow_origins_list = ["*"]
else:
    allow_origins_list = [origin.strip() for origin in allowed_origins]

# Add CORS middleware to allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def seed_sample_hcps():
    """Add sample HCP data if the table is empty"""
    db = SessionLocal()
    try:
        existing_hcps = db.query(models.HCP).count()
        if existing_hcps == 0:
            sample_hcps = [
                models.HCP(name="Dr. Martin", specialty="Cardiovascular", tier="Premium", location="Boston"),
                models.HCP(name="Dr. Anderson", specialty="Diabetes", tier="Standard", location="New York"),
                models.HCP(name="Dr. Johnson", specialty="Cardiology", tier="Standard", location="Chicago"),
                models.HCP(name="Dr. Williams", specialty="Oncology", tier="Gold", location="Los Angeles"),
            ]
            db.add_all(sample_hcps)
            db.commit()
            print("✅ Sample HCPs added to database")
    except Exception as e:
        print(f"Error seeding HCPs: {e}")
    finally:
        db.close()

# Seed data on startup
seed_sample_hcps()

@app.post("/api/chat")
def chat_with_agent(req: schemas.ChatRequest):
    try:
        ag = agent.get_agent()
        # Initialize agent and invoke
        result = ag.invoke({"messages": [("user", req.message)]}, config={"configurable": {"thread_id": req.thread_id}})
        # Get response from result
        if "messages" in result:
            messages = result["messages"]
            # Extract the response content
            if messages and isinstance(messages, list):
                last_item = messages[-1]
                if isinstance(last_item, dict) and "response" in last_item:
                    ai_response = last_item["response"]
                elif hasattr(last_item, 'content'):
                    ai_response = last_item.content
                else:
                    ai_response = str(last_item)
            else:
                ai_response = str(messages)
        else:
            ai_response = str(result)
        
        return {"response": ai_response}
    except Exception as e:
        import traceback
        error_detail = f"{str(e)}\n\n{traceback.format_exc()}"
        print(f"ERROR: {error_detail}")
        raise HTTPException(status_code=500, detail=error_detail)

@app.get("/api/interactions", response_model=list[schemas.Interaction])
def get_interactions(db: Session = Depends(get_db)):
    interactions = db.query(models.Interaction).order_by(models.Interaction.date.desc()).all()
    return interactions

@app.post("/api/interactions", response_model=schemas.Interaction)
def create_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(get_db)):
    db_interaction = models.Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@app.get("/api/hcps", response_model=list[schemas.HCP])
def get_hcps(db: Session = Depends(get_db)):
    hcps = db.query(models.HCP).all()
    return hcps

@app.get("/")
def read_root():
    return {"message": "CRM HCP API is running."}
