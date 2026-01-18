import pygame
import time
import os
import asyncio
import edge_tts
import pygame

def speak(text):
    print("Nova says:", text)

    try:
        os.makedirs("temp", exist_ok=True)
        audio_path = os.path.join("temp", "Nova.mp3")

        async def _speak():
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-GB-RyanNeural"
            )
            await communicate.save(audio_path)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(_speak())
        loop.close()

        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(audio_path)

    except Exception as e:
        # NEVER crash Nova because of TTS
        print("TTS error (ignored):", e)


def play_beep():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/play.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.quit()

def play_stop_beep():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/stop.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.quit()

