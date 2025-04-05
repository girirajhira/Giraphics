from giraphics.graphing.fancygraph import FancyGraph
import numpy as np
from giraphics.utilities.colour import ColourObj, generate_cmap, Blues, Reds

width = 1000
height = 1000
xlim = 3
ylim = 3

G = FancyGraph(width,height,xlim,ylim,'surface3d_example.svg', origin=[0,0])



x = np.linspace(-2,2,120)
y = np.linspace(-2,2,120)
xm, ym = np.meshgrid(x,y)
z = np.exp(-xm**2 - ym**2)*np.sin(5*xm*ym)


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
cmap = generate_cmap([C1,C2])

R = rotation_matrix(-.8*np.pi/3, -1.1*np.pi/4)

from giraphics.utilities.utils import Timer
T = Timer()
T.start()
G.plot_surface(xm, ym, z, R = R, cmap = cmap, axes=False, box=False, strokewidth=0)
T.stop()

G.save()
