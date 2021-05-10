"""
Unit tests for video synth controller
"""
from io import StringIO
import pytest
from model_video_synth import VideoSynth
from controller_video_synth import (YtController, Mp3Controller,)

# Define set of test cases

# YouTube Controller Cases
YtController_cases = [
    # Testing a normal youtube link
    (["https://www.youtube.com/watch?v=j9bIL53BxsI", "UHHH"], "audio_files/UHHH.mp3"),
]
# Mp3 Controller Cases
Mp3Controller_cases = [
    # Testing a file whose folder is in the same directory
    ("/home/softdes/video-synth/audio_files/UHHH.mp3",
     "/home/softdes/video-synth/audio_files/UHHH.mp3"),
    # Testing a file whose location is not in the same directory
    ("/some_folder/some_file.mp3", "/some_folder/some_file.mp3"),
]


@pytest.mark.parametrize("link_input, filepath", YtController_cases)
def test_yt_controller(link_input, filepath, monkeypatch):
    """
    Test that the YtController properly sets the file path of the video
    it downloads

    Args:
        link_input: A list that contains the link to the youtube video
                    and its title.
        filepath: A string which represents the correct file path of the
                    downloaded video.
    """
    user_input = StringIO(link_input[0]+"\n"+link_input[1])
    test = VideoSynth()
    controller = YtController(test)
    monkeypatch.setattr('sys.stdin', user_input)
    controller.create_file_path()
    assert test.file_path() == filepath


@pytest.mark.parametrize("file_input, filepath", Mp3Controller_cases)
def test_mp3_controller(file_input, filepath, monkeypatch):
    """
    Test that the Mp3Controller properly sets the file path of the file
    it was given.

    Args:
        file_input: A string representing the file path of the mp3 being
                    analyzed.
        filepath: A string which represents the correct file path of the
                    downloaded video.
    """
    user_input = StringIO(file_input)
    test = VideoSynth()
    controller = Mp3Controller(test)
    monkeypatch.setattr('sys.stdin', user_input)
    controller.create_file_path()
    assert test.file_path() == filepath
