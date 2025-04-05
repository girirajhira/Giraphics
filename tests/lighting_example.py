from giraphics.graphing.graph import Graph
import numpy as np
from giraphics.svg.filters import *
width = 1000
height = 1000
xlim = 5
ylim = 2

G = Graph(width,height,xlim,ylim,'test_light.svg', origin=[-2,-1])

t = np.linspace(-xlim,xlim+5 ,300)

G.bg(colour='red') # Plots black blach
G.axes()
# G.ticks2(markers=True)
# G.ticks(markers=True)
# G.grid2()
G.svg.canvas += lighting('f1', [0,0,200], )
G.draw_circle(1,1,2, fill='black', style="filter:url(#f1)", strokewidth=0)

G.save()
G.display()
