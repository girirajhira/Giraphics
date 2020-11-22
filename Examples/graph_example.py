from graph import *

# We first create a Graph

width = 800
height = 800
xlim = 2
ylim = 2
name = "example_graph.svg"

G = Graph(width, height, xlim, ylim, name, origin=[-1, -1])

# Setting up the graph
G.bg(colour="black")
G.grid(opac=.2)
G.axes(colour="white")
G.ticks()

def f(x):
    return .3*(.8*x-2)**3 + 1.5

print(f(0.7))
G.area(f, [0.7, 1.8], opac=0.7)
G.graph(f,colour="cyan")
G.draw_line(0.7, 0, 0.7, f(0.7), colour="white")
G.draw_line(1.8, 0, 1.8,  f(1.8), colour="white")
G.draw_line(.7, f(0.7), 1.8,  f(0.7), colour="white", dotted=True)
G.point(0.7, f(0.7), s=1)
G.point(1.8, f(1.8), s=1)
G.save()
G.display()