from abc import ABC, abstractmethod
from processing_py import *
import math
import random
from perlin_noise import PerlinNoise
from tqdm import tqdm

class VideoSynthView(ABC):
    """
    View for the Video Synthesizer

    Attributes:
        _audio_features: A list of audio_features
        _app: A processing app represent the processing app being used.
    """

    def __init__(self, audio_features_list, processing_app):
        """
        Create a new VideoSynth view.
        """
        self._audio_features = audio_features_list
        self._app = processing_app

    @property
    def audio_features(self):
        """
        Return the value of the private attribute audio_features.
        """
        return self._audio_features
    
    @property
    def processing_app(self):
        """
        Return the value of the private attribute processing_app.
        """
        return self._app    
        
    @abstractmethod
    def draw(self):
        """
        Abstract method for drawing the video synth.
        """
        pass
                
class ProcessingView(VideoSynthView):
    """
    """

    def draw(self):
        """
        Drawing method for text view of the Video Synthesizer.
        """
        app = self.processing_app
        audio_features = self.audio_features
        
        noise = PerlinNoise(octaves=3)
        center_x = 400
        center_y = 400
    
        noise_incremementer = 1
        frame_count = 1
        colors = {0:(240,58,58), 1:(240, 119, 58), 2:(240,170,58), 3:(240, 213, 58), 4:(234, 240, 58), 5:(198, 240, 58), 6:(131, 240, 58), 7:(58, 240, 97), 8:(58, 240, 207), 9:(58, 219, 240), 10:(58, 134, 240), 11:(82, 58, 240)}
        audio_features_list_length = len(audio_features[0])-1
        for feature_index in tqdm(range(0, audio_features_list_length,3)):
            app.stroke(colors[audio_features[1][feature_index]][0],colors[audio_features[1][feature_index]][1],colors[audio_features[1][feature_index]][2],34)
            noise_incremementer += 1
            app.beginShape()
            for i in range(0,361,18): # 0,361,9 ~ 30FPS 0,451,45 ~ 50FPS
                r = 50 + 500 * audio_features[0][feature_index]
                
                radius = 2*r + r * noise([i/100,float(noise_incremementer)/150])
                x = center_x + radius * math.cos(math.radians(i)) 
                y = center_y + radius * math.sin(math.radians(i))
    
                app.curveVertex(x,y)

            app.endShape("CLOSE")
            app.redraw()

class ProcessingAnimationView(VideoSynthView):
    def draw(self):
        """
        Drawing method for text view of the Video Synthesizer.
        """
        app = self.processing_app
        audio_features = self.audio_features
        
        noise = PerlinNoise(octaves=3)
        center_x = 400
        center_y = 400
    
        noise_incremementer = 1
        colors = {0:(240,58,58), 1:(240, 119, 58), 2:(240,170,58), 3:(240, 213, 58), 4:(234, 240, 58), 5:(198, 240, 58), 6:(131, 240, 58), 7:(58, 240, 97), 8:(58, 240, 207), 9:(58, 219, 240), 10:(58, 134, 240), 11:(82, 58, 240)}
        audio_features_list_length = len(audio_features[0])-1
        for feature_index in tqdm(range(0, audio_features_list_length,3)):
            app.stroke(colors[audio_features[1][feature_index]][0],colors[audio_features[1][feature_index]][1],colors[audio_features[1][feature_index]][2])
            noise_incremementer += 1
            app.beginShape()
            for i in range(0,361,18): # 0,361,9 ~ 30FPS 0,451,45 ~ 50FPS
                r = 10 + 500 * audio_features[0][feature_index]
                
                radius = 2*r + r * noise([i/100,float(noise_incremementer)/150])
                x = center_x + radius * math.cos(math.radians(i)) 
                y = center_y + radius * math.sin(math.radians(i))
                app.curveVertex(x,y)

            app.endShape("CLOSE")
            app.redraw()
            app.background(0,0,0)
