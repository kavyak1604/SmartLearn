# 📘 SmartLearn: An Adaptive Quiz & Summarizer Agent (Backend)

This is the **backend service** for the Adaptive Quiz & Summarizer Agent.  
It provides document summarization, quiz generation, keyword extraction, and flashcard generation using FastAPI, Gemini API, and a fine-tuned T5 model for offline fallback.

---

## 🛠️ Tech Stack

- **FastAPI** (Python web framework)
- **Uvicorn** (ASGI server)
- **PyMuPDF** (`fitz`) for PDF parsing
- **python-docx** for Word files
- **python-pptx** for PowerPoint
- **python-jose** for JWT tokens
- **Transformers** for T5 summarization
- **dotenv** for environment variables

---

## 📁 Project Structure

```
Backend/
│── main.py            # FastAPI app
│── services.py        # Summarization, quiz, keywords, flashcards
│── prompts.py         # LLM prompt templates
│── llm_client.py      # Gemini API client
│── requirements.txt   # Dependencies
│── .env               # API keys (not in git)
│── README.md          # Project documentation
│── t5-finetuned-samsum/   # Fine-tuned T5 model files (optional)
```

---

## ⚡ Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd Adaptive_Agent/Backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the `Backend` directory:

```
GEMINI_API_KEY=your_gemini_api_key
HF_TOKEN=your_huggingface_token
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 Authentication

- `POST /register` — Register a new user
- `POST /token` — Login and get JWT token

---

## 📚 Core Endpoints

- `POST /summarize` — Summarize raw text (`short`, `detailed`, `bullet`)
- `POST /summarize-pdf` — Summarize PDF file
- `POST /summarize-docx` — Summarize Word document
- `POST /summarize-pptx` — Summarize PowerPoint
- `POST /summarize-txt` — Summarize text file
- `POST /quiz` — Generate quiz from text
- `POST /keywords` — Extract keywords from text
- `POST /process-pdf|docx|pptx|txt` — Get summary, quiz, keywords, and flashcards in one request

---

## 🧪 Example Usage

```bash
# Register a user
curl -X POST http://127.0.0.1:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass"}'

# Login to get JWT token
curl -X POST http://127.0.0.1:8000/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpass"

# Summarize text (replace <token> with your JWT)
curl -X POST http://127.0.0.1:8000/summarize \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"text":"Your content here", "mode":"short"}'
```

---

## ⚠️ Notes

- Change `SECRET_KEY` in `main.py` before deploying to production.
- Use a real database for users in production (not the in-memory `fake_users_db`).
- Keep your `.env` file out of version control.
- For Gemini and Hugging Face APIs, ensure your keys are valid and have sufficient quota.

---

## 📄 License

MIT License © 2025

`
