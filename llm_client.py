import os
import httpx
import logging
from dotenv import load_dotenv

# ------------------ Logging ------------------
logger = logging.getLogger(__name__)

# ------------------ Load API Key ------------------
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MODEL = "gemini-2.5-flash"

# ------------------ Call LLM ------------------
async def call_llm(prompt: str, model: str = DEFAULT_MODEL):
    if not GEMINI_KEY:
        logger.critical("⚠️ GEMINI_API_KEY not set in environment")
        raise ValueError("⚠️ GEMINI_API_KEY is not set. Please add it in .env")

    url = f"{BASE_URL}/{model}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": GEMINI_KEY}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            # Extract response
            return data["candidates"][0]["content"]["parts"][0]["text"]

    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
        return f"Error: LLM API returned {e.response.status_code}"

    except httpx.RequestError as e:
        logger.error(f"Request error: {str(e)}")
        return "Error: Could not reach LLM API"

    except Exception as e:
        logger.exception("Unexpected error in call_llm")
        return "Error: Something went wrong while calling LLM"
