"""
Model for Video Synth.
"""
import librosa
import numpy as np

class VideoSynth:
    """
    VideoSynth with basic manipulation functionality.

    Attributes:
        _file_path: A string representing the file path of the file being analyzed.
        _audio_features_list: A list containing the audio_features collected.
        _harmonic: A list containing the harmonic audio features.
        _onset_beat_strength: A list containg the beat onset strength audio features.
        _tempo: A list containing the tempo audio features.
    """

    def __init__(self):
        """
        Create a new, empty VideoSynth.
        """
        self._file_path = ""
        self._audio_features_list = []
        self._harmonic = []
        self._onset_beat_strength = []
        self._tempo = []

    def set_filepath(self, file_location):
        """
        Set the file path for the model

        Args:
            file_location: A string representing the file path of the mp3 file.
        """
        self._file_path = file_location

    def file_path(self):
        """
        Returns the value of the private attribute file_path
        """
        return self._file_path

    def set_audio_features_list(self, feature_list):
        """
        Set the audio_features_list for the model

        Args:
            feature_list: A list representing the audio_features_list.
        """
        self._audio_features_list = feature_list

    def audio_features_list(self):
        """
        Returns the value of the private attribute audio_features_list
        """
        return self._audio_features_list



    def create_audio_features_list(self):
        """
        Creates an audio feature list from analyzing an mp3 file.
        """
        # Using librosa to generate lists of different audio features.
        y_array, sample_rate = librosa.load(self._file_path)
        y_harmonic, y_percussive = librosa.effects.hpss(y_array)
        chroma_harmonic = librosa.feature.chroma_cqt(
            y=y_harmonic, sr=sample_rate, bins_per_octave=36)
        onset_env = librosa.onset.onset_strength(y_array, sr=sample_rate, aggregate=np.median)
        tempo = librosa.beat.beat_track(
            y=y_percussive, sr=sample_rate, onset_envelope=onset_env)
        # Store the list of audio features
        self._harmonic = chroma_harmonic
        self._onset_beat_strength = librosa.util.normalize(onset_env)
        self._tempo = tempo

        max_in_rows = np.argmax(self._harmonic, axis=0)
        # Set the audio_features_list
        self._audio_features_list = [self._onset_beat_strength, max_in_rows]
