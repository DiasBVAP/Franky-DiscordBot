from __future__ import unicode_literals
from requests import get
import youtube_dl


def get_video(arg: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'cache/%(id)s.%(etx)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            get(arg) 
        except:
            video = ydl.extract_info(f"ytsearch:{arg}", download=True)['entries'][0]
        else:
            video = ydl.extract_info(arg, download=True)
    return video