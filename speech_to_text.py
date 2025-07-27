import speech_recognition as sr

recognizer = sr.Recognizer()

mic_index = 0  # Try changing this to 1, 2, etc. based on output from list_microphone_names()

with sr.Microphone(device_index=mic_index) as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Say something...")
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
