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

Requirements:
- Python 3.12 (required)
  Python 3.13 may cause issues with pygame, so Python 3.12 is recommended.
- Windows OS
- A working microphone

Steps to run the project:

1. Clone the repository and enter the project directory:
   git clone <your-repo-url>
   cd Nova-Voice-Assistant

2. Create a virtual environment:
   python -m venv .venv

3. Activate the virtual environment:
   Windows (PowerShell):
   .venv\Scripts\activate

   Linux / macOS:
   source .venv/bin/activate

4. Install all dependencies:
   pip install -r requirements.txt

   Note for Windows users:
   If PyAudio fails to install, run:
   pip install pipwin
   pipwin install pyaudio

5. install ollama:
   Download ollama and sign in using
   your account and generate a API key
   create a .env folder and paste the ai there
   .env:
   NOVA_AI_BACKEND=cloud
   NOVA_AI_API_KEY=YOUR_API_KEY


7. Run the assistant:
   python main.py

8. Use Nova:
   Say "Nova" to wake the assistant.
   Give voice commands after activation.
   Use push-to-talk if configured.
   Speak clearly for best recognition accuracy.

---

## Features

- Wake-word based activation ("Nova")
- Push-to-talk and continuous voice conversation modes
- YouTube and YouTube Music search using direct search URLs
- Work mode and movie mode automation
- OTT platform search
- WhatsApp message automation
- Close all tabs/apps safely (terminal protected)
- Safe PC shutdown with voice confirmation
- AI-powered conversational fallback with short spoken replies
- Modular and maintainable architecture

---

## Known Limitations

- Optimized for Windows only
- Requires Python 3.12 for full compatibility
- Microphone quality affects recognition accuracy
- Desktop automation depends on system focus and permissions

---

## Future Plans

- Improve speech recognition accuracy
- Add more productivity and system commands
- Refactor into FastAPI + OOP architecture
- Add real cloud AI API support
- Build a simple frontend for easier setup and usage

---

## Disclaimer

Nova performs system-level automation such as closing apps and shutting down the PC.  
Use destructive commands carefully and at your own discretion.

Add real cloud AI API support

Build a simple frontend for easier usage
