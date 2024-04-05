from speech.speech import listen, audio_to_text

from util import Util

ACTIVATION_COMMAND = "nova"

if __name__ == "__main__":
    util = Util()

    while True:
        audio = listen()
        command = audio_to_text(audio)
        task = command.lower()
        
        if ACTIVATION_COMMAND in task:

            if "take a note" in task:
                util.create_note()
                
            elif "clear my downloads" in task:
                util.clear_downloads()

            elif "create an event" in task:
                util.create_event()

            else:
                continue

            