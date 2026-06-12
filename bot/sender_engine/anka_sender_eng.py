import requests
import os
from dotenv import load_dotenv
import random


load_dotenv()

class AnkarexSender:

    def __init__(self, sms_informations) -> None:
        self.api_key = os.getenv('API_KEY')
        self.api = os.getenv('API')
        self.sms_informations = sms_informations

    def send_sms(self) -> None:
        
        sending_data = {
            'token': self.api_key,
            'send': 'bulk',
            'to': self.sms_informations['phone_number'],
            'sender_id': self.sms_informations['sid'],
            "message_content": self.sms_informations['message'],
            'unicode': False
        }

        print(sending_data)
        headers = {
            'method': 'POST',
            "Content-Type": "application/json",
            "User-Agent": "Ankarex-Rest-0.22"
        }

        response = requests.post(self.api, json=sending_data, headers=headers)

        return response.json()




