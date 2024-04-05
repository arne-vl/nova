import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

class GoogleCalendarClient:
    def __init__(self, timezone) -> None:
        self.timezone = timezone

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

    def create_event(self, name, start_date, end_date):
        try:
            service = build("calendar", "v3", credentials=self.creds)

            event = {
            'summary': name,
            'start': {
                'date': start_date.isoformat(),
                'timeZone': self.timezone,
            },
            'end': {
                'date': end_date.isoformat(),
                'timeZone': self.timezone,
            },
            }
            event = service.events().insert(calendarId="primary", body=event).execute()
            print("Event created: %s" % (event.get("htmlLink")))

        except HttpError as error:
            print(f"An error occurred: {error}")