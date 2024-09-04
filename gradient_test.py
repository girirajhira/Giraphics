from giraphics.graphing.graph import Graph
import numpy as np
from giraphics.svg.filters import *
from giraphics.svg.css_util import *
from giraphics.svg.definitions import *

width = 1000
height = 1000
xlim = 5
ylim = 2

G = Graph(width,height,xlim,ylim,'test_gradient.svg', origin=[-2,-1])

t = np.linspace(-xlim,xlim+5 ,300)

G.bg(colour='url(#rg1)') # Plots black blach
G.axes()
# G.ticks2(markers=True)
# G.ticks(markers=True)
# G.grid2()
G.svg.canvas += linear_gradient('g1', start_color="yellow", start_opacity = 1,
                                stop_color="black", stop_opacity = 1,start_offset=3, stop_offset=100,
                                dir = [[0,100],[100,0]])
G.svg.canvas += linear_gradient('g2', start_color="black", start_opacity = 1,
                                stop_color="blue", stop_opacity = 1,start_offset=3, stop_offset=100,
                                dir = [[0,100],[0,0]])
G.svg.canvas += radial_gradient('rg1', start_color="red", start_opacity = 1,stop_color="purple", stop_opacity = 1,
                    cx=1,cy=50,r = 50, fx = 50, fy=50, start_offset=0, stop_offset = 100)


G.plot(np.sin,colour="url(#g2)")

G.draw_circle(1,1,2, fill="url(#rg1)", strokewidth=0)
G.draw_rect(4,0, 3, 1, fill="url(#g1)", strokewidth=0)
G.save()
# G.display()
