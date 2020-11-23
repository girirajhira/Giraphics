from giraphics.utilities.convert import *
from giraphics.utilities.utils import *

Actions = {
    'sleep': 1
}


def linear_translate(start, end, frames = 100, start_frame=0, velocity=identity):
    s = np.array(start)
    e = np.array(end)
    def f(t):
        if t-start_frame <= frames:
            return s + velocity((t-start_frame)/frames)*(e-s)
        else:
            return s + velocity((frames-start_frame)/frames)*(e-s)
    return f

def pulse(a):
    pass

def linear():
    pass

class Feature:
    def __init__(self, action, frames, *params):
        self.action = action
        self.frames = frames
        self.params = params

class Sequence:
    def __init__(self, directory, width, height, xlim, ylim, framerate=60):
        self.name = directory
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.framerate = framerate

        # Stack of operations
        self.stack = []
        # Current layer
        self.layer = ""

        create_directory("ftp")
        create_directory("ftprast")

    def apply(self, action, frames, *params):
        self.stack.append(Feature(action, frames, params))

    def apply_static(self):
        pass
    def apply_dynamic(self):
        pass

    def clear(self):
        self.stack = []
        self.layer = ''

    def develop(self):
        for a in self.stack:
            Actions[a]





