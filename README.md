# 🏥 AI-First CRM HCP Module 🚀

> 💡 An AI-driven Customer Relationship Management (CRM) module specifically designed for life science experts and field representatives to log, manage, and retrieve interactions with Healthcare Professionals (HCPs).

---

## 📋 Task Information & Documentation

**📚 Full Documentation:**
- [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) - In-depth architecture, LangGraph agent design, and tool specifications
- [TASK_COMPLETION.md](TASK_COMPLETION.md) - Complete requirements checklist and verification matrix

**✅ All Core Requirements Implemented:**
- ✅ AI-First CRM HCP Module with LangGraph agent
- ✅ Log Interaction Screen (dual interface: chat + form)
- ✅ 5 Custom LangGraph Tools (with log_interaction & edit_interaction)
- ✅ React + Redux frontend with TypeScript
- ✅ FastAPI Python backend
- ✅ Groq LLM Integration (llama-3.1-8b-instant)
- ✅ Database with SQLAlchemy ORM
- ✅ Google Inter font styling
- ✅ Zero human-written core code

---

## ✨ Features 🎯

🤖 **AI Co-Pilot Interface** 
- Chat with an intelligent agent powered by LangGraph to log your interactions effortlessly via natural language. Just tell it what happened! 💬

🎨 **Premium UI** 
- Designed with glassmorphism, dynamic fluid animations, modern typography (Inter), and an elegant dark mode theme to "wow" the user. ✨

📋 **Structured Manual Entry** 
- Sometimes, point-and-click is what you need. Real-time synchronicity between the form state and AI chat state. 🖱️

🛠️ **5 Custom LangGraph Tools** ⚡
1. 📝 `log_interaction` - Smartly captures new interaction timelines (Dates, products, notes). 
2. ✏️ `edit_interaction` - Refine previously logged interaction details dynamically. 
3. 👤 `get_hcp_profile` - Fetch background, tiering, and specialty info of providers. 
4. 📊 `get_recent_interactions` - Retrieve contextual history of a provider engagement. 
5. 📅 `schedule_followup` - Automates action items directly from conversational text.

---

## 🔧 Tech Stack 

| Component | Technology | Emoji |
|-----------|-----------|-------|
| **Frontend** | React + Vite, TypeScript, Redux Toolkit, Vanilla CSS | ⚛️ |
| **Backend** | FastAPI (Python), SQLAlchemy, LangGraph, Langchain | 🐍 |
| **Database** | SQLite (can swap to Postgres/MySQL) | 🗄️ |
| **LLM** | Groq API (`llama-3.1-8b-instant`) | 🚀 |

---

## 🚀 Getting Started 

### 1️⃣ Database & Backend Setup 🔥

```bash
cd backend
python -m venv venv
# Activate the environment (Mac/Linux)
source venv/bin/activate
# Activate the environment (Windows)
.\venv\Scripts\Activate.ps1

# Install requirements 📦
pip install fastapi uvicorn sqlalchemy langgraph langchain-groq pydantic python-dotenv langchain langchain-core
```

**🔐 Add your Groq API key:**
- 📋 Copy `.env.example` to `.env`
- 🔑 Insert your `GROQ_API_KEY` from https://console.groq.com/

**▶️ Run the server:**
```bash
uvicorn main:app --reload --port 8000
```
✅ Server running on http://127.0.0.1:8000

### 2️⃣ Frontend Setup 💻

```bash
cd frontend
npm install
npm run dev
```

🎉 The React app will launch on `http://localhost:5173` - Open it to experience the AI-integrated seamless interaction system!

---

## ⚡ Quick Start (5 minutes) 🏃

### All-in-One Setup
```bash
# 1. Clone the repository
git clone https://github.com/Mageshwari10/crm-hcp-module.git
cd crm-hcp-module

# 2. Setup Backend
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

pip install fastapi uvicorn sqlalchemy langgraph langchain-groq pydantic python-dotenv langchain langchain-core

# 3. Configure API Key
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# 4. Start Backend
uvicorn main:app --reload --port 8000

# 5. In NEW terminal, Setup Frontend
cd frontend
npm install
npm run dev

# 6. Open browser
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
```

✅ Done! Start chatting with your AI assistant! 🎉

---

## 💬 How to Use 🎯

### 🤖 Via AI Assistant (Best & Fastest!) 
Just chat naturally! Examples:
- 💬 *"Log a meeting with Dr. Smith today about disease awareness"*
- 👥 *"Show me Dr. Johnson's profile"*
- 📅 *"Schedule a follow-up with Dr. Chen for next week"*
- 📊 *"What recent interactions do we have with cardiologists?"*

### 📝 Via Structured Form (Manual Entry)
1. 📋 Fill in HCP details 
2. ⏰ Enter interaction information 
3. 📌 Track dates, times, attendees, and topics
4. 📎 Manage materials shared

---

## 📁 Project Structure 🗂️

```
crm-hcp-module/
├── 🔵 backend/                 # FastAPI server 🐍
│   ├── 🤖 agent.py            # AI agent with LangGraph tools
│   ├── 🔌 main.py             # FastAPI endpoints
│   ├── 💾 database.py          # SQLAlchemy database setup
│   ├── 🗄️ models.py            # Database models
│   ├── 📝 schemas.py           # Pydantic schemas
│   └── 🔐 .env.example         # Environment template
├── 🟢 frontend/                # React + Vite app ⚛️
│   ├── src/
│   │   ├── 🧩 components/      # React components
│   │   ├── 🏪 store/           # Redux store (crmSlice)
│   │   └── 📱 App.tsx          # Main app
│   └── 🎨 public/              # Static assets
└── 📄 README.md                # This file 👋
```

---

## � Prerequisites ✅

Before getting started, make sure you have:
- ✅ **Python 3.8+** installed
- ✅ **Node.js 14+** and npm installed
- ✅ **Groq API Key** (get it free at https://console.groq.com/)
- ✅ A terminal/command line interface
- ✅ ~500MB free disk space

---

## �🔐 Environment Setup 🛡️

Create a `.env` file in the `backend/` folder:
```env
GROQ_API_KEY=your_groq_api_key_here
```

🔗 Get your Groq API key from: https://console.groq.com/ (Free tier available! 🎁)

---

## 📊 API Endpoints 🔌

| Method | Endpoint | Description | Emoji |
|--------|----------|-------------|-------|
| POST | `/api/chat` | 💬 Send message to AI agent | 🤖 |
| GET | `/api/interactions` | 📥 Get all interactions | 📋 |
| POST | `/api/interactions` | ➕ Create new interaction | ✨ |

### API Usage Examples 📡

**Chat with AI:**
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Log an interaction with Dr. Smith", "thread_id": "default_thread"}'
```

**Get all interactions:**
```bash
curl http://localhost:8000/api/interactions
```

---

## 📚 File Descriptions 📖

### Backend Files 🐍
- **`agent.py`** - Core AI agent with 5 LangGraph tools for HCP interactions
- **`main.py`** - FastAPI server with endpoints for chat and interaction management
- **`database.py`** - SQLAlchemy database configuration and session management
- **`models.py`** - Database ORM models (HCP, Interaction, FollowUpAction)
- **`schemas.py`** - Pydantic validation schemas for API requests/responses
- **`.env.example`** - Template for environment variables

### Frontend Files ⚛️
- **`App.tsx`** - Main React application component
- **`ChatInterface.tsx`** - AI chat interface with message history
- **`StructuredForm.tsx`** - Manual interaction entry form
- **`InteractionHistory.tsx`** - Display historical interactions
- **`crmSlice.ts`** - Redux state management for CRM data
- **`index.css`** - Global styles with glassmorphism

---

## 🗄️ Database Schema 📊

The application uses SQLite with three main tables:

### HCP Table 👥
```
id: Integer (Primary Key)
name: String
specialty: String
location: String
tier: String
```

### Interaction Table 📋
```
id: Integer (Primary Key)
hcp_id: Integer (Foreign Key)
date: Date
notes: Text
products_discussed: String
created_at: Timestamp
```

### FollowUpAction Table 📅
```
id: Integer (Primary Key)
hcp_id: Integer (Foreign Key)
description: String
due_date: Date
status: String (Pending/Completed)
```

---

## 🛠️ Detailed Configuration 🔧

### Backend Configuration
- **Port**: 8000 (configurable via uvicorn)
- **Database**: SQLite at `./crm.db`
- **LLM**: llama-3.1-8b-instant (via Groq API)
- **Tool Timeout**: 30 seconds per request
- **CORS**: Enabled for all origins

### Frontend Configuration
- **Port**: 5173 (Vite default)
- **State Management**: Redux Toolkit
- **API Base URL**: http://localhost:8000/api
- **Thread ID**: local_session_1 (for conversation context)

---

## 🎯 Common Use Cases 💡

### 1️⃣ Quick HCP Meeting Log 📝
**User**: "Logged a meeting with Dr. Sarah Johnson today about the new diabetes product"
**AI Response**: Automatically logs the interaction with date, products, and creates entry

### 2️⃣ Follow-up Scheduling 📅
**User**: "Schedule a follow-up with Dr. Chen for next Tuesday"
**AI Response**: Creates a follow-up action scheduled for the specified date

### 3️⃣ HCP Profile Lookup 👤
**User**: "What's Dr. Brown's specialty and location?"
**AI Response**: Retrieves and displays HCP profile information

### 4️⃣ Interaction History 📊
**User**: "Show me all interactions with cardiologists"
**AI Response**: Displays filtered interactions based on HCP specialty

---

## 🐛 Troubleshooting 🔍

### Backend Issues

**❌ Error: `ModuleNotFoundError: No module named 'fastapi'`**
- Solution: Ensure you're in the venv and ran `pip install` with all required packages

**❌ Error: `GROQ_API_KEY is not set or is invalid`**
- Solution: Check your `.env` file exists in `backend/` folder with valid API key
- Verify API key from https://console.groq.com/

**❌ Error: `Port 8000 already in use`**
- Solution: Change port with: `uvicorn main:app --port 8001`

### Frontend Issues

**❌ Error: `npm: command not found`**
- Solution: Install Node.js from https://nodejs.org/

**❌ Error: `Port 5173 already in use`**
- Solution: Let Vite use the next available port automatically

**❌ ChatInterface showing no AI response**
- Solution: Verify backend is running on http://localhost:8000
- Check browser console (F12) for network errors

### Database Issues

**❌ Error: `database is locked`**
- Solution: Close other instances accessing the database
- Delete `crm.db` to start fresh (will create new database)

---

## 🚀 Performance Tips ⚡

✅ **Frontend Performance**
- React uses memo for expensive components
- Redux state is optimized with selectors
- CSS animations use GPU acceleration

✅ **Backend Performance**
- Database queries are indexed on frequently accessed fields
- Connection pooling enabled via SQLAlchemy
- Groq API responses cached at session level

✅ **AI Performance**
- LangGraph tools execute in parallel when possible
- Agent response time: 2-5 seconds on average
- Token optimization for the 8B model

---

## 🔒 Security Considerations 🛡️

⚠️ **Never commit `.env` file** - Always use `.env.example`
⚠️ **API Key Protection** - Keep GROQ_API_KEY secure
⚠️ **CORS Configuration** - Update in production to specific domains
⚠️ **Database Backups** - Regularly backup `crm.db`

---

## 📞 Support & Feedback 💬

Have questions or issues?
- 📧 Check existing GitHub Issues
- 🐛 Create a new issue with detailed description
- 💡 Suggest features via GitHub Discussions
- 📝 Submit pull requests with improvements

---

## 🎯 Key Features in Action ⚡

### 📱 AI Chat Interface 🗨️
- 💭 Type natural language requests
- 🧠 AI agent parses your request
- 🔧 Executes appropriate tool automatically
- 📤 Returns structured results instantly

### 📋 Interaction Management 💼
Track all HCP interactions with:
- ⏰ Date and time information
- 💊 Products discussed
- 👥 Attendees and notes
- 🔄 Follow-up actions

### 👥 HCP Profiles 📊
View comprehensive HCP information:
- 🏥 Specialty and location
- 📈 Tiering information
- 📚 Interaction history
- 🎯 Recent engagement details

---

## 🎨 UI/UX Highlights ✨

✅ **Glassmorphism Design** - Modern, transparent components  
✅ **Dark Mode** - Easy on the eyes 👀  
✅ **Smooth Animations** - Fluid interactions 🎬  
✅ **Responsive Layout** - Works on all devices 📱💻  
✅ **Real-time Sync** - Chat & form state sync perfectly 🔄  

---

## 🤝 Contributing 💪

Feel free to:
- 🍴 Fork the repository
- 🐛 Create issues for bugs
- ✨ Submit pull requests
- 💡 Suggest features

All contributions are welcome! 🙌

---

## 📄 License 📜

MIT License - Feel free to use this project for your own purposes! 🎉

---

## 🌟 Show Your Support 💖

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🔄 Sharing it with colleagues
- 💬 Providing feedback and suggestions
- 🚀 Contributing improvements

---

<div align="center">

### 🏥 Built with ❤️ for Life Science Professionals 💊

**Made to revolutionize HCP interactions** 🚀

[⬆ Back to top](#-ai-first-crm-hcp-module-)

</div>
