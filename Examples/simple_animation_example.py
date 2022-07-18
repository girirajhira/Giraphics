from giraphics.animate.animation import Animation
from math import cos, sin, pi

frames = 61
xlim = 16/4
ylim = 9/4
res_x = 2560
res_y = 1440
video_name = 'fjumping2.mp4'
A = Animation(video_name, frames, res_x, res_y, xlim, ylim)

def f(t):
    return ((1.5)/(0.3*t+0.7))*(cos(2.7*t))**2
def r(t):
    return 3/(t+1)


for i in range(0, frames):
    t = 12 * i / frames
    A.plate.bg(colour="white")
    # A.plate.draw_circle(r(t)*cos(t), r(t)*sin(t), 0.3, fill="red")
    # A.plate.draw_circle(r(t)*cos(t+pi), r(t)*sin(t+pi), 0.3, fill="red")
    A.plate.add_latex('abcdefghijkghsjdld;aldkf;aksf;las;kaslda;kds;kasdlka;sdk;lakda;skd;laksd;k'[:i], 0, 0, scale=3, rotation=0, centre_align=True)
    A.plate.press()
A.develop(cleanup=True)
