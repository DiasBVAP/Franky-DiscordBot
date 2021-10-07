import threading
import queue

import youtube_handler
from player import Player
import logger
import messenger
import cache_manager

#KEYWORDS DECLARATION
PLAY = '!!play'
PAUSE = '!!pause'
STOP = '!!stop'
LOOP = '!!loop'
NEXT = '!!next'
LAST = '!!last'
QUEUE = '!!q'
DEBUG = '!!debug'

def main():
    q = queue.Queue(1)
    t1 = threading.Thread(target=logger.initialize, args=(q,))
    t1.start()

    songName = ''

    while True:
        if q.full() and ('!!' in (message := q.get())):

            if PLAY in message:
                if len(message) == len(PLAY):
                    if Player.unpause(): messenger.send(f'Resuming **{songName}**')
                else:
                    payloadIndex = len(PLAY) + 1
                    payload = message[payloadIndex:]
                    songDict = youtube_handler.get_video(payload)
                    songName = Player.add_to_queue(songDict)
                    messenger.send(f'Added to queue:\n**{songName}**')
                    cache_manager.clean_cache()

            elif PAUSE in message:
                if Player.pause(): messenger.send(f'Paused **{songName}**')

            elif STOP in message:
                if Player.stop(): messenger.send('**Queue Stopped!**')

            elif LOOP in message:
                if Player.loop(): messenger.send(f'Looping **{songName}**')

            elif NEXT in message:
                songName = Player.play_next()
                messenger.send(f'Playing next song:\n**{songName}**')

            elif LAST in message:
                songName = Player.play_last()
                messenger.send(f'Playing last song:\n**{songName}**')

            elif QUEUE in message:
                messenger.send(f'**{Player.get_queue()}**')

            elif DEBUG in message:
                messenger.send(Player.debug())
            
        songName = Player.update()


if __name__ == "__main__":
    main()