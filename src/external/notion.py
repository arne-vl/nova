import json
import requests

class NotionClient:
    def __init__(self, token, db_id) -> None:
        self.db_id = db_id

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def create_page(self, description, date):
        print("Creating page: ", description)

        url = 'https://api.notion.com/v1/pages'
        data = {
            "parent": {"database_id": self.db_id},
            "properties": {
                "Description": {
                    "title": [
                        {
                            "text": {
                                "content": description
                            }
                        }
                    ]
                },
                "Date": {
                    "date": {
                        "start": date,
                        "end": None
                    }
                }
            },
        }

        response = requests.post(url, headers=self.headers, data=json.dumps(data))

        print(response.status_code)
        print(response.json())

        if response.status_code == 200:
            return True
        else:
            return False