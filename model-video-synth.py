class VideoSynth:
    """
    VideoSynth with basic manipulation functionality.

    Attributes:
        _file_path
        _audio_features_list
    """
    
    def __init__(self):
        """
        Create a new, empty VideoSynth.
        """
        self._file_path = ""
        self._audio_features_list = []
    
    def load_filepath(self, file_location):
        self._file_path = file_location
    
    def audio_features_list(self):
        return self._audio_features_list
    
    def create_audio_features_list(self):
        #LibRosa Stuff
        
        #self._audio_features_list == LibRosa Data File