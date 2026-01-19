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

How to Run
Requirements

Python 3.12 (required)
⚠️ Python 3.13 may cause issues with pygame. Use Python 3.12.

Step 1: Clone the repository
git clone <your-repo-url>
cd Nova-Voice-Assistant

Step 2: Create a virtual environment
python -m venv .venv


Activate it:

Windows (PowerShell)

.venv\Scripts\activate


Linux / macOS

source .venv/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt


⚠️ Note for Windows users:
If pyaudio fails to install, run:

pip install pipwin
pipwin install pyaudio

Step 4: Run Nova
python main.py

Step 5: Use the assistant

Say “Nova” to wake the assistant

Give voice commands after the prompt

Use push-to-talk if enabled

Future Plans

Add more system and productivity commands

Improve speech recognition reliability

Refactor into FastAPI + OOP architecture

Add real cloud AI API support

Build a simple frontend for easier usage
