"""
View for Video Synth
"""
import math
from abc import ABC, abstractmethod
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


class ProcessingView(VideoSynthView):
    """
    Processing view of Video Synth.

    Attributes:
        _audio_features: A list of audio_features
        _app: A processing app represent the processing app being used.
    """

    def draw(self):
        """
        Drawing method for the processing view of the Video Synthesizer.
        """
        # Set up for drawing
        app = self.processing_app
        audio_features = self.audio_features
        noise = PerlinNoise(octaves=3)
        center = 400
        noise_incremementer = 1
        # Colors for each pitch class
        colors = {0: (240, 58, 58), 1: (240, 119, 58), 2: (240, 170, 58), 3: (240, 213, 58),
                  4: (234, 240, 58), 5: (198, 240, 58), 6: (131, 240, 58), 7: (58, 240, 97),
                  8: (58, 240, 207), 9: (58, 219, 240), 10: (58, 134, 240), 11: (82, 58, 240)}
        audio_features_list_length = len(audio_features[0])-1
        # Main Drawing Loop
        for feature_index in tqdm(range(0, audio_features_list_length, 3)):
            # Set the color
            index = audio_features[1][feature_index]
            app.stroke(colors[index][0], colors[index]
                       [1], colors[index][2], 34)
            noise_incremementer += 1
            app.beginShape()
            # Loop for drawing a single ring
            for i in range(0, 361, 18):
                rad = 50 + 500 * audio_features[0][feature_index]

                radius = 2*rad + rad * \
                    noise([i/100, float(noise_incremementer)/150])
                x_coord = center + radius * math.cos(math.radians(i))
                y_coord = center + radius * math.sin(math.radians(i))

                app.curveVertex(x_coord, y_coord)

            app.endShape("CLOSE")
            # Update processing window
            app.redraw()


class ProcessingAnimationView(VideoSynthView):
    """
    Animation processing view of Video Synth.

    Attributes:
        _audio_features: A list of audio_features
        _app: A processing app represent the processing app being used.
    """
    def draw(self):
        """
        Drawing method for animation processing view of the Video Synthesizer.
        """
        # Set up for drawing
        app = self.processing_app
        audio_features = self.audio_features
        noise = PerlinNoise(octaves=3)
        center = 400
        noise_incremementer = 1
        # Colors for each pitch class
        colors = {0: (240, 58, 58), 1: (240, 119, 58), 2: (240, 170, 58), 3: (240, 213, 58),
                  4: (234, 240, 58), 5: (198, 240, 58), 6: (131, 240, 58), 7: (58, 240, 97),
                  8: (58, 240, 207), 9: (58, 219, 240), 10: (58, 134, 240), 11: (82, 58, 240)}
        audio_features_list_length = len(audio_features[0])-1
        # Main drawing loop
        for feature_index in tqdm(range(0, audio_features_list_length, 3)):
            # Set the color
            index = audio_features[1][feature_index]
            app.stroke(colors[index][0], colors[index]
                       [1], colors[index][2], 34)
            noise_incremementer += 1
            app.beginShape()
            # Loop for drawing a single ring
            for i in range(0, 361, 18):
                rad = 10 + 500 * audio_features[0][feature_index]

                radius = 2*rad + rad * \
                    noise([i/100, float(noise_incremementer)/150])
                x_coord = center + radius * math.cos(math.radians(i))
                y_coord = center + radius * math.sin(math.radians(i))
                app.curveVertex(x_coord, y_coord)

            app.endShape("CLOSE")
            # Update processing window
            app.redraw()
            # Clear processing window
            app.background(0, 0, 0)
