from giraphics.graphing.fancygraph import FancyGraph
import numpy as np
from scipy.integrate import odeint

width = 600
height = 600
xlim = 5
ylim = 5

nx = 26
ny = 26

x = np.linspace(-xlim, xlim,nx)*1.1
y = np.linspace(-ylim, ylim,ny)*1.1

X, Y = np.meshgrid(x, y)

import numpy as np

def dH(x, y):
    """
    Computes the Hamiltonian vector field components derived from H(x, y) = sin(x) * cos(y) + (x^2 - y^2) / 2.

    Returns:
    Vx (float or array) - x-component of the vector field
    Vy (float or array) - y-component of the vector field
    """
    Vx = np.cos(x) * np.sin(y) - y  # ∂H/∂y
    Vy = - (np.sin(x) * np.cos(y) + x)  # -∂H/∂x
    return Vx, Vy

Vx, Vy = dH(X, Y)

# Trajectories

def F(x, t):
    dxH, dyH =  dH(x[0],x[1])
    return [dxH, dyH]

# Time array for integration
t = np.linspace(0, 25, 500)  # 500 time steps

# Initial conditions for different particles
initial_conditions = [
    (1.0/4, -1.0/3),
    (-3.0, -3.0),
    (3.4, 2.8),
    # (-3.4, -.7),

]

# Plot trajectories
sols = []
for x0, y0 in initial_conditions:
    sol = odeint(F, [x0, y0], t)
    sols.append(sol)



G = FancyGraph(width, height, xlim, ylim, 'vectorfield_example.svg', origin=[0, 0])
t = np.linspace(-xlim, xlim, 600)
G.bg(colour='black')  # Plots black background
# G.axes(colour='white',strokewidth=.5)
G.grid2(strokewidth=.2, colour="white")
G.VectorField(X,Y,Vx,Vy, tail_length=1, constLength=True)
# Trajs
for sol in sols:
    G.plot(sol[:, 0], sol[:, 1], colour='white', strokewidth=.4)
for x0, y0 in initial_conditions:
    G.draw_circle(x0,y0, r=.1, fill='white', strokewidth=0)

G.save()

