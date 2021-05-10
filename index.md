## Our objective:
As lovers of all things music and Python, we wanted to find a way for people to visualize audio easily in a format that is both pleasing to the eye and meaningful.
![Visualization of a cover of Daft Punk's song, Harder, Better, Faster stronger](daft_punk_visual.png)
A youtube video to the song accompanying the visualization above can be found [here.](https://youtu.be/RHu0ALxqUIo)

## What we did: 
We created a program that processes a user inputted .mp3 file, extracts a few key audio features from the file, and maps these features to various characteristics of a [perlin noise flower](https://www.benfrederickson.com/flowers-from-simplex-noise/) that is generated(example of this visual can be seen above).

## How does it all work? 
When processing an audio file and generating the flower, our program extracts data representing: 
* The beat onset and onset strength of the song 
  * The beat onset data determines when a ring of the perlin flower is drawn, meaning that for every 'beat' detected in the song, a ring is drawn.
  * The beat onset strength data determines how large each ring is based on how strong each beat is within the song 
* The pitch class of all of the harmonic components of the inputted song
  * The pitch class data is a dataset representing the most prominent notes at thousands of points during the song; these notes are mapped to colors for the rings. 

## Some tools that we used for this
We researched many musical, visual, and data manipulation and storage Python libraries, however we decided on using these specific libraries:
* [Librosa](https://librosa.org/doc/main/index.html)
  * We use Librosa to process audio and pull out the necessary data
* [Processing-py](https://py.processing.org/)
  * Processing is used to generate the perlin flower visual
* [Youtube-DL](https://youtube-dl.org/)
  * Youtube-Dl allows us to download youtube videos from their link 
* [Perlin-Noise](https://pypi.org/project/perlin-noise/)
  * Perlin-Noise is used to generate the perlin noise for the flower
* [tqdm](https://pypi.org/project/tqdm/)
  * tqdm provides the user with a progress bar for the art generation

## How you can use it! 

