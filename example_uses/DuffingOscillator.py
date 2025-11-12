from giraphics.graphing.fancygraph import FancyGraph
import numpy as np

width = 600
height = 600
xlim = 3
ylim = 3

def func(x, y):
    return [y, -x + np.sin(y)]

G = FancyGraph(width, height, xlim, ylim, 'duffing_oscilator.svg', origin=[0, 0])
t = np.linspace(-xlim, xlim, 600)
G.bg(colour='black')  # Plots black background
G.grid2(strokewidth=.2, colour="white")
G.VectorFieldFunction(func, tail_length=.4, constLength=True)

G.save()
