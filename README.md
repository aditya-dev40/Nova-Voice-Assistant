# Nova Voice Assistant (Python)

Nova is a Python voice assistant I built for learning. It activates with a wake word and can open websites, play songs, and read the latest news using voice commands.

## Features
- Wake word activation ("Nova")
- Open websites (Google, YouTube, LinkedIn)
- Play songs using voice commands
- Read latest news headlines
- Voice output using edge-tts + pygame

## Commands
Say **"Nova"** to activate, then try:
- open google
- open youtube
- open linkedin
- play <song name>
- news

## How to Run
Install the required packages:
pip install -r requirements.txt

Run the assistant:
python main.py

Say **"Nova"** to activate and give commands.

## Project Structure
Nova-Voice-Assistant/
│── main.py
│── musicLibrary.py
│── newsLibrary.py
│── requirements.txt
│── README.md
│── .gitignore

## Future Plans
- Add more commands
- Improve recognition accuracy
- Add ChatGPT API support later
