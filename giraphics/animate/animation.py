from giraphics.utilities.convert import *
from giraphics.graphing.fancygraph import *
from IPython.display import Image, SVG, Video
from giraphics.utilities.utils import Timer


class FrameGraphic(FancyGraph):
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                 transform="none", grouped=False):
        FancyGraph.__init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                            transform=transform, grouped=False)
        self.frame_index = 0
        self.last_frame = ''

    def press(self):
        self.svg.path = "vectors/g" + namer(self.frame_index) + ".svg"
        self.frame_index += 1
        self.last_frame = self.svg.canvas
        FancyGraph.save(self, clear=False)
        self.svg.canvas = self.svg.preamble


class Animation:
    def __init__(self, name, width, height, xlim, ylim, framerate=60, origin=[0, 0], pauses=True):
        create_directory("vectors", warnings=False)
        create_directory("rasters", warnings=False)
        self.frames = 0
        self.name = name
        self.width = width
        self.framerate = framerate
        self.height = height
        self.xlim = xlim
        self.ylim = ylim
        self.pauses = pauses
        self.plate = FrameGraphic(width, height, xlim, ylim, '', origin=origin)

    def pause(self, frames):
        if self.pauses:
            for i in range(frames):
                self.plate.svg.canvas = self.plate.last_frame
                self.plate.press()

    def develop(self, cleanup=True, warnings=True, workers=2, timeit=False):
        # Creating
        if timeit:
            T = Timer()
            T.start()
        create_raster_batch('vectors', 'g', 'p', 'rasters', self.plate.frame_index)
        filename = os.path.splitext(self.name)[0]
        if self.name.lower().endswith(('.gif')):
            os.system(f'convert -delay 20 -loop 0 rasters/*.png {filename}.gif')
        else:
            create_mpeg(self.name, 'p', "rasters", framerate=self.framerate, warnings=warnings)
        if cleanup:
            clean_up('vectors', 'rasters')

        if timeit:
            T.stop()

    def show(self):
        Video(self.name)

    def preview(self):
        # preview
        pass

    def every(self, n):
        # take every nth frame
        pass


    def skip_every(self, n):
        # skip every n frames
        pass