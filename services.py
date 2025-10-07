import os
from transformers import pipeline
from google.api_core.exceptions import ServiceUnavailable
from llm_client import call_llm, call_gemini_summary
from prompts import (
    SHORT_SUMMARY_PROMPT,
    DETAILED_SUMMARY_PROMPT,
    BULLET_SUMMARY_PROMPT,
    QUIZ_PROMPT,
    KEYWORDS_PROMPT,
    FLASHCARDS_PROMPT
)


from transformers import pipeline

# ✅ Use your hosted Hugging Face model
t5_summarizer = pipeline(
    "summarization",
    model="kavya19566789/t5-summarizer",
    tokenizer="kavya19566789/t5-summarizer"
)

async def summarize_with_t5(text: str, mode: str = "short"):
    """Summarization using your Hugging Face hosted T5."""
    max_len = 120 if mode == "short" else 250
    min_len = 30 if mode == "short" else 80

    try:
        summary = t5_summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        print(f"T5 summarization failed: {e}")
        return "⚠️ T5 summarizer encountered an error."


# ------------------------------
# 🧠 Summarization Functions
# ------------------------------
async def summarize_with_t5(text: str, mode: str = "short"):
    """Offline summarization using fine-tuned local T5."""
    if not t5_summarizer:
        return "⚠️ T5 summarizer not available."

    max_len = 120 if mode == "short" else 250
    min_len = 30 if mode == "short" else 80

    try:
        summary = t5_summarizer(
            text, max_length=max_len, min_length=min_len, do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        print(f"T5 summarization failed: {e}")
        return "⚠️ T5 summarizer encountered an error."


async def summarize_text(text: str, mode: str = "short"):
    """Try Gemini first, fallback to local T5."""
    try:
        return await call_gemini_summary(text, mode)
    except ServiceUnavailable:
        print("Gemini overloaded — switching to local T5 summarizer.")
        return await summarize_with_t5(text, mode)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return await summarize_with_t5(text, mode)


# ------------------------------
# 🧩 Other LLM Tasks
# ------------------------------
async def generate_quiz(text: str, difficulty: str = "medium"):
    prompt = QUIZ_PROMPT.format(text=text, difficulty=difficulty)
    return await call_llm(prompt)


async def extract_keywords(text: str):
    prompt = KEYWORDS_PROMPT.format(text=text)
    return await call_llm(prompt)


async def generate_flashcards(text: str):
    prompt = FLASHCARDS_PROMPT.format(text=text)
    return await call_llm(prompt)
