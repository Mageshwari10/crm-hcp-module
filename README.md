# AI-First CRM HCP Module

An AI-driven Customer Relationship Management (CRM) module specifically designed for life science experts and field representatives to log, manage, and retrieve interactions with Healthcare Professionals (HCPs).

## Features
- **AI Co-Pilot Interface**: Chat with an intelligent agent powered by LangGraph to log your interactions effortlessly via natural language.
- **Premium UI**: Designed with glassmorphism, dynamic fluid animations, modern typography (Inter), and an elegant dark mode theme to "wow" the user.
- **Structured Manual Entry**: Sometimes, point-and-click is what you need. Real-time synchronicity between the form state and AI chat state.
- **5 Custom LangGraph Tools**:
    1. `log_interaction`: Smartly captures new interaction timelines (Dates, products, notes).
    2. `edit_interaction`: Refine previously logged interaction details dynamically.
    3. `get_hcp_profile`: Fetch background, tiering, and specialty info of providers.
    4. `get_recent_interactions`: Retrieve contextual history of a provider engagement.
    5. `schedule_followup`: Automates action items directly from conversational text.

## Tech Stack
- **Frontend**: React + Vite, TypeScript, Redux Toolkit, Vanilla CSS.
- **Backend**: FastAPI (Python), SQLAlchemy, LangGraph, Langchain.
- **Database**: SQLite (SQLAlchemy ORM — can be directly swapped to Postgres/MySQL via the connection string).
- **LLM**: Groq API (`gemma2-9b-it`).

## Getting Started

### 1. Database & Backend Setup
```bash
cd backend
python -m venv venv
# Activate the environment (Mac/Linux)
source venv/bin/activate
# Activate the environment (Windows)
.\venv\Scripts\Activate.ps1

# Install requirements (Assuming they are set, otherwise pip install fastapi uvicorn sqlalchemy langgraph langchain-groq pydantic python-dotenv)
pip install fastapi uvicorn sqlalchemy langgraph langchain-groq pydantic python-dotenv
```

Add your Groq API key:
- Copy `.env.example` to `.env`
- Insert your `GROQ_API_KEY`

Run the server:
```bash
uvicorn main:app --reload --port 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

The React app will launch on `http://localhost:5173`. Open it to experience the AI-integrated seamless interaction system!
