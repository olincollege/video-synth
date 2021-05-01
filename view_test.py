from processing_py import *
from video_synth_view import *
import time

audio_features = [100,95,105,90,110]

app = App(600,600) # create window: width, height
app.background(0,0,0)
app.noFill()
app.stroke(255,0,0,25)

view = ProcessingView3(audio_features, app)

start = time.time()
view.draw()
total_time = (time.time() - start)

print(f"Total Time: {total_time}")