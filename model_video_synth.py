import librosa
import numpy as np
import librosa.display

class VideoSynth:
    """
    VideoSynth with basic manipulation functionality.

    Attributes:
        _file_path
        _audio_features_list
        _harmonic
        _onset_beat_strength
        _tempo
    """
    
    def __init__(self):
        """
        Create a new, empty VideoSynth.
        """
        self._file_path = ""
        self._audio_features_list = []
    
    def set_filepath(self, file_location):
        self._file_path = file_location
    
    def audio_features_list(self):
        return self._audio_features_list
    
    def create_audio_features_list(self):
        #LibRosa Stuff

        y, sr = librosa.load(self._file_path)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        chroma_harmonic = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr, bins_per_octave=36)
        onset_env = librosa.onset.onset_strength(y, sr=sr, aggregate=np.median)
        tempo = librosa.beat.beat_track(y=y_percussive, sr=sr, onset_envelope=onset_env)
        
        self._harmonic = chroma_harmonic.flatten()
        self._onset_beat_strength = librosa.util.normalize(onset_env)
        self._tempo = tempo
        maxInRows = np.amax(self._harmonic, axis=0)
        result = np.where(self._harmonic == np.amax(self._harmonic))
        self._audio_features_list = [self._onset_beat_strength,result[0]]
    
    def tempo(self):
        return self._tempo
        