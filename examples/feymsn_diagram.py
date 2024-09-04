from giraphics.graphing.graph import Graph
import numpy as np
from latex2mathml.converter import convert


width = 1000
height = 1000
xlim = 5
ylim = 5

G = Graph(width,height,xlim,ylim,'feynman_diagram.svg', origin=[0,0])
t = np.linspace(0,np.pi,200)
xarc1, yarc1 = 2*np.cos(t) - 1,  2*np.sin(t)
xarc2, yarc2 = 2*np.cos(t) + 1 ,-2*np.sin(t)

G.bg(colour='teal') #
G.plot_decorated(xarc1,yarc1, amplitude=.1,period=10,colour='white', strokewidth=1)
G.plot_decorated(xarc2,yarc2, amplitude=.1,period=10,colour='white', strokewidth=1)
G.draw_line(-4,0,4,0, colour='white', strokewidth=1)
# G.draw_arrowhead(-1.5-2,0, ang=0, colour='white',)
G.draw_arrowhead(-1.5,  0, ang=0, colour='white',scale=.7)
G.draw_arrowhead(-1.5+2,0, ang=0, colour='white',scale=.7)
G.draw_arrowhead(-1.5+4,0, ang=0, colour='white',scale=.7)
# G.axes(colour='black')
G.add_latex(r'$\omega_1$',-1, 2.6,colour='white', scale=.8)
G.add_latex(r'$\omega_2$', 1, -2.7,colour='white', scale=.8)

G.save()
# G.display()
