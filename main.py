import youtube_handler
import player
import websocket_logger
import message_sender

import threading
import queue

#KEYWORDS DECLARATION
PLAY = '!!play'
PAUSE = '!!pause'
STOP = '!!stop'

def main():
    q = queue.Queue(1)

    t1 = threading.Thread(target=websocket_logger.initialize, args=(q,))
    t1.start()

    songName = ''

    while True:
        if q.full():
            message = q.get()
            if PLAY in message:
                if len(message) == len(PLAY):
                    player.unpause_music()
                    message_sender.send_message(f'Resuming **{songName}**')
                else:
                    payloadIndex = len(PLAY) + 1
                    payload = message[payloadIndex:]
                    songName = youtube_handler.get_video(payload)
                    player.play_music(f'cache/{songName}.wav')
                    message_sender.send_message(f'Playing **{songName}**')
            elif PAUSE in message:
                player.pause_music()
                message_sender.send_message(f'Paused **{songName}**')
            elif STOP in message:
                player.stop_music()
                message_sender.send_message('**Track Stopped!**')


if __name__ == "__main__":
    main()