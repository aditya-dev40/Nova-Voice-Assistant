import json
import webbrowser

from musicLibrary import getSongLink, getVideoLink
from newsLibrary import get_news_titles
from assistant_actions import (
    send_whatsapp_message,
    start_work_mode,
    start_movie_mode,
    open_ott_search
)
from ai_engine import ask_ai


# ---------------- MEMORY ----------------
conversation_memory = []


# ---------- ALLOWED SIMPLE COMMANDS ----------
COMMANDS = {
    "start_work_mode": start_work_mode,
    "start_movie_mode": start_movie_mode,
    "open_google": lambda: webbrowser.open("https://www.google.com/"),
    "open_youtube": lambda: webbrowser.open("https://www.youtube.com/"),
    "open_linkedin": lambda: webbrowser.open("https://www.linkedin.com/"),
    "open_github": lambda: webbrowser.open("https://www.github.com/")
}


# ---------- VOICE RULES ----------
VOICE_RULES = """
You are Nova, a VOICE assistant.

Rules for ALL responses:
- Speak like a human, not a document
- NO markdown, NO bullet points, NO tables
- NO symbols like *, #, |, or `
- Short, clear sentences
- Maximum 3–4 sentences
- Sound natural when spoken aloud

If the explanation is complex, give a SIMPLE overview first.
Ask the user if they want more details.
"""


def handle_command(text, speak, take_command):
    print("COMMAND RECEIVED:", text)
    c = text.lower().strip()

    if len(c) < 2:
        speak("Yes?")
        return True

    # ----- MEDIA -----
    if "play" in c and "song" in c:
        song, link = getSongLink(c)
        speak(f"Playing {song}")
        webbrowser.open(link)
        return True

    if "youtube" in c:
        video, link = getVideoLink(c)
        speak(f"Playing {video}")
        webbrowser.open(link)
        return True
    
    # ----- MOVIE MODE (EXPLICIT) -----
    if "movie mode" in c:
        speak("Starting movie mode")
        start_movie_mode()
        return True


    # ----- OTT SEARCH (GENERIC) -----
    if "movie" in c or "watch" in c:
        speak("Searching on streaming platform")
        open_ott_search(c)
        return True


    # ----- NEWS -----
    if "news" in c:
        for title in get_news_titles()[:3]:
            speak(title)
        return True

    # ----- MANUAL WHATSAPP FALLBACK -----
    if "send whatsapp message" in c:
        speak("Whom should I message?")
        contact = take_command()

        speak("What should I say?")
        message = take_command()

        speak(f"Sending message to {contact}")
        send_whatsapp_message(contact, message)
        speak("The message is being sent")
        return True

    # ----- AI INTENT ROUTING -----
    if ai_intent_router(c, speak):
        return True

    # ----- AI CHAT (WITH MEMORY) -----
    return ai_chat(text, speak)


def ai_intent_router(text, speak):
    prompt = f"""
{VOICE_RULES}

Available simple commands:
{", ".join(COMMANDS.keys())}

Rules:
- If user wants to run ONE of the above commands,
  reply with ONLY the command name.
- If user wants to send a WhatsApp message,
  reply ONLY in valid JSON like:

{{
  "action": "send_whatsapp",
  "contact": "<name>",
  "message": "<text>"
}}

- If user wants to watch a movie on an OTT platform,
  reply ONLY in valid JSON like:

{{
  "action": "ott_search",
  "movie": "<movie name>"
}}

- If no command matches, reply NONE.

User: {text}
"""

    result = ask_ai(prompt).strip()

    if result in COMMANDS:
        speak("Okay")
        COMMANDS[result]()
        return True

    try:
        data = json.loads(result)

        if data.get("action") == "send_whatsapp":
            speak(f"Sending message to {data['contact']}")
            send_whatsapp_message(data["contact"], data["message"])
            speak("The message is being sent")
            return True

        if data.get("action") == "ott_search":
            speak(f"Searching {data['movie']} on OTT")
            open_ott_search(data["movie"])
            return True

    except Exception:
        pass

    return False


def ai_chat(text, speak):
    global conversation_memory

    conversation_memory.append(f"User: {text}")
    conversation_memory = conversation_memory[-6:]

    prompt = f"""
{VOICE_RULES}

Conversation so far:
{chr(10).join(conversation_memory)}

Nova:
"""

    reply = ask_ai(prompt).strip()

    conversation_memory.append(f"Nova: {reply}")
    conversation_memory = conversation_memory[-6:]

    speak(reply)
    return True
