from giraphics.graphing.fancygraph import FancyGraph
import numpy as np

width = 600
height = 600
xlim = 3
ylim = 3


G = FancyGraph(width, height, xlim, ylim, 'LinearTransformExample.svg', origin=[0, 0])
t = np.linspace(-xlim, xlim, 600)
G.bg(colour='black')  # Plots black background
# G.grid2(strokewidth=.2, colour="white")

def func(x,y):
    z = (x + 1j*y)
    r2 = x**2 + y**2
    return z**(1/2)

Nx, Ny = 20,20

# G.ComplexPlot2(lambda x, y: (x + 1j*y), Nx = Nx, Ny = Ny, colour='white')
G.ComplexPlot2(func, Nx = Nx, Ny = Ny, colour='yellow')

G.save()
