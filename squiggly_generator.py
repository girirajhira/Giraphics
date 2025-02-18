# from giraphics.graphing.graph import Graph
# import numpy as np
# G = Graph(160, 160, 4,4,'poster2/squig.svg')
#
# t = np.linspace(-1, 1, 100)
#
# X = 4*t
#
# Y =-1* (t-1)*(t+1)
#
# G.plot_decorated(X, Y, colour="black", amplitude=.4, period=4)
# G.save()

from giraphics.graphing.graph import Graph
import numpy as np
G = Graph(160, 160, 4,4,'poster2/halfcirc.svg')

t = np.linspace(-1, 1, 100)  + 1

X = 3*np.cos(np.pi * t/2)

Y = 3*np.sin(np.pi * t/2)

G.plot_decorated(X, Y, colour="black", amplitude=.15, period=7)
G.save()
