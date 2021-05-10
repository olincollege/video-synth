"""
Video Synth Controller.
"""
from abc import abstractmethod
from youtube_dl import YoutubeDL


class SongController:
    """
    Abstract class for the controller of the Video Synth.

    Attributes:
        _visual_synth: A visual_synth object respresenting the visual
                        synth being controlled.
    """

    def __init__(self, VisualSynth):
        self._visual_synth = VisualSynth

    @property
    def visual_synth(self):
        """
        Return the value of the private attribute visual_synth.
        """
        return self._visual_synth

    @abstractmethod
    def create_file_path(self):
        """
        Abstract method for creating a file path for the video synth.
        """

class YtController(SongController):
    """
    Controller for the YouTube based version of the Video Synth.

    Attributes:
        _visual_synth: A visual_synth object respresenting the visual
                        synth being controlled.
    """

    def create_file_path(self):
        """
        Creates a file path for the video synth from a youtube video.
        """
        # Takes user input for youtube url
        yt_url = input('Paste in a youtube link that you want to visualize! ')
        # Options for YoutubeDL
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'audio_files/%(title)s.%(ext)s',
        }
        # Calling YoutubeDL to download video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        # Takes user input to properly create file path
        file_path = input('Paste the title of the youtube video! ')
        file_path = 'audio_files/'+file_path+'.mp3'
        # Sets the file path of the visual synth
        self.visual_synth.set_filepath(file_path)


class Mp3Controller(SongController):
    """
    Controller for the Mp3 file based version of the Video Synth.

    Attributes:
        _visual_synth: A visual_synth object respresenting the visual
                        synth being controlled.
    """

    def create_file_path(self):
        """
        Creates a file path for the video synth from a given file.
        """
        # Takes user input to create file path
        file_path = input(
            'Paste in the file path of the mp3 you want to visualize! ')
        # Sets the file path of the visual synth
        self.visual_synth.set_filepath(file_path)
