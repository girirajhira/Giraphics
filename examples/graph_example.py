from giraphics.graphing.graph import Graph
import numpy as np

width = 1000
height = 1000
xlim = 5
ylim = 2

G = Graph(width,height,xlim,ylim,'graph_example.svg', origin=[-2,-1])

t = np.linspace(-xlim,xlim+5 ,600)

ss = np.linspace(-5,5, 30)
G.bg(colour='black') # Plots black blach
G.axes()
G.ticks2(markers=True)
# G.ticks(markers=True)
G.grid2()
# G.scatter(ss, np.sin(ss))
# G.plot_decorated(t, 2*np.sin(t)/(1 + t*t),period=30,amplitude=.1,colour='red', strokewidth=1.4)
# G.plot_decorated(t, np.sin(t), amplitude=.1,period=30,colour='blue')
# G.plot_decorated(t, .1*t*t, amplitude=.1,period=10,colour='green')
# G.plot_coil(t, 0*t*t, period=40,amplitude=.1,colour='teal', strokewidth=.8)
G.plot_coil2(t, t, period=40,amplitude=.1, colour='green', strokewidth=.8)
G.plot(t, t, colour='blue', strokewidth=.8)

# G.plot_coil(t, .1*t*t, period=30,amplitude=.1,colour='purple', strokewidth=.8)
# G.add_latex('1', 0,0)
# G.area(t, 2*np.sin(t)/(1 + t*t), fill_opacity=.2, fill_colour='red')
G.save()
# G.display()
