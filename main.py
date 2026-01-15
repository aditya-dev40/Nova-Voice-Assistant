import speech_recognition as sr
import webbrowser
import asyncio
import edge_tts
import os
import pygame
import time
from musicLibrary import getSongLink
from newsLibrary import get_news_titles



def speak(text):
    print("Nova says:", text)

    async def _speak():
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-GB-RyanNeural"
        )
        await communicate.save("Nova.mp3")

    asyncio.run(_speak())

    pygame.mixer.init()
    pygame.mixer.music.load("Nova.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove("Nova.mp3")

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
        titles = get_news_titles()
        for title in titles:
            speak(title)
        return        


if __name__ == "__main__":
    speak("Initializing Nova....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=20)

            word = r.recognize_google(audio)

            if word.lower() == "Nova":
                speak("Yes Sir")

                with sr.Microphone() as source:
                    print("Nova Active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error;", e)
