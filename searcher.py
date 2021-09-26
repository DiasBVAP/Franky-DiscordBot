from youtube_search import YoutubeSearch
import json

def search_video(name: str) -> str:

    results = YoutubeSearch(name, max_results=1).to_dict()
    actual_dict = results[0]    #This is fucking dumb. to_dict() returns an unidimensional list with the actual dictionary inside it.
    url = 'youtube.com' + actual_dict['url_suffix']
    return url