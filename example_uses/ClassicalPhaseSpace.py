from giraphics.graphing.graph import *
from giraphics.animate.animation import *
from scipy.integrate import odeint
import numpy as np

omega = 2.0  # Angular frequency, for example
beta = .25
# Define the system of ODEs
def harmonic_oscillator(state, t, omega):
    x, v = state  # Unpack the state vector
    dxdt = v
    dvdt = -omega ** 2 * x - beta*v
    return [dxdt, dvdt]


# Initial conditions
x0 = 2.0  # Initial displacement
v0 = 0.0  # Initial velocity
initial_state = [x0, v0]

# Time points where we want the solution
t = np.linspace(0, 26, 2400)
trail = 85
# Solve the ODEs
solution = odeint(harmonic_oscillator, initial_state, t, args=(omega,))

# Extract the displacement and velocity
x = solution[:, 0]
p = solution[:, 1] / omega

s = np.linspace(0, 1, 200)


scaler = 5
width = 100 * scaler
height = 100 * scaler
xlim = 4
ylim = 4
A2 = Animation('SpringOPS.gif', width=width, height=height, xlim=xlim, ylim=ylim, origin=[-xlim + 1, 0])

for i in range(0,len(t),4):
    A2.plate.bg(colour="white")
    ##
    spring_start = -3
    spring_end = x[i] - .5
    SX = spring_start + (spring_end - spring_start) * s
    SY = s * 0 - 3
    sw_x, sw_y = spring_end, 0
    sw_size = 1


    # Background,grid
    A2.plate.bg(colour="white")
    A2.plate.grid(colour="grey", strokewidth=.15)

    #Axes
    A2.plate.axes(colour="black")
    A2.plate.add_latex('$p$', .25, 3.7, scale=.6)
    A2.plate.add_latex('$x$', 3.7, .25, scale=.6)

    #Spring
    A2.plate.draw_rect(-4, -3, 2, 2, fill="grey", strokewidth=0)
    A2.plate.plot_decorated(SX, SY, colour="black", strokewidth=.5, amplitude=.5)

    # Mass
    A2.plate.draw_rect(sw_x+sw_size/2, sw_y-3, sw_size, sw_size, fill="teal", strokewidth=.5)

    # Spring Fasteners
    A2.plate.draw_circle(-3, -3, .01, fill="black")
    A2.plate.draw_circle(spring_end, -3, .01, fill="black")
    A2.plate.plot_trail(x[:i + 1], p[:i + 1], trail=trail, colour="#C03047")

    # Indicator Line
    A2.plate.draw_line(x[i], -3, x[i], p[i], colour='#C03047', opacity=.5, style='dotted', strokewidth=1)

    A2.plate.press()

A2.develop()
