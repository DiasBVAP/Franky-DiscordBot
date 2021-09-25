from __future__ import unicode_literals
import youtube_dl

def download_music(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'teste',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])