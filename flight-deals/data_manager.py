import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

headers = {
    "Authorization": os.getenv('SHEETY_AUTH')
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers= headers)
        data = response.json()
        print(data)
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)
