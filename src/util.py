import os
import pyttsx3
from speech.speech import listen, audio_to_text
from decouple import config
from datetime import datetime

from external.notion import NotionClient

# Notion API
NOTION_TOKEN = config("NOTION_TOKEN")
NOTION_TODO_DATABASE_ID = config("NOTION_TODO_DATABASE_ID")
notionclient = NotionClient(NOTION_TOKEN, NOTION_TODO_DATABASE_ID)


class Util():
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def create_note(self):
        self.speak("What should I write in the note?")
        note = listen()
        note = audio_to_text(note)
        
        res = notionclient.create_page(note, datetime.now().astimezone().isoformat())
        if res:
            self.speak(f"I have created a new note: {note} in your Notion database.")
        else:
            self.speak("Failed to create note.")

    def clear_downloads(self):
        self.speak("Clearing downloads.")

        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        os.chdir(downloads_dir)

        if os.name == 'nt':  # Windows
            del_files_command = "del /S /Q *.*"
            del_dirs_command = "for /D %p in (*) do rmdir /s /q %p"

            os.system(del_files_command)
            os.system(del_dirs_command)
        else:  # Unix/Linux
            del_files_dirs_command = "rm -rf *"

            os.system(del_files_dirs_command)

        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

        self.speak("Downloads cleared.")
