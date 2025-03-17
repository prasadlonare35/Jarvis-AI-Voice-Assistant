import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import re
# from gtts import gTTS
# import pygame
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     # Generate speech with the speed adjusted (slow=False means normal speed)
#     tts = gTTS(text, slow=False)
#     tts.save('temp.mp3')

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     # Unload and remove the temporary file
#     pygame.mixer.music.unload()
#     os.remove('temp.mp3')

def aiProcess(command):
    genai.configure(api_key=gemini_api_key)
    # genai.configure(api_key="AIzaSyDSh4Ebf6vobOtV9X-EsW3-2heEEoqs2Vc")
    chat = genai.GenerativeModel("gemini-1.5-pro").start_chat(history=[])

    try:
        response_chunks = chat.send_message(command, stream=True)
        response_text = ''.join(chunk.text for chunk in response_chunks if hasattr(chunk, 'text'))

        # Remove asterisks (*) and other Markdown formatting
        clean_text = re.sub(r'[*_`]', '', response_text)  # Removes *, _, and ` (Markdown style formatting)
        clean_text = re.sub(r'\n+', ' ', clean_text)  # Replace multiple newlines with a single space
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Remove extra spaces

        return clean_text if clean_text else "I couldn't generate a response."
    except Exception as e:
        return f"An error occurred while processing your command: {e}"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https:/google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https:/youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https:/facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https:/linkedin.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])
            
            for article in articles:
                speak(article['title'])
    
    else:
        print(f"Processing command: {c}")
        output = aiProcess(c)
        print(output)
        speak(output)

if __name__ == "__main__":
    print("Initializing Jarvis....")
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            if(word.lower() == 'exit'):
                break
        except Exception as e:
            print(f"Error: {e}")
