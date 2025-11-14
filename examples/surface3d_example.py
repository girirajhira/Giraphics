from giraphics.graphing.fancygraph import FancyGraph
import numpy as np
from giraphics.utilities.colour import ColourObj, generate_cmap, Blues, Reds
from giraphics.utilities.utils import  Rz, Rx

width = 500
height = 500
xlim = 2.5
ylim = 2.5

G = FancyGraph(width,height,xlim,ylim,'surface3d_example.svg', origin=[0,0])

x = np.linspace(-2,2,50)
y = np.linspace(-2,2,50)
xm, ym = np.meshgrid(x,y)
z = np.exp(-xm**2 - ym**2)*np.sin(5*xm*ym)


# def rotation_matrix(theta, phi):
    # return Rx(theta) @ Rz(phi) # First rotate around Z, then around X
def rotation_matrix(theta, phi):
    """Create a 3D rotation matrix from angles theta (Z-axis) and phi (X-axis)."""
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi), np.cos(phi)]
    ])

    return Rx @ Rz  # First rotate around Z, then around X


C1 = ColourObj(Blues.royal)
C2 = ColourObj(Reds.salmon)
C1 = ColourObj('#0000FF')
C2 = ColourObj('#FF0000')
cmap = generate_cmap([C1,C2])

theta = .1
# Rotation around Z-axis
phi = -1.1 # Rotation around X-axis
R = rotation_matrix(theta, phi)
# Create plot
G.bg(colour='#555555')
G.background3d([-2,2], [-2,2], [0, 1], colour='green', R = R)
# G.plot_surface(xm, ym, z, R = R, cmap = cmap, axes=False, box=False,
#                strokewidth=.08)

G.save()
