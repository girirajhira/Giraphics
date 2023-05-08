from giraphics.animate.animation import Animation
from giraphics.utilities.utils import Rx, Ry, Rz
from math import pi
name = 'stereographic.mp4'

A = Animation(name, None, 700, 700, 5, 5)

frames = 3 * 60

for i in range(frames):
    Theta = pi/2 * (i / frames)
    rotator = Rz(Theta/5)
    A.plate.bg(colour='white')
    A.plate.axes3d(colour='black', rotator=rotator)
    A.plate.mesh_sphere(3, 0, 0, 0, rotator=rotator, colour='black')
    A.plate.press()

for i in range(frames):
    Theta = pi/4 * (i / frames)
    rotator = Rx(Theta/5)
    A.plate.bg(colour='white')
    A.plate.axes3d(colour='black', rotator=rotator)
    A.plate.mesh_sphere(3, 0, 0, 0, rotator=rotator, colour='black')
    A.plate.press()

for i in range(frames):
    Theta = -pi/2 * (i / frames)
    rotator = Rz(Theta/5)
    A.plate.bg(colour='white')
    A.plate.axes3d(colour='black', rotator=rotator)
    A.plate.mesh_sphere(3, 0, 0, 0, rotator=rotator, colour='black')
    A.plate.press()
A.pause(30)
A.develop()

