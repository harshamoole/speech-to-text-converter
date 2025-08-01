# 🗣️ Speech-to-Text Converter

## 🔍 Description
A simple Python-based Speech-to-Text Converter that captures audio input from a microphone and converts it into text using Google’s Speech Recognition API. This project demonstrates real-time audio processing and error handling in speech recognition.

## 💡 Features
- Real-time speech recognition  
- Ambient noise calibration  
- Google Web Speech API integration  
- Clear error handling for unrecognized input or connection issues  

## 🛠️ Technologies Used
- Python  
- SpeechRecognition  
- PyAudio  
- Google Speech API  

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/speech-to-text-converter.git
cd speech-to-text-converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

If PyAudio throws errors, install it using pipwin:
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Run the script
```bash
python speech_to_text.py
```

### 4. Speak into your mic 🎙️  
The terminal will display what you said.

## 📁 Sample Code
```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Say something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
```

## 📄 License
This project is free and open-source under the MIT License.
