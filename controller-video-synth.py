from abc import ABC, abstractmethod
import sys
from youtube_dl import YoutubeDL

class SongController:
    """
    """
    def __init__(self):
        pass

    @abstractmethod
    def create_file_path(self):
        pass

class YtController(SongController):
    """
    """
    def create_file_path(self):
        file_path = 'audio_files/%(title)s.%(ext)s'
        yt_url = input('Paste in a youtube link that you want to visualize!')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': file_path,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

class Mp3Controller(SongController):
    """
    """
    def create_file_path(self):
        pass