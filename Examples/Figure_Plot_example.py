from giraphics.graphing.figure import *


def func(x):
    return math.exp(x - math.sin(x))

f = Figure(600, 450, 15, 10, "figure_example.svg", origin=[0, 0])
f.plot(func, colour="red", strokewidth=3)
f.plot_points(np.linspace(-15, 15, 100), np.linspace(-15, 15, 100) ** 2, colour='blue', strokewidth=3)
f.grid()
# f.grid2(colour="blue")
f.ticks(markers=True)
# f.xlabel(label="$f(x)$", use_latex=True)
# f.ylabel(use_latex=True)
f.inner_graph.axes(colour='black')
f.xlabel(label='$x$', use_latex=True)
f.ylabel(label='$y$', use_latex=True)
f.add_latex('$f(x)$', 0, 0, scale=3, rotation=0)
# f.title("Title", use_latex=True)
f.save()
f.display()
