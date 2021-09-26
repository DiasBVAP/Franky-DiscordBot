import downloader
import player
import websocket_logger
import searcher

import threading
import queue

#KEYWORDS DECLARATION
PLAY = '!!play'
PAUSE = '!!pause'
STOP = '!!stop'

if __name__ == "__main__":
    q = queue.Queue(1)
    message = ''

    t1 = threading.Thread(target=websocket_logger.initialize, args=(q,))
    t1.start()

    while True:
        if q.full():
            message = q.get()
            if PLAY in message:
                if 'youtube.com' in message:
                    linkIndex = message.index('youtube')
                    link = message[linkIndex:]
                    downloader.download_music(link)
                    player.play_music('teste.wav')
                else:
                    searchIndex = len(PLAY)
                    searchTerm = message[searchIndex:]
                    link = searcher.search_video(searchTerm)
                    downloader.download_music(link)
                    player.play_music('teste.wav')
