from giraphics.graphing.fancygraph import *
from giraphics.utilities.convert import convert_image
import math

''''
This script takes plots the a vector field of a function that takes (x,y) and assigns
it a vector. 

'''

# SVG setup
width = 600
height = 600
xlim = 5
ylim = 5
name = 'VectorField.svg'
G = FancyGraph(width, height, xlim, ylim, name)


# Vector Function
def V(x, y):
    if x**2 + y**2 != 0 :
        z = (x - 1j*y)*(x + 1j*y)**(-2)
    else:
        z = 0
    return [z.real, z.imag]


# Parameters
gridint = 8  # Number of vectors in the x and y directions
scale = 0.01
stroke = 'white'
arrow = True
constcolour = False
initColour = [200, 0, 200]
endColour = [200, 0, 0]
constLength = True  # Length of the wa
length_scale = .4  # Length of the arrow
arrow_scale = 1  # Size of the arrowhead

G.bg(colour="black")
G.grid(grid_int=[gridint, gridint])
G.VectorField(V, gridint=[gridint, gridint], scale=scale, stroke=stroke, arrow=arrow, constColour=constcolour,
              constLength=constLength, tail_length=length_scale, arrow_scale=arrow_scale, initColour=initColour,
              endColour=endColour)

# Save and display the plot
G.save()
G.display()

# Convert from svg to png
save_file = 'VectorField.png'
convert_image(name, save_file)
