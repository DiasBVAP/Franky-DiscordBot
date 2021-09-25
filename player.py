from pygame import mixer
import time

def play_music(fileName: str):
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(fileName)
    mixer.music.set_volume(1.0)
    mixer.music.play()
    while mixer.music.get_busy(): 
        time.sleep(1)
    mixer.quit()