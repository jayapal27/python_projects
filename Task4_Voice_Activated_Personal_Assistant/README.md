## TASK 4: VOICE-ACTIVATED PERSONAL ASSISTANT PROJECT

Description :
This project implements a Voice-Activated Personal Assistant using Python.
The assistant listens to user voice commands, processes them using speech
recognition, and responds using text-to-speech. It can check weather,
read news headlines, and set reminders through voice interaction.

## FEATURES
- Voice-based interaction
- Weather information through voice
- News headlines reading
- Reminder creation
- Continuous listening until exit command
- Text-to-speech responses

## FOLDER STRUCTURE
Task4_Voice_Activated_Personal_Assistant/
│
├── assistant.py        <--- Main project file
├── reminders.txt       <--- Stores reminders
├── README.md
└── Task4_Report.txt

## SYSTEM REQUIREMENTS
- Windows 11
- Python 3.8 or above
- Working microphone
- Speakers / headphones
- Internet connection

## INSTALL REQUIRED PACKAGES
Open Command Prompt / Terminal and run:

pip install speechrecognition pyttsx3 requests
pip install pipwin
pipwin install pyaudio

# API KEY SETUP
1. Weather API:
   - Website: https://openweathermap.org/
   - Generate API key
   - Add key in assistant.py

2. News API:
   - Website: https://newsapi.org/
   - Generate free API key
   - Add key in assistant.py

## WHAT THE ASSISTANT SPEAKS
When you speak commands, the assistant responds by speaking:

- Weather:
  "The current temperature in Chennai is 23 degrees Celsius."

- News:
  "Here are the top news headlines..."
  Followed by latest headlines.

- Reminder:
  "Your reminder has been saved successfully."

- Exit:
  "Goodbye. Have a nice day."

## HOW TO RUN THE PROJECT
1. Open terminal in the project folder.
2. Run the command:
 ** python assistant.py**

3. Speak one of the following commands after 'Listening...' appears.

## VOICE COMMANDS
After running the project and when the terminal shows "Listening...",
the user should speak one of the following commands clearly.

Weather Commands:
- "What is the weather"
- "Tell me the weather"
- "What is today's weather"

Assistant Response (Spoken):
- "The current temperature in Chennai is XX degrees Celsius."

------------------------------------

News Commands:
- "Tell me the news"
- "Read the news"
- "What is the latest news"

Assistant Response (Spoken):
- "Here are the top news headlines..."
- Followed by latest news headlines.

------------------------------------

Reminder Commands:
- "Set reminder buy groceries"
- "Set reminder meeting at 5 PM"
- "Set reminder call my friend"

Assistant Response (Spoken):
- "Your reminder has been saved successfully."

(Reminders are stored in reminders.txt)

------------------------------------

Exit Commands:
- "Exit"
- "Stop"
- "Close assistant"

Assistant Response (Spoken):
- "Goodbye. Have a nice day."

## OUTPUT
- Assistant speaks responses through speakers.
- Recognized commands are printed in terminal.
- Reminders are saved in reminders.txt file.

## AI & TECHNOLOGY DETAILS
- Speech Recognition:
  Uses Google Speech Recognition via SpeechRecognition library
  to convert speech into text.

- Natural Language Processing:
  Simple keyword-based command detection.

- Text-to-Speech (AI):
  Uses Windows SAPI5 through pyttsx3 to convert text responses into speech.

## IMPORTANT NOTES
- Speak clearly after 'Listening...' message.
- Do not run multiple audio applications simultaneously.
- Internet connection is required for APIs.

## TASK STATUS
TASK 4 COMPLETED SUCCESSFULLY
