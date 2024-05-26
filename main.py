# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
