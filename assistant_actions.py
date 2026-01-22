import pyautogui
import time
import webbrowser
import os
import win32gui
import threading



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

def open_ott_search(text: str, provider: str = DEFAULT_OTT):
    """
    Open OTT platform Explore page and search movie.
    Accepts raw natural language and cleans internally.
    """

    # -------- CLEAN MOVIE NAME --------
    c = text.lower().strip()

    # Priority 1: everything after "called"
    if "called" in c:
        movie = c.split("called", 1)[1].strip()
    else:
        # Fallback cleanup
        noise_words = [
            "i want to",
            "please",
            "can you",
            "play",
            "watch",
            "movie",
            "a",
            "the"
        ]

        movie = c
        for w in noise_words:
            movie = movie.replace(w, "")

        movie = " ".join(movie.split()).strip()

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

    # -------- OPEN ENTRY PAGE --------
    os.system(
        f'start chrome --profile-directory="Default" "{ott["entry_url"]}"'
    )

    # -------- WAIT FOR PAGE + PROFILE --------
    time.sleep(ott["load_time"])

    # -------- TYPE MOVIE NAME DIRECTLY --------
    pyautogui.write(movie, interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")



TERMINAL_KEYWORDS = [
    "command prompt",
    "powershell",
    "windows terminal",
    "cmd",
    "terminal",
    "wsl",
    "bash"
]

def is_terminal_window(title: str) -> bool:
    title = title.lower()
    return any(k in title for k in TERMINAL_KEYWORDS)

import win32gui

def focus_non_terminal_window() -> bool:
    def enum_handler(hwnd, results):
        if not win32gui.IsWindowVisible(hwnd):
            return
        title = win32gui.GetWindowText(hwnd)
        if not title:
            return
        if is_terminal_window(title):
            return
        results.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_handler, windows)

    if not windows:
        return False  # nothing else to focus

    try:
        win32gui.SetForegroundWindow(windows[0])
        return True
    except Exception:
        return False


def close_All_Tabs_Apps():
    max_actions = 20
    actions = 0

    while actions < max_actions:
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)

        # If Nova (terminal) is focused → switch focus properly
        if is_terminal_window(title):
            switched = focus_non_terminal_window()
            if not switched:
                break  # nothing else to close
            time.sleep(0.4)
            continue

        pyautogui.hotkey('alt', 'f4')
        actions += 1
        time.sleep(0.5)

def confirm_shutdown(speak, take_command):
    speak("Are you sure you want to shut down the PC?")

    try:
        reply = take_command()
    except Exception:
        speak("I didn't catch that. Shutdown cancelled.")
        return

    if not reply:
        speak("Shutdown cancelled.")
        return

    reply = reply.lower()

    if "yes" in reply or "s" in reply:
        speak("Shutting down. Goodbye.")
        shutdown_pc()
        return

    if "no" in reply or "cancel" in reply:
        speak("Shutdown cancelled.")
        return

    speak("I didn't understand. Shutdown cancelled.")


def shutdown_pc():
    # 1️Close other apps
    close_All_Tabs_Apps()
    time.sleep(1)

    # 2 Trigger Windows shutdown in background
    def shutdown_os():
        os.system("shutdown /s /t 0")

    threading.Thread(target=shutdown_os, daemon=True).start()

    # 3️ Give OS a moment to accept the command
    time.sleep(0.5)

    # 4️ Exit Nova LAST
    os._exit(0)




