import speech_recognition as sr
import gtts
from playsound import playsound
import os

r = sr.Recognizer()

def listen():
    with sr.Microphone() as src:
        print("Listening...")
        audio = r.listen(src)
    return audio

def audio_to_text(audio):
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Sorry, I didn't get that."
    
def talk(text):
    try:
        tts = gtts.gTTS(text)
        tts.save("out.mp3")
        playsound("out.mp3")
        os.remove("out.mp3")
    except:
        print("Could not play sound.")