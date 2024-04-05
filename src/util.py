import os
import pyttsx3
from speech.speech import listen, audio_to_text
from decouple import config
import datetime
from dateutil import parser

from external.notion import NotionClient
from external.google_calendar import GoogleCalendarClient


class Util():
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)

        self.notionclient = NotionClient(config("NOTION_TOKEN"), config("NOTION_TODO_DATABASE_ID"))
        self.calendarclient = GoogleCalendarClient(config("TIMEZONE"))
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def create_note(self):
        self.speak("What should I write in the note?")
        note = listen()
        note = audio_to_text(note)
        
        res = self.notionclient.create_page(note, datetime.now().astimezone().isoformat())
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

    def create_event(self):
        self.speak("What is the name of the event?")
        name = listen()
        name = audio_to_text(name)

        self.speak("For what date?")
        date = listen()
        date = audio_to_text(date)
        date = self._convert_to_date(date)
        
        self.calendarclient.create_event(name, date, date)

    def _convert_to_date(self, date):
        parsed_date = parser.parse(date, fuzzy=True)

        day = parsed_date.day
        month = parsed_date.month
        year = datetime.date.today().year

        return datetime.date(year, month, day)