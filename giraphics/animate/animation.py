from giraphics.utilities.convert import *
from giraphics.graphing.fancygraphs import *
from os import getcwd
from IPython.display import Image, SVG, Video


class Frame_graphic(FancyGraphs):
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                 transform="none", grouped=False):
        FancyGraphs.__init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                 transform="none", grouped=False)
        self.frame_index = 0

    def press(self):
        self.svg.path = "vectors/g" + namer(self.frame_index) + ".svg"
        self.frame_index += 1
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

    def develop(self, cleanup=True, warnings=True):
        # Creating
        create_raster_batch("vectors", 'g', 'p', "rasters", self.frames)
        create_mpeg(self.name, 'p', self.frames, "rasters", framerate=self.framerate, warnings=warnings)
        if cleanup:
            clean_up('vectors', 'rasters')


