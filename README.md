# Jarvis Voice Assistant 🗣️🤖

A voice-activated personal assistant built with Python. Jarvis can open websites, play songs from your custom library, fetch the latest news, and even respond to custom queries using Google's Gemini AI model.

## 🚀 Features

- 🎙️ Voice Activation using Speech Recognition
- 🔗 Opens popular websites (YouTube, Google, Instagram, WhatsApp, etc.)
- 🎵 Plays songs from your local music library
- 📰 Fetches latest news headlines using News API
- 🤖 AI-powered conversational replies (using Google Gemini API)
- 🗣️ Text-to-speech responses using pyttsx3

## 🛠️ Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- requests
- google-generativeai
- dotenv

## 📂 Project Structure

├── jarvis.py ├── musicLibrary.py ├── .env.example ├── requirements.txt ├── README.md └── .gitignore


## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prasadlonare35/Jarvis-AI-Voice-Assistant.git
   cd Jarvis-AI-Voice-Assistant

2. **Create .env file:**
   ```bash
   GEMINI_API_KEY=your_actual_gemini_api_key
   NEWS_API_KEY=your_actual_newsapi_key

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run Jarvis:**
   ```bash
   python main.py

## ⚠️ Notes
1. .env is excluded via .gitignore.
2. Make sure your microphone is connected for voice input.
   
## ✨ Future Improvements
1. Add reminder and alarm features
2. Add more commands (weather updates, calendar integration, etc.)
3. Implement NLP for better context understanding

**Made with ❤️ by Prasad Lonare**
