from giraphics.graphing.graph import Graph
import numpy as np
from latex2mathml.converter import convert


width = 800
height = 800
xlim = 5
ylim = 5

G = Graph(width,height,xlim,ylim,'feynman_diagram.svg', origin=[0,0])
G.bg(colour='teal')



G.save()
# G.display()
