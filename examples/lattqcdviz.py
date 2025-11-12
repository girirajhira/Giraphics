from giraphics.graphing.fancygraph import FancyGraph
import numpy as np
from giraphics.utilities.colour import ColourObj, generate_cmap, Blues, Reds
from giraphics.utilities.utils import  Rz, Rx

width = 1200
height = 800
xlim = 12
ylim = 8

G = FancyGraph(width,height,xlim,ylim,'latt_example2.svg', origin=[0,-2.5])

x = np.linspace(-2,2,23)
y = np.linspace(-2,2,23)
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

theta = .65 # Rotation around Z-axis
phi = -1.9
# Rotation around X-axis
R = rotation_matrix(theta, phi)

G.bg(colour='#555555')
G.background3d([0,10], [0,10], [0,10],colour='white', R = R, opacity=.6,
               strokecolor='black', strokewidth=.2)
# G.add
# G.plot_surface(xm, ym, z, R = R, cmap = cmap, axes=False, box=False,
#                strokewidth=.08, colorbar=True)
# G.draw_circle(0,0,.2,'green')
# G.add_
num_plaq = 1000
d = np.array([0,1,2])
cm = cmap(np.linspace(0,1,num_plaq))[0]
for i in range(num_plaq):
    p = np.random.randint(size=(3,), high=10, low=0)
    mu = np.random.randint(size=(1,), high=2,low=0)[0]
    nu = np.random.randint(size=(1,), high=3,low=mu+1)[0]
    print(p, mu, nu)
    rect_verts = np.array([
        p,
        p + (d==mu),
        p + (d==mu) + (d==nu),
        p +(d==nu),
        p
    ])
    rot_verts = rect_verts @ R.T
    G.area(rot_verts[:,0], rot_verts[:,1],fill_colour=cm[i], colour='black', fill_opacity=.2, opac=1, strokewidth=.1)

G.save()
