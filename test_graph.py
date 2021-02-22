from giraphics.graphing.graph import Graph
import numpy as np

G = Graph(1000,1000,10,10,'svg.svg')

G.bg()

t = np.linspace(-10,10,300)

G.plot_points(t, t * t)
G.save()
G.display()
