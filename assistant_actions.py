import pyautogui
import time
import webbrowser
import os
import urllib.parse


def send_whatsapp_message(contact, message):
    # Open WhatsApp desktop app
    os.system("start whatsapp:")
    time.sleep(8)  # wait for app to open

    # Open search (Ctrl + F works in WhatsApp Desktop)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    # Type contact name
    pyautogui.write(contact, interval=0.1)
    time.sleep(2)
    pyautogui.press("enter")

    time.sleep(1)

    # Type message and send
    pyautogui.write(message, interval=0.05)
    pyautogui.press("enter")

WORK_MODE_ACTIONS = {
    "chrome": True,
    "vscode": True,
    "youtube": True,
    "chatgpt": True,
}

MOVIE_MODE = {
    "movie": True,
}

def start_work_mode():
    if WORK_MODE_ACTIONS.get("chrome"):
        os.system('start chrome --profile-directory="Profile 1"')
        time.sleep(2)

    if WORK_MODE_ACTIONS.get("vscode"):
        os.system("code")
        time.sleep(2)

    if WORK_MODE_ACTIONS.get("youtube"):
        webbrowser.open("https://www.youtube.com")

    if WORK_MODE_ACTIONS.get("chatgpt"):
        webbrowser.open("https://chatgpt.com")


def start_movie_mode():
    if MOVIE_MODE.get("movie"):
        os.system('start chrome --profile-directory="Default"')

        webbrowser.open("https://www.hotstar.com/in/home")

DEFAULT_OTT = "jiohotstar"

OTT_PROVIDERS = {
    "jiohotstar": {
        "entry_url": "https://www.hotstar.com/in/explore",
        "load_time": 12,
        "type_directly": True
    },
    "netflix": {
        "entry_url": "https://www.netflix.com/search",
        "load_time": 10,
        "type_directly": True
    },
    "prime": {
        "entry_url": "https://www.primevideo.com/search",
        "load_time": 10,
        "type_directly": True
    }
}

\
def open_ott_search(text: str, provider: str = DEFAULT_OTT):
    """
    Open OTT platform Explore page and search movie.
    Accepts raw natural language and cleans internally.
    """

    # -------- CLEAN MOVIE NAME --------
    c = text.lower()

    triggers = [
        "play a movie called",
        "play movie called",
        "watch a movie called",
        "watch movie called",
        "play movie",
        "watch movie",
        "play",
        "watch"
    ]

    movie = c
    for t in triggers:
        if t in c:
            movie = c.replace(t, "").strip()
            break

    if not movie:
        print("No movie name detected")
        return

    provider = provider.lower()
    if provider not in OTT_PROVIDERS:
        print(f"Unknown OTT provider: {provider}")
        return

    ott = OTT_PROVIDERS[provider]

    # -------- OPEN CHROME WITH LOGGED-IN PROFILE --------
    os.system('start chrome --profile-directory="Default"')
    time.sleep(2)

    # -------- OPEN EXPLORE PAGE --------
    os.system(
        f'start chrome --profile-directory="Default" "{ott["explore_url"]}"'
    )

    # -------- WAIT FOR PAGE + PROFILE --------
    time.sleep(ott["load_time"])

    # -------- TYPE MOVIE NAME DIRECTLY --------
    pyautogui.write(movie, interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")