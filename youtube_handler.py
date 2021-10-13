from __future__ import unicode_literals
from requests import get
import youtube_dl

import cache_manager
import messenger


def get_video(arg: str) -> dict:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'cache/%(id)s.%(etx)s',
        'noplaylist': True,
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
            video = ydl.extract_info(f'ytsearch:{arg}', download=False)['entries'][0]
            if cache_manager.is_in_cache(video['id']):
                return video
            else:
                messenger.send('**Downloading . . .**')
                ydl.download(['https://www.youtube.com/watch?v=' + video['id']])
        else:
            video = ydl.extract_info(arg, download=False)
            if cache_manager.is_in_cache(video['id']):
                return video
            else:
                messenger.send('**Downloading . . .**')
                ydl.download(['https://www.youtube.com/watch?v=' + video['id']])
    return video

def search(arg: str) -> dict:
    with youtube_dl.YoutubeDL() as ydl:
        video = ydl.extract_info(f'ytsearch:{arg}', download=False)['entries'][0]
    return video