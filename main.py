import requests
from dotenv import load_dotenv
import os

load_dotenv()
AUTHORIZATION_TOKEN = os.getenv('AUTHORIZATION_TOKEN')
url = "https://api.bland.ai/v1/calls"

payload = {
    "phone_number": "<string>",
    "task": "<string>",
    "voice": "<string>",
    "first_sentence": "<string>",
    "wait_for_greeting": True,
    "interruption_threshold": 123,
    "pathway_id": "<string>",
    "model": "<string>",
    "tools": [{}],
    "webhook": "<string>",
    "record": True,
    "transfer_phone_number": "<string>",
    "transfer_list": {},
    "voice_settings": {
        "quality": 123,
        "stability": 123,
        "similarity": 123,
        "speed": 123
    },
    "language": "<string>",
    "max_duration": 123,
    "answered_by_enabled": True,
    "from": "<string>",
    "pronunciation_guide": [{}],
    "temperature": 123,
    "start_time": "<string>",
    "voicemail_action": {},
    "amd": True,
    "request_data": {},
    "dynamic_data": [{"dynamic_data[i].response_data": [{}]}],
    "voice_preset_id": "<string>",
    "reduce_latency": True,
    "voice_id": 123
}
headers = {
    "authorization": AUTHORIZATION_TOKEN,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text, response.content, response.status_code)