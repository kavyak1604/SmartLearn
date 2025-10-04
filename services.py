from llm_client import call_llm
from prompts import SHORT_SUMMARY_PROMPT, DETAILED_SUMMARY_PROMPT,BULLET_SUMMARY_PROMPT, QUIZ_PROMPT,KEYPOINTS_PROMPT


async def summarize_text(text: str, mode: str = "short"):
    if mode == "short":
        prompt = SHORT_SUMMARY_PROMPT.format(text=text)
    elif mode == "detailed":
        prompt = DETAILED_SUMMARY_PROMPT.format(text=text)
    elif mode == "bullet":
        prompt = BULLET_SUMMARY_PROMPT.format(text=text)
    else:
        prompt = SHORT_SUMMARY_PROMPT.format(text=text)  # fallback

    return await call_llm(prompt)

async def generate_quiz(text: str, difficulty: str = "medium"):
    prompt = QUIZ_PROMPT.format(text=text, difficulty=difficulty)
    return await call_llm(prompt)

async def extract_keypoints(text: str):
    prompt = KEYPOINTS_PROMPT.format(text=text)
    return await call_llm(prompt)

