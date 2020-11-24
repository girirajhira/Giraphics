from giraphics.graphing.graph import *
from giraphics.utilities.convert import *
from math import sin, pi


timeSteps = 360

create_directory("sc")
create_directory("scrast")


for j in range(0, timeSteps):
    G = Graph(1800, 1800, 10, 10, "sc/g"+namer(j)+".svg")
    G.bg("black")
    for i in range(0,12):
        t = j/(pi)
        x = G.tranx(0)
        y = G.trany(6-i/2 + 3*sin((i/30)*t**0.5) - 2.5)
        G.svg.draw_ellipse(x, y, rx=G.tranx(i**2/3)/4, ry = G.trany(1.5)/3, strokewidth=2, stroke="white", fill="none")
    G.save()


create_raster_batch("sc", 'g', 'p', 'scrast', timeSteps)
create_mpeg('sc5.mp4', 'p', timeSteps, dir=os.getcwd() + "/scrast")
#'''