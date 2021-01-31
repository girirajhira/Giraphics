from fancygraphs import *
from random import uniform
g = FancyGraphs(1000, 1000, 10, 10, 'f1.py')

g.bg(colour="black")
for i in range(0,10):
    g.draw_circle(uniform(-10,10), uniform(-10,10), uniform(0,2), fill="white")

g.save()