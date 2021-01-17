from giraphics.utilities.convert import *
from giraphics.graphing.fancygraphs import *
from os import getcwd
from IPython.display import Image, SVG, Video


class Frame_graphic(FancyGraphs):
    def create_frame(self, i):
        self.svg.path = "vectors/g" + namer(i) + ".svg"
        FancyGraphs.save(self)
        self.svg.__init__(self.svg.path, self.width, self.height, transform="none", grouped=False)


class Animation:
    def __init__(self, name, frames, width, height, xlim, ylim, framerate=60, origin=[0, 0]):
        create_directory("vectors", warnings=False)
        create_directory("rasters", warnings=False)
        self.frames = frames
        self.name = name
        self.width = width
        self.framerate = framerate
        self.height = height
        self.xlim = xlim
        self.ylim = ylim
        self.plate = Frame_graphic(width, height, xlim, ylim, '', origin=origin)

    def develop(self, cleanup=False):
        # Creating
        create_raster_batch("vectors", 'g', 'p', "rasters", self.frames)
        create_mpeg(self.name, 'p', self.frames, dir=os.getcwd() + "/rasters", framerate=self.framerate, warnings=True)
        if cleanup:
            clean_up('vectors', 'rasters')


A = Animation('anime33.mp4', 120, 1000, 1000, 10, 10)
for i in range(0,120):
    A.plate.bg(colour="black")
    A.plate.draw_circle(0, 0, i * 0.1, fill="red")
    A.plate.create_frame(i)
A.develop()
print(6)
