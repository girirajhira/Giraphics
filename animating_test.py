from giraphics.animate.animation import Animation
from math import cos, sin, pi

frames = 60
xlim = 5
ylim = 5
res_x = 1000
res_y = 1000
video_name = 'combinatio.mp4'
A = Animation(video_name, frames, res_x, res_y, xlim, ylim)

def f(t):
    return ((1.5)/(0.3*t+0.7))*(cos(2.7*t))**2
def r(t):
    return 3/(t+1)


for i in range(0, frames):
    t = 12 * i / frames
    A.plate.bg(colour="black")
    A.plate.draw_circle(r(t)*cos(t), r(t)*sin(t), 0.3, fill="red")
    A.plate.draw_circle(r(t)*cos(t+pi), r(t)*sin(t+pi), 0.3, fill="red")
    A.plate.press()
A.develop(cleanup=False)

