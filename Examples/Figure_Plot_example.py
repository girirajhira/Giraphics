from giraphics.graphing.figure import *


def func(x):
    return math.exp(x-math.sin(x))

f = Figure(600, 450, 15, 10, "fig.svg", origin=[-5,-5])
f.grid()
f.graph(func, colour="red")
# f.grid2(colour="blue")
f.ticks(markers=True)
f.xlabel(label="f(x)")
f.ylabel()
f.title("Title")
f.save()
f.display()