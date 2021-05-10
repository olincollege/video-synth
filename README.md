# Read Me - Video Synth

## Project Summary
Video Synth is a python based program which analyzes an mp3 file and uses key audio features to from that file to draw or animate a perlin flower. The goal of this program was to visualize audio in a visually appealing way while exploring regenerative art and audio processing libararies. Mp3 files can be provided with a direct file path or downloaded with a youtube link. Audio features used to generate the perlin flower are the beat onset, the beat onset strength, and the pitch class. The beat onset is used to deterimine when a ring of the flower is drawn, the beat onset strength is used to determine the raidus of the ring, and the pitch class is used to determine the color of the ring.

## Libraries
The following is the list of libraries that need to be downloaded in order to use our program.
* Librosa - https://librosa.org/doc/main/index.html
* Processing-py - https://py.processing.org/
* Youtube-DL - https://youtube-dl.org/
* Perlin-Noise - https://pypi.org/project/perlin-noise/
* tqdm - https://pypi.org/project/tqdm/
* FFmpeg - https://www.ffmpeg.org/

Other libraries that are used:
* ArgParse
* abc
* numpy
* math

## Code Changes
No Changes are needed to run this program.  

## Usage
Install all the files found in this github repository.

In a python environment run the file `video_synth.py`.
Our program has various options which can be explored at any time by running `video_synth.py -h` or `video_synth.py --help`

### Commands

`video_synth.py` | Runs the default video synth. Generates a still image from the file path of an mp3 file.  
`video_synth.py -y` | Generates a still image from a YouTube link.  
`video_synth.py --youtube` | Generates a still image from a YouTube link.  
`video_synth.py -a` | Generates an animation from the file path of an mp3 file.  
`video_synth.py --animation` | Generates an animation from the file path of an mp3 file.  
`video_synth.py -y -a` | Generates an animation from a YouTube link.  
`video_synth.py -y --animation` | Generates an animation from a YouTube link.  
`video_synth.py --youtube -a` | Generates an animation from a YouTube link.  
`video_synth.py --youtube --animation` | Generates an animation from a YouTube link.  
`video_synth.py -h` | Displays a help menu.  
`video_synth.py --help` | Displays a help menu.  

#### Contact
Feel free to reach out to us at *pythonvisualsynthesizer@gmail.com* if you have any comments or questions.
