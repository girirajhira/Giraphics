from giraphics.animate.animation import Animation
from math import cos, sin, pi
import numpy as np
from giraphics.utilities.utils import Timer

frames = 160
xlim = 3
ylim = 3
res_x = 1000
res_y = 1000
video_name = '3Danim.mp4'
A = Animation(video_name, res_x, res_y, xlim, ylim)



x = np.linspace(-2,2,40)
y = np.linspace(-2,2,40)
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

T = Timer()
T.start()
for i in range(0, frames):
    t1 = np.pi / 10 * (i/frames)
    t2 = -np.pi / 2 * (i/frames)
    R = rotation_matrix(t1, t2)
    A.plate.plot_surface(xm, ym, z, R = R)
    A.plate.press()

A.develop(cleanup=True)

T.stop()