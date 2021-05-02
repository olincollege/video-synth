from abc import ABC, abstractmethod
import sys
from youtube_dl import YoutubeDL

class SongController:
    """
    """
    def __init__(self,VisualSynth):
        self._visual_synth = VisualSynth
    
    @property
    def visual_synth(self):
        return self._visual_synth
    @abstractmethod
    def create_file_path(self):
        pass

class YtController(SongController):
    """
    """
    def create_file_path(self):
        yt_url = input('Paste in a youtube link that you want to visualize!')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'audio_files/%(title)s.%(ext)s',
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        file_path = input('Paste the title of the youtube video')
        file_path = 'audio_files/'+file_path+'.mp3'
        self.visual_synth.set_filepath(file_path)
class Mp3Controller(SongController):
    """
    """
    def create_file_path(self):
        file_path = input('Paste in the file path of the mp3 you want to visualize!')
        self.visual_synth.set_filepath(file_path)
    