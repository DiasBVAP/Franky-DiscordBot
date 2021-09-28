from pygame import mixer
import time

def play_music(fileName: str):
    try:
        mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
        mixer.music.load(fileName)
        mixer.music.set_volume(1.0)
        mixer.music.play()
    except:
        pass

def pause_music():
    try:
        mixer.music.pause()
    except:
        pass

def stop_music():
    try:
        mixer.music.stop()
        mixer.quit()
    except:
        pass

def unpause_music():
    try:
        mixer.music.unpause()
    except:
        pass
def loop_music():
    try:
        pos = mixer.music.get_pos() / 1000.0
        mixer.music.play(-1, pos)
    except:
        pass