import os
from dotenv import load_dotenv

def clean_cache() -> None:
    load_dotenv()
    MAX_CACHE_SIZE = int(os.environ.get('MAX_CACHE_SIZE'))

    cache_size = get_folder_size('cache')
    if cache_size > MAX_CACHE_SIZE:
        oldestFile = get_oldest_file('cache')
        os.remove('cache/' + oldestFile)

def get_folder_size(folder: str) -> float:
    sizeBytes = 0
    for file in os.listdir(folder):
        sizeBytes += os.path.getsize('cache/' + file)
    sizeMega = sizeBytes / (1024 * 1024)
    return sizeMega

def get_oldest_file(folder: str) -> None:
    oldestFile = 'cache/' + os.listdir(folder)[0]
    for file in os.listdir(folder):
        if os.path.getctime('cache/' + file) > os.path.getctime(oldestFile):
            oldestFile = file
    return oldestFile

def is_in_cache(target: str) -> bool:
    for file in os.listdir('cache'):
        if target + '.mp3' == file:
            return True
    return False
