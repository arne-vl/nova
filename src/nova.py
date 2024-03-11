import os
from speech.speech import listen, audio_to_text, talk
from decouple import config
from external.notion import NotionClient
from datetime import datetime

ACTIVATION_COMMAND = "test"

# Notion API
NOTION_TOKEN = config("NOTION_TOKEN")
NOTION_TODO_DATABASE_ID = config("NOTION_TODO_DATABASE_ID")
notionclient = NotionClient(NOTION_TOKEN, NOTION_TODO_DATABASE_ID)

if __name__ == "__main__":

    while True:
        audio = listen()
        command = audio_to_text(audio)
        
        if ACTIVATION_COMMAND in command.lower():
            print("Nova is activated")
            talk("What can I do for you?")

            task = listen()
            task = audio_to_text(task)

            if "make a note" in task:
                talk("What should I write in the note?")
                note = listen()
                note = audio_to_text(note)
                
                res = notionclient.create_page(note, datetime.now().astimezone().isoformat())
                if res:
                    talk(f"I have created a new note: {note} in your Notion database.")
                else:
                    talk("Failed to create note.")
    
                
            elif "clear downloads" in task:
                talk("Clearing downloads.")
                os.system("rm -rf ~/Downloads/*")

            
