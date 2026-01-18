import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AI_BACKEND = os.getenv("NOVA_AI_BACKEND", "cloud")
AI_API_KEY = os.getenv("NOVA_AI_API_KEY")

if AI_BACKEND == "cloud" and not AI_API_KEY:
    raise RuntimeError("NOVA_AI_API_KEY not set in .env")


def ask_ai(prompt: str) -> str:
    """
    Single entry point for AI.
    """
    if AI_BACKEND == "cloud":
        return ask_cloud_model(prompt)
    return "Local AI not configured."


def ask_cloud_model(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "gpt-oss:20b-cloud",
        "prompt": prompt,
        "stream": False
    }

    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(url, json=payload, headers=headers, timeout=60)
        res.raise_for_status()
        return res.json()["response"].strip()
    except Exception as e:
        print("AI error:", e)
        return "Sorry, I couldn't process that."
