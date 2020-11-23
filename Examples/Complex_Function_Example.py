from giraphics.graphing.fancygraphs import *

'''
Takes a cartesian grid and transforms it according to the given function.
The function takes two variables (x, y) and return a complex number.

'''
# SVG parameters
width = 1000
height = 1000
xlim = 10
ylim = 10
name = 'VectorField.svg'
origin = [0, 0]
# Creating Graph Object
G = FancyGraphs(width, height, xlim, ylim, name, origin=origin)


# Complex Function
def func(x, y):
    return (x + 1j*y) *(y + 1j*x)


strokewidth = 1
colour = "yellow"
axes = True
N = 60
epsfuncorder = 1

# Adding the background and grid (which is untransformed)
G.bg()
G.grid()

# Plotting the transformed grid
G.ComplexPlot(func, colour=colour, N=N, epsfuncorder=epsfuncorder)

# Save and displaying the grid
G.save()
G.display()
