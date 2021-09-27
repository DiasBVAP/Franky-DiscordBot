import downloader
import player
import websocket_logger
import searcher
import message_sender

import threading
import queue

#KEYWORDS DECLARATION
PLAY = '!!play'
PAUSE = '!!pause'
STOP = '!!stop'

def main():
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
                    message_sender.send_message('Playing Track!')
                elif len(message) == len(PLAY):
                    player.unpause_music()
                    message_sender.send_message('Rusuming Track!')
                else:
                    searchIndex = len(PLAY) + 1
                    searchTerm = message[searchIndex:]
                    link = searcher.search_video(searchTerm)
                    downloader.download_music(link)
                    player.play_music('teste.wav')
                    message_sender.send_message('Playing Track!')
            elif PAUSE in message:
                player.pause_music()
                message_sender.send_message('Track Paused!')
            elif STOP in message:
                player.stop_music()
                message_sender.send_message('Track Stopped!')


if __name__ == "__main__":
    main()