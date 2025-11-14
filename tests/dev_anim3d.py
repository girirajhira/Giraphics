from giraphics.animate.animation import Animation
from giraphics.utilities.utils import Timer
from math import cos, sin, pi
import numpy as np
from giraphics.utilities.colour import ColourObj, generate_cmap, Blues, Reds


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




frames = 100
xlim = 5
ylim = 5
res_x = 1400
res_y = 1400
video_name = 'dev_anim3d.mp4'
A = Animation(video_name, res_x, res_y, xlim, ylim)


t = np.linspace(0, 1, frames)

x = np.linspace(-5,5,100)

theta = .8
# Rotation around Z-axis
phi = -1.1 # Rotation around X-axis


x = np.linspace(-2,2,50)
y = np.linspace(-2,2,50)
xm, ym = np.meshgrid(x,y)
z = np.exp(-xm**2 - ym**2)*np.sin(5*xm*ym)

C1 = ColourObj(Blues.royal)
C2 = ColourObj(Reds.salmon)
C1 = ColourObj('#0000FF')
C2 = ColourObj('#FF0000')
cmap = generate_cmap([C1,C2])

T = Timer()
T.start()
for i in range(0, frames):
    t = (i + 1)/frames
    A.plate.bg(colour="black")
    # A.plate.plot_decorated((1-t[i])*x, t[i]*x, amplitude=.4)
    # A.plate.plot_coil2(x, x, theta = 2*np.pi*i/frames)
    R = rotation_matrix(theta*t/2, phi*t)
    # A.plate.axes3d(R, colour="yellow")
    # A.plate.background3d([-1,1], [-1,1], [-1, 1], R=R, colour="green")
    A.plate.plot_surface(xm, ym, z, R = R, cmap = cmap, axes=True, box=True,
                   strokewidth=.08)
    A.plate.press()
A.develop(cleanup=False)
T.stop()