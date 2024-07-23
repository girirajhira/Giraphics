from giraphics.graphing.graph import Graph
import numpy as np

width = 1000
height = 1000
xlim = 5
ylim = 2

G = Graph(width,height,xlim,ylim,'test_graph.svg', origin=[-2,-1])

t = np.linspace(-xlim,xlim+5 ,300)

G.bg(colour='black') # Plots black blach
G.axes()
G.ticks2(markers=True)
# G.ticks(markers=True)
G.grid2()
G.plot_points(t, 2*np.sin(t)/(1 + t*t), colour='red', strokewidth=2)
G.area(t, 2*np.sin(t)/(1 + t*t), fill_opacity=.2, fill_colour='red')
G.save()
# G.display()
