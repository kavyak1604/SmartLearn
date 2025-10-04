# ------------------ Summaries ------------------
SHORT_SUMMARY_PROMPT = """
Summarize the following text in 2-3 concise sentences.

Text:
{text}

Summary:
"""

DETAILED_SUMMARY_PROMPT = """
Write a detailed summary of the following text in 3-4 paragraphs.
Focus on clarity and include all important details.

Text:
{text}

Detailed Summary:
"""
# Bullet Summary Prompt
BULLET_SUMMARY_PROMPT = """
Summarize the following text into clear bullet points. 
Keep each bullet short and precise, focusing only on the most important information.

Text:
{text}

Bullet Point Summary:
- 
- 
- 
"""

# ------------------ Quiz ------------------
QUIZ_PROMPT = """
Based on the following text, create 5 multiple-choice questions with answers.
Each question should have 4 options (a, b, c, d), and clearly indicate the correct answer.

Difficulty: {difficulty}

Text:
{text}

Output format (text):
Q1. ...
a) ...
b) ...
c) ...
d) ...
Answer: x
"""
KEYPOINTS_PROMPT = """
Extract the 3-5 most important key points from the following text.
Keep each point short, factual, and easy to understand.

Text:
{text}

Key Points:
- 
- 
- 
"""

