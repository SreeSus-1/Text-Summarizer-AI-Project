# 🧠 LLaMA Text Summarizer (Local GenAI Project)

An end-to-end Generative AI application that summarizes long text using a locally hosted LLaMA2 model via Ollama, with a FastAPI backend and Streamlit frontend.

## 🚀 Project Overview
This project demonstrates a full-stack GenAI architecture where users can input large text and receive concise summaries in real time. The application integrates a local LLM (LLaMA2) using Ollama, ensuring privacy, low latency, and no dependency on paid external APIs.

## 🏗️ Architecture
User Input (Streamlit UI)  
→ FastAPI Backend (REST API)  
→ Ollama (LLaMA2 Local LLM)  
→ Generated Summary (Returned to UI)

## ✨ Features
- Local LLM inference using LLaMA2 (via Ollama)
- Interactive Streamlit UI for real-time summarization
- FastAPI REST API backend
- End-to-end GenAI pipeline
- Robust error handling between frontend and backend
- Privacy-focused (no external API calls)

## 🛠️ Tech Stack
- Python
- FastAPI
- Streamlit
- Ollama
- LLaMA2
- Requests
- REST APIs


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SreeSus-1/Text-Summarizer-AI-Project.git
cd Text-Summarizer-AI-Project


2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows


3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install and Run Ollama (Local LLM)
Download: https://ollama.com

Then run:

ollama serve
ollama pull llama2

5️⃣ Start Backend (FastAPI)
uvicorn backend.main:app --reload --port 8000

6️⃣ Start Frontend (Streamlit)
streamlit run frontend/app.py

🌐 API Endpoint
Request:

{
  "text": "Your long text here"
}
Response:

{
  "summary": "Generated summary text"
}
