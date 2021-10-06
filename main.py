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
SKIP = '!!skip'
QUEUE = '!!queue'
DEBUG = '!!debug'

def main():
    q = queue.Queue(1)
    t1 = threading.Thread(target=websocket_logger.initialize, args=(q,))
    t1.start()

    songName = ''

    while True:
        if q.full() and ('!!' in (message := q.get())):

            if PLAY in message:
                if len(message) == len(PLAY):
                    if Player.unpause(): message_sender.send_message(f'Resuming **{songName}**')
                else:
                    payloadIndex = len(PLAY) + 1
                    payload = message[payloadIndex:]
                    songDict = youtube_handler.get_video(payload)
                    Player.add_to_queue(songDict)
                    #songName = songDict['title']
                    #songID = songDict['id']
                    #Player.play(f'cache/{songID}.mp3')
                    #message_sender.send_message(f'Playing **{songName}**')
                    cache_manager.clean_cache()

            elif PAUSE in message:
                if Player.pause(): message_sender.send_message(f'Paused **{songName}**')

            elif STOP in message:
                if Player.stop(): message_sender.send_message('**Track Stopped!**')

            elif LOOP in message:
                if Player.loop(): message_sender.send_message(f'Looping **{songName}**')

            elif SKIP in message:
                if Player.play_next(): message_sender.send_message(f'Skipped **{songName}**')

            elif QUEUE in message:
                message_sender.send_message(Player.get_queue())

            elif DEBUG in message:
                message_sender.send_message(Player.debug())
            
        Player.update()


if __name__ == "__main__":
    main()