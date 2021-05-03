from model_video_synth import VideoSynth
from controller_video_synth import YtController
from video_synth_view import ProcessingView3
from processing_py import *

synth = VideoSynth()
controller = YtController(synth)
controller.create_file_path()
synth.create_audio_features_list()

app = App(800,800)
app.background(0,0,0)
app.noFill()
view = ProcessingView3(synth.audio_features_list(), app)

view.draw()
