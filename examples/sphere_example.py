from giraphics.graphing.fancygraph import FancyGraph
import numpy as np
from giraphics.utilities.colour import ColourObj, generate_cmap, Blues, Reds
from giraphics.utilities.utils import  Rz, Rx

width = 1000
height = 1000
xlim = 2.5
ylim = 2.5

G = FancyGraph(width,height,xlim,ylim,'sphere_example.svg', origin=[0,0])


rr = 1

THETA  = np.linspace(0,2*np.pi,60)
PHI = np.linspace(0,np.pi,40)

TM, PM = np.meshgrid(THETA,PHI)

X = rr*np.sin(TM)*np.cos(PM)
Y = rr*np.sin(TM)*np.sin(PM)
Z = rr*np.cos(TM)

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

theta = .3 # Rotation around Z-axis
phi = -1.3  # Rotation around X-axis
R = rotation_matrix(theta, phi)

G.bg(colour='#555555')
G.plot_surface(X, Y, Z, R = R, cmap = cmap, axes=False, box=False,
               strokewidth=.1, colorbar=True)

G.save()
