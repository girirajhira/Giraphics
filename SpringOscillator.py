from giraphics.graphing.graph import *
from giraphics.animate.animation import *
import numpy as np

width = 400
height = 100
xlim = 4
ylim = 1

t = np.linspace(0, 1, 600)

spring_start = 0
spring_end = 2
SX = spring_start + (spring_end - spring_start) * t
SY = t * 0
sw_x, sw_y = spring_end, 0
sw_size = 1

G = Graph(width, height, xlim, ylim, 'SpringOscillator.svg', origin=[-xlim + 1, 0])
G.bg(colour="white")
# G.axes(colour="blue")
G.draw_rect(-1, 0, 2, 2, fill="grey", strokewidth=0)
G.draw_rect(2, -1, 10, 1, fill="grey", strokewidth=0)
G.plot_decorated(SX, SY, colour="black", strokewidth=.5, amplitude=.5)
G.draw_rect(sw_x + sw_size / 2, sw_y, sw_size, sw_size, fill="teal", strokewidth=.5)
G.draw_circle(0, 0, .01, fill="black")
G.draw_circle(spring_end, 0, .01, fill="black")

G.save(export='png')
