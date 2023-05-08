from giraphics.graphing.fancygraph import *
from giraphics.utilities.convert import convert_image
# Optional
from scipy.integrate import odeint


''''
This example plots a vectorfield for the function of the form f:(x,y) -> [u, v].
'''

# SVG setup
width = 900
height = 600
xlim = 1.875
ylim = 1.25
name = 'VectorField.svg'

# Creates the Graph Object
G = FancyGraph(width, height, xlim, ylim, name, origin=[-0, 0])

# Vector Function
def V(x,y):
    a = 1.4
    b = 0.7
    return [y*(1-y*y),-x - y*y]



### Optional - particular solutions
def wrapper_V(x,t):
    return V(x[0], x[1])


X0 = np.array([[-.4,.3], [1.4,2], [-1, -.5], [-1,-.8]])
sol = np.zeros
tspan = np.linspace(0,15,200)
sol = np.zeros((len(X0), len(tspan),2))

for i in range(len(X0)):
    sol[i,:,:] = (odeint(wrapper_V, X0[i,:], tspan))
###



# Parameters
gridint = [15,10] # Number of vectors in the x and y directions
scale = 0.01
stroke = 'white'
arrow = True
constColour = False # Colours the arrows based on the lengthf of f(x,y)
initColour = [0, 230, 100] # Colour of the smallest arrow  (RGB)
endColour = [0, 100, 230] # Colour of the largest arrow (RGB)
constLength = True # Length of the arrows are constant
length_scale = .4 # Length of the arrow
arrow_scale = 1# Size of the arrowhead

# Drawing the background and grid
G.bg(colour="black")
# G.grid(grid_int=gridint)
G.axes(colour='white',strokewidth=2)
G.ticks(colour='white')

# Drawing the vector Field
G.VectorField(V, gridint=gridint, scale=scale, stroke=stroke, arrow=arrow, constColour=constColour,
                constLength=constLength, tail_length=length_scale, arrow_scale=arrow_scale, initColour=initColour,
                endColour=endColour)


# Optional - plotting particular solutions
for i in range(len(X0)):
    G.plot_points(sol[i][:,0], sol[i][:,1], colour='white')

# Save and display the plot
G.save()
G.display()

# Convert from svg to png
save_file = 'VectorField.png'
convert_image(name, save_file)
