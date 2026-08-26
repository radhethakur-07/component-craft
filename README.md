# 🚀 Component Craft ✨
**AI-Powered Text-to-React UI Builder**

![Status](https://img.shields.io/badge/Status-Active-success)
![Frontend](https://img.shields.io/badge/Frontend-React%20%7C%20Vite-61DAFB?logo=react)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![AI](https://img.shields.io/badge/AI-Google%20Gemini%203.5-4285F4?logo=google)
![Database](https://img.shields.io/badge/Database-Supabase-3ECF8E?logo=supabase)

**Component Craft** is a modern, full-stack web application that allows users to generate beautiful, responsive, and production-ready React components using natural language prompts. Just describe what you want, and the AI will code it, style it with Tailwind CSS, and render it in a live interactive sandbox!

---

## ✨ Key Features

- **🧠 AI Code Generation:** Powered by Google's blazing-fast **Gemini 3.5 Flash** model for highly accurate React and Tailwind CSS generation.
- **⚡ Live Interactive Preview:** Integrated with **Sandpack** to render generated code instantly in a resizable, draggable, and dynamic IDE-like environment.
- **🎨 Tailwind CSS Ready:** Automatic injection of the Tailwind CDN ensures all modern utility classes are parsed and styled perfectly in real-time.
- **💾 Database Persistence:** All generated prompts and code snippets are automatically saved to a **Supabase** PostgreSQL database.
- **🛡️ Strict AI Guardrails:** Custom system instructions ensure the AI outputs only valid, raw JSX without markdown bloat or conversational text.

---

## 🛠️ Tech Stack

### Frontend
- **React.js** (Vite)
- **Tailwind CSS** (Styling)
- **Sandpack** (Live Code Execution & Preview)
- **Lucide React** (Icons)

### Backend
- **Python / FastAPI** (High-performance API)
- **Uvicorn** (ASGI Server)
- **Google GenAI SDK** (AI Model Integration)
- **Pydantic** (Environment & Data Validation)

### Database & Storage
- **Supabase** (PostgreSQL)

---

## 🚀 Local Development Setup

Follow these steps to run Component Craft on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/radhethakur-07/component-craft.git
cd component-craft
```

### 2. Backend Setup
Navigate to the root directory and set up your Python environment:
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your API keys:
```env
SUPABASE_URL="your_supabase_project_url"
SUPABASE_KEY="your_supabase_anon_key"
GEMINI_API_KEY="your_google_gemini_api_key"
ENVIRONMENT="development"
```

Start the FastAPI server:
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Frontend Setup
Open a new terminal window and navigate to the frontend folder:
```bash
cd frontend

# Install Node modules
npm install
```

Create a `.env` file in the `frontend` folder:
```env
VITE_API_URL="http://localhost:8000"
```

Start the Vite development server:
```bash
npm run dev
```

Your app should now be running at `http://localhost:5173/`! 🎉

---

## 🌍 Deployment Guide

This project is built to be easily deployed using modern cloud platforms.

- **Frontend (Vercel):** Connect your GitHub repository to Vercel. Ensure you set the `VITE_API_URL` environment variable to your live backend URL during deployment.
- **Backend (Render):** Deploy as a Web Service on Render. Connect the repo, set the Root Directory to `backend`, use `pip install -r requirements.txt` as the build command, and `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` as the start command. Don't forget to add your Supabase and Gemini API keys in the environment variables!

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License
This project is open-source and available under the MIT License.