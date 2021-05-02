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
        noise = PerlinNoise(octaves=3)
        center_x = 300
        center_y = 300
    
        noise_incremementer = 1
        frame_count = 300

        for c in range(frame_count):
            #app.stroke(random.randint(0,255),random.randint(0,255),random.randint(0,255),70)  
            noise_incremementer += 1
            app.beginShape()
            for i in range(0,361,9): # 0,361,9 ~ 30FPS 0,451,45 ~ 50FPS

                radius = 200 + 100 * noise([i/100,float(noise_incremementer)/150])
                x = center_x + radius * math.cos(math.radians(i)) 
                y = center_y + radius * math.sin(math.radians(i))
        
                app.curveVertex(x,y)

            app.endShape("CLOSE")
            app.redraw()
            
class ProcessingView2(VideoSynthView):
    """
    """

    def draw(self):
        """
        Drawing method for text view of the Video Synthesizer.
        """
        app = self.processing_app
        audio_features = self.audio_features
        
        noise = PerlinNoise(octaves=3)
        center_x = 300
        center_y = 300
    
        noise_incremementer = 1
        frame_count = 10
        for z in audio_features:
            
            for c in range(frame_count):
                app.stroke(random.randint(0,255),random.randint(0,255),random.randint(0,255),70)  
                noise_incremementer += 1
                app.beginShape()
                for i in range(0,361,9): # 0,361,9 ~ 30FPS 0,451,45 ~ 50FPS

                    radius = 2*z + z * noise([i/100,float(noise_incremementer)/150])
                    x = center_x + radius * math.cos(math.radians(i)) 
                    y = center_y + radius * math.sin(math.radians(i))
        
                    app.curveVertex(x,y)

                app.endShape("CLOSE")
                app.redraw()
                
class ProcessingView3(VideoSynthView):
    """
    """

    def draw(self):
        """
        Drawing method for text view of the Video Synthesizer.
        """
        app = self.processing_app
        audio_features = self.audio_features
        
        noise = PerlinNoise(octaves=3)
        center_x = 300
        center_y = 300
    
        noise_incremementer = 1
        frame_count = 1
        audio_features_list_length = len(audio_features[0])-1
        for feature_index in tqdm(range(0, audio_features_list_length,2)):
            for frame_index in range(frame_count):
                app.stroke(random.randint(0,255),random.randint(0,255),random.randint(0,255),70)  
                noise_incremementer += 1
                app.beginShape()
                for i in range(0,361,9): # 0,361,9 ~ 30FPS 0,451,45 ~ 50FPS

                    #r = frame_index*(audio_features[feature_index+1]-audio_features[feature_index])/frame_count 
                    #r += audio_features[feature_index]
                    r = 50 + 200 * audio_features[1][feature_index]
                    radius = 2*r + r * noise([i/100,float(noise_incremementer)/150])
                    x = center_x + radius * math.cos(math.radians(i)) 
                    y = center_y + radius * math.sin(math.radians(i))
        
                    app.curveVertex(x,y)

                app.endShape("CLOSE")
                app.redraw()
                #app.background(0,0,0)
                