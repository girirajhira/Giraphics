from giraphics.animate.animation import Animation
from giraphics.utilities.utils import Timer
from math import cos, sin, pi
import numpy as np

frames = 200
xlim = 5
ylim = 5
res_x = 400
res_y = 400
video_name = 'dev_anim.mp4'
A = Animation(video_name, res_x, res_y, xlim, ylim)


t = np.linspace(0, 1, frames)

x = np.linspace(-5,5,100)

theta = .1
# Rotation around Z-axis
phi = -1.1 # Rotation around X-axis


T = Timer()
T.start()
for i in range(0, frames):
    A.plate.bg(colour="black")
    # A.plate.plot_decorated((1-t[i])*x, t[i]*x, amplitude=.4)
    A.plate.plot_coil2(x, x, theta = 2*np.pi*i/frames)
    A.plate.press()
A.develop(cleanup=True)
T.stop()