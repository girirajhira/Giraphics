from giraphics.graphing.graph import Graph


def func(x):
    return (x-3)*(x+2)*x*0.2

g = Graph(800,600,8,6, 'example1.svg')

g.bg()
g.grid()
g.axes()
g.graph(func)

g.save()
g.display()