# assistant.py
import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import pywhatkit as kit
from googletrans import Translator

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function for listening to the command
def listen_to_command():
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Function for speaking text back
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for opening files or apps
def open_file(file_path):
    os.startfile(file_path)
    speak(f"Opening {file_path}")

# Function to take screenshots
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken")

# Function to search the web
def search_web(query):
    kit.search(query)
    speak(f"Searching for {query} on the web")

# Function for translating text
def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

# Execute commands based on the user input
def execute_command(command):
    if 'open' in command and 'file' in command:
        open_file("path_to_your_file.txt")
    elif 'screenshot' in command:
        take_screenshot()
    elif 'search' in command:
        search_web(command.replace('search', '').strip())
    elif 'translate' in command:
        translated_text = translate_text(command.replace('translate', '').strip())
        speak(f"Translated text: {translated_text}")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop to keep the assistant running
if __name__ == "__main__":
    while True:
        command = listen_to_command()
        if command:
            execute_command(command)
