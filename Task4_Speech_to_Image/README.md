## TASK 4: SPEECH TO IMAGE GENERATION PROJECT

  Converts speech input into text and generates an image using AI.

## 📂 FOLDER STRUCTURE

Task4_Speech_to_Image/
│
├── audio/
│   ├── input_audio.wav
│   ├── input_audio2.wav
│   └── input_audio3.wav
│
├── output/
│   └── generated_image.png
│
├── generateaudio.py    <--- AudioGenerate file
├── speech_to_image.py  <--- project Main file
└── README.md

## SYSTEM REQUIREMENTS
  - Python 3.8 or above
  - Internet connection
  - Stability AI account

## INSTALL REQUIRED PACKAGES
  Open Command Prompt / Terminal and run:
    pip install speechrecognition requests

  For Windows audio support:
    pip install pipwin
    pipwin install pyaudio

## API KEY SETUP (IMPORTANT)
1. Create an account at https://platform.stability.ai/
2. Generate an API key from the dashboard.
3. Open speech_to_image.py
4. Replace:
  API_KEY = "YOUR_STABILITY_API_KEY"

with your actual API key.

## HOW TO RUN THE PROJECT
1. Place your audio file inside the audio folder.
2. Audio must be in WAV format.
3. Open terminal inside Task4_Speech_to_Image folder.
4. Run the command:

**python speech_to_image.py**

## OUTPUT
- Recognized speech text will be printed in the terminal.
- Generated image will be saved as:
  output/generated_image.png

## IMPORTANT NOTES FOR OTHER USERS
- Do not change API URL or image resolution.
- Ensure API key is valid and active.
- Internet connection is mandatory.
- Use clear English speech in audio files.

## TASK STATUS
  TASK 4 COMPLETED SUCCESSFULLY
