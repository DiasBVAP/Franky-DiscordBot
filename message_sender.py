import requests
import os
from dotenv import load_dotenv

def send_message(message: str):
    load_dotenv()
    payload = {
        'content': message
    }
    header = {
        'authorization': os.environ.get('TOKEN')
    }
    channel_id = os.environ.get('CHANNEL_ID')
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=header)