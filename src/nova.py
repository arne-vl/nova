import pyttsx3
from speech.speech import listen, audio_to_text
from decouple import config
from datetime import datetime

from util import clear_downloads
from external.notion import NotionClient

ACTIVATION_COMMAND = "nova"

# Notion API
NOTION_TOKEN = config("NOTION_TOKEN")
NOTION_TODO_DATABASE_ID = config("NOTION_TODO_DATABASE_ID")
notionclient = NotionClient(NOTION_TOKEN, NOTION_TODO_DATABASE_ID)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def create_note():
    speak("What should I write in the note?")
    note = listen()
    note = audio_to_text(note)
    
    res = notionclient.create_page(note, datetime.now().astimezone().isoformat())
    if res:
        speak(f"I have created a new note: {note} in your Notion database.")
    else:
        speak("Failed to create note.")


if __name__ == "__main__":

    while True:
        audio = listen()
        command = audio_to_text(audio)
        task = command.lower()
        
        if ACTIVATION_COMMAND in task:

            if "make a note" in task:
                create_note()
    
                
            elif "clear my downloads" in task:
                speak("Clearing downloads.")
                
                clear_downloads()

                speak("Downloads cleared.")

            else:
                continue

            