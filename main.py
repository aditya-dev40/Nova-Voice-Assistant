import speech_recognition as sr
import webbrowser
import keyboard

from musicLibrary import getSongLink, getVideoLink
from newsLibrary import get_news_titles
from assistant_actions import send_whatsapp_message, start_work_mode, start_movie_mode
from sound_utils import speak, play_beep, play_stop_beep
from listening_modes import ptt_listen, voice_active_listen


# GLOBAL STATE

r = sr.Recognizer()
listening = False
LISTENING_MODE = "ptt"   # "ptt" or "voice"


# COMMAND EXECUTION

def takeCommand():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source, timeout=5, phrase_time_limit=6)
        return r.recognize_google(audio, language="en-IN")


def processCommand(c):
    print("COMMAND RECEIVED:", c)
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")

    elif "open youtube" in c:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open linkedin" in c:
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/")

    elif "open github" in c:
        speak("Opening github")
        webbrowser.open("https://www.github.com/")

    elif c.startswith("play"):
        song, link = getSongLink(c)
        speak(f"Playing {song}")
        webbrowser.open(link)

    elif c.startswith("youtube"):
        video, link = getVideoLink(c)
        speak(f"Playing {video}")
        webbrowser.open(link)

    elif "news" in c:
        for title in get_news_titles()[:3]:
            speak(title)

    elif "send whatsapp message" in c:
        speak("Whom should I message?")
        contact = takeCommand()

        speak("What should I say?")
        message = takeCommand()

        send_whatsapp_message(contact, message)
        speak("Message sent")

    elif "work mode" in c:
        speak("Starting work mode")
        start_work_mode()

    elif "movie mode" in c:
        speak("Starting movie mode")
        start_movie_mode()

    else:
        speak("Sorry, I didn't understand that command")


# PTT HANDLERS

def on_ptt_press(event):
    global listening

    if listening:
        return

    listening = True
    play_beep()
    print("F8 pressed")

    if LISTENING_MODE == "ptt":
        print("PTT mode active")
        wake_detected = ptt_listen(r)

        if wake_detected:
            speak("Yes Sir")
            print("Listening for command...")

            try:
                command = takeCommand()
                processCommand(command)
            except Exception as e:
                print("Command error:", e)

    elif LISTENING_MODE == "voice":
        print("Voice mode active")
        voice_mode()



def on_ptt_release(event):
    global listening

    if listening:
        listening = False
        play_stop_beep()
        print("PTT stopped")


# VOICE MODE LOOP

def voice_mode():
    # Step 1: wait for wake word (nova)
    wake_detected = ptt_listen(r)

    if not wake_detected:
        return

    speak("Yes Sir")
    print("Listening for command...")

    try:
        command = voice_active_listen(r)
        if command:
            processCommand(command)
    except Exception as e:
        print("Voice command error:", e)


# MODE SWITCH

def toggle_mode():
    global LISTENING_MODE

    if LISTENING_MODE == "ptt":
        LISTENING_MODE = "voice"
        speak("Voice mode enabled")
        print("MODE → voice")
    else:
        LISTENING_MODE = "ptt"
        speak("Push to talk mode enabled")
        print("MODE → ptt")


# MAIN

if __name__ == "__main__":
    speak("Initializing Nova...")

    keyboard.on_press_key("f8", on_ptt_press)
    keyboard.on_release_key("f8", on_ptt_release)
    keyboard.add_hotkey("ctrl+m", toggle_mode)

    keyboard.wait()
