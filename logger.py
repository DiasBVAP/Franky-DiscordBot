import websocket
import json
import threading
import time
import os
from dotenv import load_dotenv

def send_json_request(ws, request) -> None:
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws) -> None:
    print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("Heartbeat sent")

def initialize(q) -> None:
    load_dotenv()
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    event = recieve_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

    payload = {
        'op': 2,
        "d": {
            "token": os.environ.get('TOKEN'),
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": 'pc'
            }
        }
    }
    send_json_request(ws, payload)

    while True:
        event = recieve_json_response(ws)

        try:
            if event['d']['author']['username'] != os.environ.get('BOT_USERNAME'):
                q.put(f"{event['d']['content']}")
            op_code = event['op']
            if op_code == 11:
                print('heartbeat received')
        except:
            pass