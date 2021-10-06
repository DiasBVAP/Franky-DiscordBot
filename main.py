import threading
import queue

import youtube_handler
from player_class import Player
import websocket_logger
import message_sender
import cache_manager

#KEYWORDS DECLARATION
PLAY = '!!play'
PAUSE = '!!pause'
STOP = '!!stop'
LOOP = '!!loop'

def main():
    q = queue.Queue(1)
    t1 = threading.Thread(target=websocket_logger.initialize, args=(q,))
    t1.start()

    songName = ''

    while True:
        if q.full() and ('!!' in (message := q.get())):

            if PLAY in message:
                if len(message) == len(PLAY):
                    if Player.unpause():
                        message_sender.send_message(f'Resuming **{songName}**')
                    else:
                        message_sender.send_message('**No song to play**')
                else:
                    payloadIndex = len(PLAY) + 1
                    payload = message[payloadIndex:]
                    songDict = youtube_handler.get_video(payload)
                    songName = songDict['title']
                    songID = songDict['id']
                    Player.play(f'cache/{songID}.mp3')
                    message_sender.send_message(f'Playing **{songName}**')
                    cache_manager.clean_cache()

            elif PAUSE in message:
                if Player.pause():
                    message_sender.send_message(f'Paused **{songName}**')
                else:
                    message_sender.send_message('**No song to pause**')

            elif STOP in message:
                if Player.stop():
                    message_sender.send_message('**Track Stopped!**')
                else:
                    message_sender.send_message('**No song to stop**')

            elif LOOP in message:
                if Player.loop():
                    message_sender.send_message(f'Looping **{songName}**')
                else:
                    message_sender.send_message('**No song to loop**')


if __name__ == "__main__":
    main()