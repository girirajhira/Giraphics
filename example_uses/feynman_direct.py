from giraphics.graphing.graph import Graph
import numpy as np
from latex2mathml.converter import convert


# Set parameters
width = 800
height = 800
xlim = 5
ylim = 5

G = Graph(width,height,xlim,ylim,'feynman_diagram_direct.svg', origin=[0,-1])

# Setting up photon propagators
t1 = np.linspace(0,3.24*np.pi/8,200)
t2 = np.linspace(np.pi-3.24*np.pi/8, np.pi,200)
xarc1, yarc1 = 2*np.cos(t1),  2*np.sin(t1)
xarc2, yarc2 = 2*np.cos(t2),  2*np.sin(t2)


# Background
G.bg(colour='PaleVioletRed')

# Photon lines
G.plot_decorated(xarc1,yarc1, amplitude=.1,period=5,colour='white', strokewidth=1)
G.plot_decorated(xarc2,yarc2, amplitude=.1,period=5,colour='white', strokewidth=1)

# Fermion loop
G.draw_circle(0, 2, .6, colour='white', strokewidth=1)
G.draw_arrowhead(-.2, 2.6, ang=np.pi, colour='white',scale=.7)
G.draw_arrowhead(.2, 1.4, ang=0, colour='white',scale=.7)

#External line
G.draw_line(-4,0,4,0, colour='white', strokewidth=1)
G.draw_arrowhead(-1.5-1,  0, ang=0, colour='white', scale=.7)
G.draw_arrowhead(-1.5+2,0, ang=0, colour='white',scale=.7)
G.draw_arrowhead(-1.5+5,0, ang=0, colour='white',scale=.7)

# Latex labels
G.add_latex(r'$\omega$',-2, 1.5,colour='white', scale=.8)
G.add_latex(r'$\omega$', 2.15, 1.5,colour='white', scale=.8)

G.save()
# G.display()
