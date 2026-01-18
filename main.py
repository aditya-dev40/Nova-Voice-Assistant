import speech_recognition as sr
import webbrowser
import keyboard
import warnings; warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

from musicLibrary import getSongLink
from newsLibrary import get_news_titles
from assistant_actions import send_whatsapp_message, start_work_mode, start_movie_mode
from sound_utils import speak, play_beep, play_stop_beep

r = sr.Recognizer()
listening = False
WAKE_WORDS = ["nova", "noa", "nava", "nover"]


def takeCommand():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source, timeout=5, phrase_time_limit=6)
        return r.recognize_google(audio, language="en-IN")


def processCommand(c):
    print("COMMAND RECEIVED:", c)

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif "open ground" in c.lower():
        speak("Opening ground")
        webbrowser.open("https://www.G.round.com/")
    elif c.lower().startswith("play"):
        song, link = getSongLink(c)
        speak(f"Playing {song}")
        webbrowser.open(link)
        return
    elif "news" in c.lower():
        titles = get_news_titles()[:3]  # only top 3
        for title in titles:
            speak(title)
        return
    elif "send whatsapp message" in c.lower():
        speak("Whom should I message?")
        contact = takeCommand()

        speak("What should I say?")
        message = takeCommand()

        speak(f"Sending message to {contact}")
        send_whatsapp_message(contact, message)
        speak("Message sent")
        return
    elif "start work mode" in c.lower() or "work mode" in c.lower():
        speak("Starting your work mode")
        start_work_mode()
        speak("Work mode activated")
    elif "start movie mode" in c.lower() or "movie mode" in c.lower():
        speak("Starting your movie mode")
        start_movie_mode()
        speak("movie mode activated")

    else:
        speak("Sorry, I didn't understand that command")

def on_ptt_press(event):
    global listening

    if listening:
        return

    listening = True
    play_beep()
    print("PTT started")

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.4)
            audio = r.listen(source, timeout=4, phrase_time_limit=3)

        word = r.recognize_google(audio, language="en-IN").lower()
        print("Heard wake word:", word)

        if any(w in word for w in WAKE_WORDS):
            speak("Yes Sir")

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.4)
                audio = r.listen(source, timeout=6, phrase_time_limit=10)

            command = r.recognize_google(audio, language="en-IN")
            processCommand(command)

    except Exception as e:
        print("Error:", e)

def on_ptt_release(event):
    global listening

    if listening:
        listening = False
        play_stop_beep()
        print("PTT stopped")


if __name__ == "__main__":
    speak("Initializing Nova...")

    keyboard.on_press_key("f8", on_ptt_press)
    keyboard.on_release_key("f8", on_ptt_release)

    keyboard.wait()  

   
