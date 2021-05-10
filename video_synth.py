"""
Main method for video synth
"""
import argparse
import processing_py
from model_video_synth import VideoSynth
from controller_video_synth import YtController
from controller_video_synth import Mp3Controller
from video_synth_view import ProcessingView
from video_synth_view import ProcessingAnimationView

# Set up for argparse
parser = argparse.ArgumentParser(description='Creates and runs a VideoSynth')
parser.add_argument("-y", "--youtube",
                    help="Download mp3 from youtube (default: file path of mp3)",
                    action="store_true")
parser.add_argument("-a", "--animation",
                    help="Turn on Video Synth Animation (default: no animation)",
                    action="store_true")
args = parser.parse_args()

# Create Video Synth object
synth = VideoSynth()
# Determine Which controller to use
if args.youtube:
    controller = YtController(synth)
else:
    controller = Mp3Controller(synth)
# Create a controller object
controller.create_file_path()
synth.create_audio_features_list()
# Set up for processing-py
app = processing_py.App(800, 800)
app.background(0, 0, 0)
app.noFill()
# Determine which view to use
if args.animation:
    view = ProcessingAnimationView(synth.audio_features_list(), app)
else:
    view = ProcessingView(synth.audio_features_list(), app)
# Draw/Animate the perlin flower
view.draw()
