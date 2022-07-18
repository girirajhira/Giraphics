from giraphics.graphing.graph import *
from giraphics.animate.animation import Animation


## Creating the animation Object

# Animation parameters
width = 600
height = 600
xlim =  4
ylim = 4

# Length
seconds = 2 #s
frames = seconds*60


# Name of the File
name = 'basisVideo.mp4'


A = Animation(name, frames, width, height, xlim, ylim, framerate=60, origin=[0,0])



## Introduction
intro_seconds = 2 #s
intro_frames = 60*intro_seconds


for i in range(intro_frames):
    A.plate.bg(colour='black')
    A.plate.grid(colour='white', opac=0.5*i/intro_frames)
    A.plate.axes(colour='white')
    A.plate.press()


A.develop(cleanup=False)