from pygame import mixer

class Player():

    #flags
    is_loaded = False
    is_playing = False
    is_looping = False

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