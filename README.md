# 📘 Adaptive Quiz & Summarizer Agent (Backend)

This is the **backend service** for the Adaptive Quiz & Summarizer Agent.
It uses **FastAPI** with Gemini API integration to provide document summarization, quiz generation, and keypoint extraction.

---

## 🚀 Features

* 🔑 **User Authentication** (Register / Login with JWT tokens)
* 📝 **Summarization Modes**: Short, Detailed, Bullet Points
* 📚 **Quiz Generation**: Multiple-choice questions with difficulty levels
* 📌 **Key Point Extraction**: 3–5 key takeaways from text
* 📂 **Document Support**: PDF, DOCX, TXT, PPTX
* ⚡ **Process Mode**: Get summary, quiz, and keypoints in one request

---

## 🛠️ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) (Python backend framework)
* [Uvicorn](https://www.uvicorn.org/) (ASGI server)
* [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing
* [python-docx](https://python-docx.readthedocs.io/) for Word files
* [python-pptx](https://python-pptx.readthedocs.io/) for PowerPoint
* [python-jose](https://python-jose.readthedocs.io/) for JWT tokens
* [dotenv](https://pypi.org/project/python-dotenv/) for environment variables

---

## 📂 Project Structure

```
Backend/
│── main.py            # FastAPI app
│── services.py        # Summarization, quiz, keypoints
│── prompts.py         # LLM prompt templates
│── llm_client.py      # Gemini API client
│── requirements.txt   # Dependencies
│── .env               # API keys (ignored in git)
│── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd Backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a **.env** file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

The backend runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📌 API Endpoints

### 🔑 Authentication

* `POST /register` → Register new user
* `POST /token` → Login & get JWT

### 📝 Summaries

* `POST /summarize` → Summarize raw text (`short`, `detailed`, `bullet`)
* `POST /summarize-pdf` → Summarize a PDF
* `POST /summarize-docx` → Summarize Word document
* `POST /summarize-pptx` → Summarize PowerPoint
* `POST /summarize-txt` → Summarize text file

### 📚 Quiz

* `POST /quiz` → Generate quiz from text
* `POST /process-pdf|docx|pptx|txt` → Get **summary + quiz + keypoints**

### 📌 Key Points

* `POST /keypoints` → Extract 3–5 important points

---

## 🧪 Example Usage (cURL)

```bash
# 1. Register
curl -X POST http://127.0.0.1:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456"}'

# 2. Login
curl -X POST http://127.0.0.1:8000/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test&password=123456"

# 3. Summarize text
curl -X POST http://127.0.0.1:8000/summarize \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{"text":"Your content here", "mode":"detailed"}'
```

---

## 🔒 Security Notes

* Keep `.env` **out of GitHub** (already in `.gitignore`)
* Change `SECRET_KEY` in `main.py` before deployment
* For production, run with a real database (Postgres/MySQL) instead of in-memory `fake_users_db`

---

## 📜 License

MIT License © 2025

---
