from giraphics.graphing.fancygraph import FancyGraph
import numpy as np

width = 1000
height = 1000
xlim = 3
ylim = 3

G = FancyGraph(width,height,xlim,ylim,'inset_example.svg', origin=[.8,-1.7])
t = np.linspace(-xlim-2,xlim+5 ,10000)


def sine_square(x):
    total = 0
    L = 4
    for n in range(1, 670,2):
        total += np.sin(n*np.pi*x/L)/n
    return .8 + total


G.bg(colour='PaleGreen') # Plots black blach
G.axes(colour='black', strokewidth=.5)
G.ticks2(colour= 'black', strokewidth=.5)
# G.ticks(markers=True)
G.grid2(strokewidth=.75, colour='black')
G.plot(t,sine_square(t), colour='Red', strokewidth=.4)
#INSET
G.add_inset(3, 3, .25, .25,
            position=[-2, 3] ,magnifier_pos=[0, 1.65],
            magnifier=True, magnifier_dims=[.5,.5],
            bcol="black", bstroke=.1, origin=[0, -1.65])
G.insets[0].bg(colour ='PaleGreen')
G.insets[0].grid()
G.insets[0].axes(colour='black', strokewidth=1)
G.insets[0].plot(t, sine_square(t), colour='Red', strokewidth=1,)
G.save()
# G.display()
