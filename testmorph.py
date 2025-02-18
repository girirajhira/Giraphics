from giraphics.graphing.graph import *
from giraphics.animate.animation import *
import numpy as np

width = 400
height = 400
xlim = np.pi
ylim = np.pi

t = np.linspace(-np.pi, np.pi, 600)

G = Graph(width, height, xlim, ylim, 'testKeynoteMorph1.svg')
G.bg(colour="white")
G.plot(t, np.sin(3 * t))

G.save()


G = Graph(width, height, xlim, ylim, 'testKeynoteMorph2.svg')
G.bg(colour="white")
G.plot(t, 3 * np.cos(t))

G.save()
