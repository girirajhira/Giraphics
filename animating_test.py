from giraphics.animate.animation import Animation
from math import cos, sin, pi
import numpy as np

frames = 400
xlim = 5
ylim = 5
res_x = 1000
res_y = 1000
video_name = 'combination.mp4'
A = Animation(video_name, res_x, res_y, xlim, ylim)


def f(t):
    return (1.5 / (0.3 * t + 0.7)) * (np.cos(2.7 * t)) ** 2


def r(t):
    return 3 / (t + 1)


t = np.linspace(0, 10, frames)
x1 = r(t) * np.cos(t)
y1 = r(t) * np.sin(t)

x2 = r(t) * np.cos(t + pi)
y2 = r(t) * np.sin(t + pi)

from giraphics.utilities.utils import Timer

T = Timer()
T.start()
for i in range(0, frames):
    A.plate.bg(colour="black")
    A.plate.add_latex(r'\int f(x)dx', 0,0, colour='white')
    A.plate.plot_points(x1[:i], y1[:i], colour='pink', style='5,5')
    A.plate.plot_points(x2[:i], y2[:i], colour='pink', style='5,5')
    A.plate.draw_circle(x1[i], y1[i], 0.3, fill="red")
    A.plate.draw_circle(x2[i], y2[i], 0.3, fill="red")
    A.plate.press()
A.develop(cleanup=True)
T.stop()