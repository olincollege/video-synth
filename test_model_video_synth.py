"""
Unit tests for the video synth model.
"""
import os
import pytest
from model_video_synth import VideoSynth

# Define set of test cases

set_filepath_cases = [
    # Check that an empty file path stays empty
    ("", ""),
    # Check that a normal file path is properly set
    ("filepath", "filepath"),
]

audio_features_list_cases = [
    # Check that an empty audio features list stays empty
    ([], []),
    # Check that a normal audio_features_list is properly called
    ([[0, 0, 0], [1, 2, 4]], [[0, 0, 0], [1, 2, 4]])
]

create_audio_features_list_cases = [
    # Check that an audio_features_list is properly created from a file path
    ("/audio_files/test.mp3", [8153, 8153])
]


@pytest.mark.parametrize("filepath_input, filepath", set_filepath_cases)
def test_set_filepath(filepath_input, filepath):
    """
    Test that the file path is properly set for the model.

    Args:
        filepath_input: A string representing what the file path should be
                        set too.
        filepath: A string which represents the correct file path of the
                    downloaded video.
    """
    test = VideoSynth()
    test.set_filepath(filepath_input)
    assert test.file_path() == filepath

@pytest.mark.parametrize("audio_features_input, audio_features", audio_features_list_cases)
def test_audio_features_list(audio_features_input, audio_features):
    """
    Test that the audio_features_list is properly called

    Args:
        audio_features_input = A list representing what the audio_features_list
                                is being set too.
        audio_features: A list representing what the audio_features_list should be.
    """
    test = VideoSynth()
    test.set_audio_features_list(audio_features_input)
    assert test.audio_features_list() == audio_features


@pytest.mark.parametrize("file_path, list_lengths", create_audio_features_list_cases)
def test_create_audio_features_list(file_path, list_lengths):
    """
    Test that an audio_features_list is properly created.

    Args:
        file_path: A string representing the file path of the file.
        list_lengths: A list containting integers representing the lengths
                    that each inner list of audio_features_list should be.
    """
    test = VideoSynth()
    test.set_filepath(os.getcwd()+file_path)
    test.create_audio_features_list()
    for i in range(1):
        assert len(test.audio_features_list()[i]) == list_lengths[i]
