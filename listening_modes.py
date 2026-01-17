import time
import speech_recognition as sr

WAKE_WORDS = ["nova", "noa", "nava", "nover"]


def ptt_listen(recognizer, timeout=4, phrase_time_limit=3):
    """
    Listens for wake word only.
    Returns True if wake word detected, else False.
    """
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        text = recognizer.recognize_google(audio, language="en-IN").lower().strip()
        print("Heard (PTT wake):", text)

        return any(w in text for w in WAKE_WORDS)

    except Exception:
        return False


def voice_active_listen(recognizer, silence_timeout=3, phrase_time_limit=5):
    """
    Listens continuously while the user is speaking.
    Stops after silence_timeout seconds of silence.
    """

    collected_text = []
    last_speech_time = time.time()

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = recognizer.listen(
                    source,
                    timeout=silence_timeout,
                    phrase_time_limit=phrase_time_limit
                )

            text = recognizer.recognize_google(audio, language="en-IN").strip()
            print("Heard (voice-active):", text)

            collected_text.append(text)
            last_speech_time = time.time()

        except sr.WaitTimeoutError:
            break

        except sr.UnknownValueError:
            if time.time() - last_speech_time > silence_timeout:
                break

        except Exception:
            break

    if not collected_text:
        return None

    return " ".join(collected_text)
