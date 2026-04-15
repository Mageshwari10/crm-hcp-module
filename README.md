# 🏥 AI-First CRM HCP Module 🚀

> 💡 An AI-driven Customer Relationship Management (CRM) module specifically designed for life science experts and field representatives to log, manage, and retrieve interactions with Healthcare Professionals (HCPs).

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

## 🔐 Environment Setup 🛡️

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
