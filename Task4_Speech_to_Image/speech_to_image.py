import speech_recognition as sr
import requests
import base64
import os

os.makedirs("output", exist_ok=True)

# -------------------------------
# STEP 1: Speech to Text
# -------------------------------
def speech_to_text(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized Text:", text)
        return text
    except sr.UnknownValueError:
        print("Speech not clear")
        return None


# -------------------------------
# STEP 2: Text to Image (Stability AI)
# -------------------------------
def generate_image(prompt):
    API_KEY = "sk-dbVrZGHgs9zxSn8uCDiRtKU2m2InONFlB8bsT8pMDLrle5uf"  #<<< relace with your Stability AI key

    url = (
        "https://api.stability.ai/v1/generation/"
        "stable-diffusion-xl-1024-v1-0/text-to-image"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "text_prompts": [
            {"text": prompt}
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        image_base64 = data["artifacts"][0]["base64"]
        image_bytes = base64.b64decode(image_base64)

        with open("output/generated_image3.png", "wb") as f:
            f.write(image_bytes)

        print("✅ Image generated successfully!")
    else:
        print("❌ Image generation failed")
        print("Status:", response.status_code)
        print(response.text)


# -------------------------------
# STEP 3: Main Execution
# -------------------------------
audio_file = "audio/input_audio3.wav"

prompt_text = speech_to_text(audio_file)

if prompt_text:
    generate_image(prompt_text)
