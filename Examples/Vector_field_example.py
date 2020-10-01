from fancygraphs import *
from convert import convert_image
import math

''''
This script takes plots the a vector field of a function that takes (x,y) and assigns
it a vector. 

'''

# SVG setup
width = 1000
height = 1000
xlim = 2
ylim = 2
name = 'VectorField.svg'

# Creates the Graph Object
G = FancyGraphs(width, height, xlim, ylim, name, origin=[-xlim,-ylim])

# Vector Function
def V(x,y):
    a = 1.4
    b = 0.7
    return [x - y*x,-a*y + b*x*y]

# Parameters
gridint = 16 # Number of vectors in the x and y directions
scale = 0.01
stroke = 'white'
arrow = True
constcolour = False
initColour = [200, 0, 200]
endColour = [200, 0, 0]
constLength = True # Length of the wa
length_scale = .4 # Length of the arrow
arrow_scale = 0.5*2 # Size of the arrowhead


# Drawing the background and grid
G.bg(colour="black")
G.grid(grid_int=[gridint, gridint])
G.axes()
G.ticks()

# Drawing the vector Field
G.VectorField(V, gridint=gridint, scale=scale, stroke=stroke, arrow=arrow, constColour=constcolour,
                constLength=constLength, tail_length=length_scale, arrow_scale=arrow_scale, initColour=initColour,
                endColour=endColour)

# Save and display the graph
G.save()
G.display()

# Convert from svg to png
save_file = 'VectorField.png'
convert_image(name, save_file)
