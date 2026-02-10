import speech_recognition as sr
import pyttsx3
import requests
import datetime

# -------------------------------
# TEXT TO SPEECH SETUP AND FUNCTION
# -------------------------------
engine = pyttsx3.init(driverName='sapi5')
engine.setProperty("rate", 160)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    print("Assistant speaking:", text)  
    engine.say(text)
    engine.runAndWait()


# -------------------------------
# SPEECH RECOGNITION
# -------------------------------
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# -------------------------------
# WEATHER (OpenWeather)
# -------------------------------
def get_weather():
    API_KEY = "1be044423089c973406c0ad43c4db225"  # <-- REPLACE API KEY
    CITY = "Madurai"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url, timeout=10)
    data = response.json()

    print("Weather API response:", data)  # DEBUG

    if "main" in data:
        temp = data["main"]["temp"]
        result = f"The current temperature in {CITY} is {temp} degrees Celsius."
        print(result)
        speak(result)
    else:
        speak("Sorry, I could not fetch weather information.")

# -------------------------------
# NEWS (NewsAPI - everything endpoint for free keys)
# -------------------------------
def get_news():
    API_KEY = "0a198a03264c49eb898114ad133fa3bc"  # <-- REPLACE API KEY
    url = (
        f"https://newsapi.org/v2/everything"
        f"?q=india&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    print("News API response:", data)  

    if "articles" in data and len(data["articles"]) > 0:
        speak("Here are the top news headlines.")
        for article in data["articles"][:3]:
            title = article.get("title", "")
            if title:
                print("Headline:", title)
                speak(title)
    else:
        speak("Sorry, no news articles were found.")

# -------------------------------
# REMINDERS
# -------------------------------
def set_reminder(command):
    reminder_text = command.replace("set reminder", "").strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("reminders.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {reminder_text}\n")

    print(f"Reminder saved the file: {reminder_text} at {timestamp}")
    speak("Your reminder has been saved.")

# -------------------------------
# MAIN ASSISTANT LOOP
# -------------------------------
def start_assistant():
    speak("Hello, I am your personal assistant. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        if "weather" in command:
            get_weather()

        elif "news" in command:
            get_news()

        elif "set reminder" in command:
            set_reminder(command)

        elif "exit" in command or "stop" in command:
            speak("Goodbye. Have a nice day.")
            break

        else:
            speak("Please say weather, news, set reminder, or exit.")


if __name__ == "__main__":
    start_assistant()
