from giraphics.graphing.figure import Figure
import numpy as np

f = Figure(600, 450, 5, 5, "fg_example.svg", origin=[-5,0])
f.bg(colour="white")
x = np.linspace(0, 10, 300)
f.plot_points(x,x**2, colour='blue',strokewidth=.5)
f.plot_points(x,np.sin(x), colour='red',strokewidth=.5)

# f.grid()
# f.grid2(colour="blue")
# f.ticks2(markers=True)
# f.xlabel(label="$f(x)$", use_latex=True)
# f.ylabel(use_latex=True)
# f.inner_graph.axes(colour='black')
# f.xlabel(label ='x',fontsize=10, scale=2)
# f.ylabel(label ='y',fontsize=10, scale=2)
# f.add_latex('$f(x)$', 2.5, 2.5, scale=.2, rotation=0)
# f.grid()
f.ticks(markers=True)
# f.title("Title", use_latex=True)
f.save()
f.display()
