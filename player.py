from pygame import mixer    

class Player():

    #flags
    is_loaded = False
    is_playing = False
    queue_looping = False
    on_queue = False

    #queue
    single_song = {}
    myQueue = []
    current_song = 0

    @classmethod
    def update(cls) -> str:
        if cls.is_playing and cls.is_loaded and (not mixer.music.get_busy()):
            if (not cls.queue_looping) and (cls.current_song == len(cls.myQueue) - 1): # If on queue, but not looping
                return cls.myQueue[cls.current_song]
            if not cls.on_queue: # If not on queue
                return cls.single_song
            cls.play_next()
        if cls.on_queue:
            return cls.myQueue[cls.current_song]['title']
        return cls.single_song['title']

    @classmethod
    def play_next(cls) -> str:
        if cls.current_song + 1 < len(cls.myQueue):
            songID = cls.myQueue[cls.current_song + 1]['id']
            cls.play(f'cache/{songID}.mp3')
            cls.current_song += 1
        else:
            songID = cls.myQueue[0]['id']
            cls.play(f'cache/{songID}.mp3')
            cls.current_song = 0
        cls.on_queue = True
        return cls.myQueue[cls.current_song]['title']

    @classmethod
    def play_last(cls) -> str:
        if cls.current_song > 0:
            songID = cls.myQueue[cls.current_song - 1]['id']
            cls.play(f'cache/{songID}.mp3')
            cls.current_song -= 1
        else:
            songID = cls.myQueue[len(cls.myQueue) - 1]['id']
            cls.play(f'cache/{songID}.mp3')
            cls.current_song = len(cls.myQueue) - 1
        cls.on_queue = True
        return cls.myQueue[cls.current_song]['title']

    @classmethod
    def add_to_queue(cls, songDict: dict) -> str:
        cls.myQueue.append(songDict)
        if not (cls.is_playing or cls.is_loaded): 
            songID = songDict['id']
            cls.play(f'cache/{songID}.mp3')
            cls.on_queue = True
        return songDict['title']

    @classmethod
    def remove_from_queue(cls, songIndex: int) -> str:
        if len(cls.myQueue) > 1:
            songName = cls.myQueue.pop(songIndex)['title']
            if songIndex == cls.current_song: 
                cls.current_song -= 1
                Player.play_next()
            return songName
        return None

    @classmethod
    def get_queue(cls) -> str:
        if len(cls.myQueue) > 0:
            nameList = []
            i = 1
            for song in cls.myQueue:
                nameList.append(str(i) + '. ' + song['title'])
                i += 1
            return '\n'.join(nameList)
        return 'Queue empty!'

    @classmethod
    def play(cls, fileName: str) -> None:
        mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
        mixer.music.load(fileName)
        mixer.music.set_volume(1.0)
        mixer.music.play()
        cls.is_playing = True
        cls.is_loaded = True

    @classmethod
    def pause(cls) -> bool:
        if cls.is_playing:
            mixer.music.pause()
            cls.is_playing = False
            return True
        return False

    @classmethod
    def stop(cls) -> bool:
        if cls.is_loaded:
            mixer.music.stop()
            mixer.quit()
            cls.myQueue.clear()
            cls.current_song = 0
            cls.is_loaded = False
            cls.is_playing = False
            return True
        return False

    @classmethod
    def unpause(cls) -> bool:
        if (not cls.is_playing) and cls.is_loaded:
            mixer.music.unpause()
            cls.is_playing = True
            return True
        return False

    @classmethod    
    def loop(cls) -> bool:
        if cls.is_loaded:
            pos = mixer.music.get_pos() / 1000.0
            mixer.music.play(-1, pos)
            return True
        return False

    @classmethod
    def flip_qloop(cls) -> bool:
        cls.queue_looping = not cls.queue_looping
        return cls.queue_looping    