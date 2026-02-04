import pyttsx3
import os

os.makedirs("audio", exist_ok=True)

engine = pyttsx3.init()

texts = {
    "audio/input_audio1.wav": "car driving on a mountain road with scenic views",
    "audio/input_audio2.wav": "mentioning on the beach during sunset with sky",
    "audio/input_audio3.wav": "a beautiful sunset over the mountains with orange and purple sky",
}

for file, text in texts.items():
    engine.save_to_file(text, file)

engine.runAndWait()

print("Audio files generated successfully!")
