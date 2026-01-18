## Nova – Python Voice Assistant

Nova is a Python voice assistant I built mainly for learning and experimentation.
It runs locally on my system, listens for a wake word, and then responds to voice
commands by performing different actions.

The goal of this project is not to build a finished “smart assistant”, but to
understand how voice recognition, text-to-speech, and desktop automation work
together in a real program.

---

## Why this project exists

I started this project to:
- Learn how wake-word based assistants work
- Experiment with speech recognition and TTS
- Understand long-running background Python programs
- Practice structuring a project so it can grow over time

Because of this, the project is intentionally kept modular and flexible.

---

## Project structure (high level)

- **main.py**
  - Entry point of the assistant
  - Handles wake word detection and command flow

- **assistant_actions.py**
  - Contains system-level actions and automations

- **Other modules**
  - Used for specific logic (APIs, helpers, experiments)
  - Kept separate so the core loop stays clean

This structure makes it easy to add new ideas without breaking existing code.

## How to Run
Install the required packages:
pip install -r requirements.txt

Run the assistant:
python main.py

Say **"Nova"** to activate and give commands.


## Future Plans
- Add more commands
- Improve recognition accuracy
- Add generative ai API support later
