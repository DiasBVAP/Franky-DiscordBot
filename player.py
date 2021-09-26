from pygame import mixer
import time

def play_music(fileName: str):
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(fileName)
    mixer.music.set_volume(1.0)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def stop_music():
    mixer.music.stop()
    mixer.quit()

def unpause_music():
    mixer.music.unpause()