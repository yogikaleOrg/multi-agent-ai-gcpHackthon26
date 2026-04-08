from google import genai
import os
import json
import re

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ ADD THIS FUNCTION HERE
def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    return {}


def classify_intent(text: str):
    prompt = f"""
    Classify intent into one word only:
    task, calendar, notes, workflow

    Input: {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return (response.text or "").strip().lower()


def extract_entities(text: str):
    prompt = f"""
    Extract structured JSON from the input.

    Return ONLY valid JSON:
    {{
        "title": "",
        "time": "",
        "priority": "",
        "content": ""
    }}

    Input: {text}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    # ✅ USE SAFE PARSER HERE
    return safe_json_parse(response.text or "")