from giraphics.graphing.fancygraphs import *
from math import sin, cos
from random import gauss

g = FancyGraphs(1440, 1440, 10, 10, "ss.svg")
g.bg(colour="black")
colours = ['']
def path(t, mu=1):
    return [gauss(5,mu)*cos(i), gauss(5,mu)*sin(i)]

for i in range(0,500):
    p = path(i)
    g.draw_circle(p[0], p[1], gauss(0.2,0.1),fill="red", strokewidth=0)

#spiral


for j in range(0, 12):
    SX = [i*0.02*sin(0.02*i+j) for i in range(0,600)]
    SY = [i*0.02*cos(0.02*i+j) for i in range(0,600)]
    g.plot_points(SX, SY)
g.save()
g.display()