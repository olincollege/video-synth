from model_video_synth import VideoSynth
from controller_video_synth import YtController
from controller_video_synth import Mp3Controller
from video_synth_view import ProcessingView
from video_synth_view import ProcessingAnimationView
from processing_py import *
import argparse

parser = argparse.ArgumentParser(description='Creates and runs a VideoSynth')
parser.add_argument("-y","--youtube", help = "Download mp3 from youtube (default: file path of mp3", action = "store_true")
parser.add_argument("-a","--animation", help = "Turn on Video Synth Animation (default: no animation", action = "store_true")
args = parser.parse_args()

synth = VideoSynth()
if args.youtube:
    controller = YtController(synth)
else:
    controller = Mp3Controller(synth)

controller.create_file_path()
synth.create_audio_features_list()

app = App(800,800)
app.background(0,0,0)
app.noFill()

if args.animation:
    view = ProcessingAnimationView(synth.audio_features_list(), app)
else:
    view = ProcessingView(synth.audio_features_list(), app)

view.draw()
