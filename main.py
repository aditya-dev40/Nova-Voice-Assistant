import speech_recognition as sr
import keyboard
import warnings; warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")
from command_router import handle_command


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
                handle_command(
                                command,
                                speak=speak,
                                take_command=takeCommand
                            )
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
    wake_detected = ptt_listen(r)
    if not wake_detected:
        return

    speak("Yes Sir")
    print("Voice conversation started")

    while True:
        command = voice_active_listen(r, silence_timeout=6)

        if not command:
            speak("Okay, stopping.")
            break

        handle_command(
            command,
            speak=speak,
            take_command=takeCommand
        )



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
