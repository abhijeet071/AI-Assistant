# AI-Assistant

# 🎙️ AI-Powered Voice Assistant

A modular Python-based AI virtual assistant that integrates **speech recognition, natural language processing (NLP), API integrations, and smart task automation** to perform system operations and online tasks via voice or text commands.

---

## 📌 Features

- 🎤 **Voice Interaction:** Converts voice to text using Speech Recognition and responds via Text-to-Speech (TTS).
- 🧠 **Intent Recognition:** Uses **Sentence Transformers** and semantic similarity to intelligently classify user commands.
- 🌐 **Web Services Integration:**
  - Fetches latest news
  - Retrieves weather updates based on IP location
  - Plays YouTube videos
  - Performs Google and Wikipedia searches
  - Tells jokes and gives advice via APIs
- 🖥️ **System Automation:** Opens native applications like Notepad, Calculator, Command Prompt, and Camera.
- 📝 **Smart Task Automation:**
  - Set reminders with custom times
  - Add and display dynamic to-do lists
- 📡 **Communication:**
  - Send emails via SMTP
  - Send instant WhatsApp messages using `pywhatkit`
- 🕸️ **IP Address Detection:** Displays your current public IP.

---

## ⚙️ Tech Stack

- **Python 3.11+**
- `SpeechRecognition`
- `pyttsx3`
- `SentenceTransformers`
- `Spacy`
- `pywhatkit`
- `Requests`
- `OpenWeatherMap API`
- `Thenewsapi.com`
- `SMTP for email`

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai_virtual_assistant.git
   cd ai_virtual_assistant

