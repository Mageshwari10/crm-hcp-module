from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from dotenv import load_dotenv

import models, schemas, agent
from database import engine, get_db

# Load env variables
load_dotenv()

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM HCP API")

# Add CORS middleware to allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
def chat_with_agent(req: schemas.ChatRequest):
    try:
        ag = agent.get_agent()
        # Initialize LangGraph state and invoke
        result = ag.invoke({"messages": [("user", req.message)]}, config={"configurable": {"thread_id": req.thread_id}})
        # The result will contain the conversation history. We get the last AIMessage.
        ai_response = result["messages"][-1].content
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
