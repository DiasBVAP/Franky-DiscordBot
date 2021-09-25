import downloader
import player
import websocket_logger

import threading
import queue

if __name__ == "__main__":
    q = queue.Queue(1)
    message = ''

    t1 = threading.Thread(target=websocket_logger.initialize, args=(q,))
    t1.start()

    while True:
        if q.full():
            message = q.get()

        if '!batata' in message:
            if 'https' in message:
                linkIndex = message.index('https')
                link = message[linkIndex:]
                downloader.download_music(link)
                player.play_music('teste.wav')
