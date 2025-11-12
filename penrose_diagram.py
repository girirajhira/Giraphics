from giraphics.graphing.graph import Graph
import numpy as np
from latex2mathml.converter import convert


# Set parameters
width = 800
height = 800
xlim = 5
ylim = 5

G = Graph(width,height,xlim,ylim,'feynman_diagram_direct.svg', origin=[0,0])


# Background
G.bg(colour='teal')

# Frame
ti, tf = -4, 4
xi, xf = -4, 4
X0 = [(xi+xf)/2, xi, (xi+xf)/2, xf, (xi+xf)/2]
T0 = [ti, (ti+tf)/2, tf, (ti+tf)/2, ti]
G.plot(X0, T0, colour="white")


# Fermion loop

#External line
# G.draw_line(-4,0,4,0, colour='white', strokewidth=1)
# G.draw_arrowhead(-1.5-1,  0, ang=0, colour='white', scale=.7)
# G.draw_arrowhead(-1.5+2,0, ang=0, colour='white',scale=.7)


# Latex labels
G.add_latex(r'$\omega$',-2, 1.5,colour='white', scale=.8)
G.add_latex(r'$\omega$', 2.15, 1.5,colour='white', scale=.8)

G.save()
# G.display()
