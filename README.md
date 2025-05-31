# 📢 Text to Speech Converter 🎙️
![image](https://github.com/user-attachments/assets/38a81943-8f50-4343-b5ff-7eeebe782d07)

Welcome to the **Text-to-Speech (TTS) Converter project!** This application converts user-provided text into natural-sounding speech with customizable English accents. Built using Flask, gTTS (Google Text-to-Speech), HTML, Tailwind CSS, and JavaScript, it offers a sleek, responsive UI and is architected with modularity, error handling, and configuration management—making it ideal for integration into larger systems. 🌐✨



---

## 🚀 Features

- **Multiple Accents**: Choose from a variety of English accents to customize your speech output. 🗣️  
- **Fast Conversion**: Convert text to speech in seconds with a seamless experience. ⚡  
- **Responsive Design**: Access the app on any device, from desktops to mobiles. 📱💻  
- **User-Friendly Interface**: Modern UI with intuitive controls and audio playback. 🎨  
- **Powered by Pwskills.com**: Leverages advanced text-to-speech technology. 🧠  

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python) 🐍
- **Text-to-Speech Engine**: gTTS (Google Text-to-Speech) 🎧
- **Frontend**: HTML, Tailwind CSS, JavaScript 🌐  
- **Libraries**: jQuery, Font Awesome (for icons) 📚  
- **Deployment**: Runs locally with Flask server 🌍  

---

## 📦 Project Overview
- This application performs the following operations:
- Accepts a text input and a desired accent (e.g., British, Indian, Australian).
- Validates and maps the accent to a corresponding TLD (e.g., .co.uk for British).
- Converts the text to speech using gTTS with the chosen accent.
- Saves the original text input to a file for logging (userinput.txt).
- Stores the generated MP3 audio file with a timestamped name.
- Encodes the MP3 file into a base64 string for easy usage in web or other systems.
- Returns the base64 audio string to the client for playback or transmission.
- Handles errors gracefully with custom exceptions (TTSException) and logging.

---

## 📋 Prerequisites

Before you start, ensure you have the following installed:

- Python 3.8+ 🐍  
- pip (Python package manager) 📦  
- Git (for cloning the repository) 🗂️  

---

## ⚙️ Installation

### Clone the Repository 📥
```bash
git clone https://github.com/your-username/text-to-speech-converter.git
cd text-to-speech-converter
````

### Create a Virtual Environment 🧪

```bash
conda create -p env python==3.11 -y
```

### Activate the Virtual Environment 🧪

```bash
conda activate env/
```

### Install Dependencies 📦

```bash
pip install -r requirements.txt
```

### Set Up the Flask Application 🚀

Ensure the `app.py` file and the `templates` folder (containing `index.html`) are in the project directory.

### Run the Application 🌟

```bash
python app.py
```

The app will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
### Set Up the Streamlit Application 🚀

Ensure the `main.py` file is in the project directory.

### Run the Application 🌟

```bash
streamlit run main.py
```


## 🎮 Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`. 🌐
2. Select an English accent from the dropdown menu. 🗣️
3. Enter the text you want to convert in the textarea. ✍️
4. Click the **Convert to Speech** button. ▶️
5. Listen to the generated audio in the results section. 🎧

---

## 📂 Project Structure

```
text-to-speech-converter/
├── templates/
│   └── index.html       # Frontend template with HTML, Tailwind CSS, JS
├── app.py
├── text_to_speech/      # Flask backend for handling requests
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── text_to_speech/      # Custom modules for TTS functionality
```

---

## 🐞 Troubleshooting

* **Flask Server Not Starting**: Ensure all dependencies are installed and the virtual environment is activated. 🛠️
* **Audio Not Playing**: Check if the browser supports WAV audio and verify the backend response. 🔊
* **CORS Issues**: The app uses Flask-CORS to handle cross-origin requests; ensure the backend URL is correct. 🌐

---
---

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details. 📄

---

```
# Text_To_Speech
