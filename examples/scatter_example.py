from giraphics.graphing.graph import Graph
import numpy as np

width = 600
height = 600
xlim = 4
ylim = 2

G = Graph(width,height,xlim,ylim,'scatter_plot_example.svg', origin=[0,0])

t = np.linspace(-4,4, 30)
G.bg(colour='white') # Plots black blach
G.axes(colour='black')
G.ticks2(markers=True, colour='black')
# G.ticks(markers=True)
G.grid2(colour='black')
G.scatter(t,  np.sin(t), s=5)
G.scatter(t, 1.4*np.sin(t+np.pi/2), s =5, marker='s', colour='white',markeredgecolour='crimson')
G.scatter(t, np.sin(t+np.pi), s = 5, marker='^', colour='white',markeredgecolour='DodgerBlue')

G.save()
# G.display()
