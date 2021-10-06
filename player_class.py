from pygame import mixer

class MyQueue():
    
    myQueue = []
    current_song = 0

    @classmethod
    def next(cls) -> None:
        pass
    
    @classmethod
    def last(cls) -> None:
        pass

class Player():

    #flags
    is_loaded = False
    is_playing = False
    is_looping = False

    music_ended = False

    #queue
    myQueue = []
    current_song = 0

    @classmethod
    def update(cls) -> None:
        #if playing, but not busy -> music ended
        if cls.is_playing and cls.is_loaded and (not mixer.music.get_busy()): cls.music_ended = True
        #if music ended, try to play next, and music_ended = False
        if cls.music_ended:
            cls.play_next()
            cls.music_ended = False

    @classmethod
    def play_next(cls) -> None:
        #get next song id
        songID = cls.myQueue[cls.current_song + 1]['id']
        #play next song
        cls.play(f'cache/{songID}.mp3')
        #increment current_song
        cls.current_song += 1

    @classmethod
    def add_to_queue(cls, songDict: dict) -> None:
        cls.myQueue.append(songDict)
        #if no song is playing, try to play
        if not (cls.is_playing and cls.is_loaded): 
            songID = songDict['id']
            cls.play(f'cache/{songID}.mp3')

    @classmethod
    def remove_from_queue(cls, songDict: dict) -> None:
        cls.myQueue.remove(songDict)

    @classmethod
    def get_queue(cls) -> list:
        return cls.myQueue

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
            cls.is_loaded = False
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
        if (not cls.is_looping) and cls.is_loaded:
            pos = mixer.music.get_pos() / 1000.0
            mixer.music.play(-1, pos)
            cls.is_looping = True
            return True
        return False

    @classmethod
    def debug(cls) -> str:
        return f'is_loaded: {cls.is_loaded}\nis_playing: {cls.is_playing}\nis_looping: {cls.is_looping}\nget_busy: {mixer.music.get_busy()}'