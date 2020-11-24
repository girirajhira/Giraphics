from giraphics.graphing.graph import *
from giraphics.utilities.convert import *
import numpy as np

N = 9

def xfunc(x):
    total = 0
    for i in range(1, N):
        total += 1/(2*i)*np.sin(i*x)
    return total

def yfunc(x):
    total = 0
    for i in range(1, N):
        total += 1/(2*i)*np.cos(i*x)
    return total

frames = 300
create_directory("ftp")
create_directory("ftprast")

t = np.arange(0, 7, .01)
X = xfunc(t)
Y = yfunc(t)
ds = round(len(t)/frames)

for i in range(frames):
    f = Graph(800, 800, 5, 5, "ftp/g"+namer(i)+".svg", origin=[-0, -0])
    f.bg()
    # f.graph(func)
    # f.math_text("sin(x)", 3.14 ,1)
    f.save()

create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# Creating the final video
create_mpeg('t6.mp4', 'p', frames, dir=os.getcwd() + "/ftprast")
#'''