from giraphics.graphing.fancygraph import FancyGraph
import numpy as np

width = 1000
height = 1000
xlim = 5
ylim = 5

G = FancyGraph(width,height,xlim,ylim,'densityplot_example.svg', origin=[-2,-1])

t = np.linspace(-xlim,xlim+5 ,600)

x = np.linspace(-5,5, 100)
y = np.linspace(-5,5, 100)

xm, ym = np.meshgrid(x,y)
G.bg(colour='black') # Plots black blach

f = np.exp(-(xm**2+ym**2)/10)*np.sin(xm*ym)


G.DenistyPlot(f)
G.save()
