from giraphics.animate.animation import Animation
import numpy as np
from giraphics.utilities.colour import *

width = 700
height = 700

xlim = 5
ylim = 5

pauses = True

name = 'pendulumscene.mp4'
A = Animation(name, None, width, height, xlim, ylim, pauses=pauses)

### Introduction

# Add first circle
intro_frames = 20
for i in range(intro_frames):
    A.plate.bg()
    r = .3 * (i + 1) / intro_frames
    A.plate.draw_circle(0, 0, r, fill='white')
    A.plate.press()

# Draw string
for i in range(intro_frames):
    A.plate.bg()
    A.plate.draw_circle(0, 0, r, fill='white')
    y = 4 * (i + 1) / intro_frames
    A.plate.draw_line(0, 0, 0, y, colour='white', strokewidth=2)
    A.plate.press()

# Draw pivot
intro_frames = 30
for i in range(intro_frames):
    A.plate.bg()
    r2 = .1 * (i + 1) / intro_frames
    A.plate.draw_circle(0, 0, r, fill='white')
    A.plate.draw_line(0, 0, 0, y, colour='white', strokewidth=2)
    A.plate.draw_circle(0, y, r2, fill='white')
    A.plate.press()

A.pause(30)

# Perturb the pendulum
perturb_frames = 45
for i in range(perturb_frames):
    A.plate.bg()
    theta = (np.pi / 9) * (i + 1) / perturb_frames
    y1 = y - y * np.sin(theta + np.pi / 2)
    x1 = y * np.cos(theta + np.pi / 2)
    A.plate.draw_circle(x1, y1, r, fill='white')
    A.plate.draw_line(x1, y1, 0, y, colour='white', strokewidth=2)
    A.plate.draw_line(0, y, 0, y, colour='white', strokewidth=2, style='dashed', opacity=i / perturb_frames)
    A.plate.draw_circle(0, y, r2, fill='white')
    A.plate.draw_arc(0, y, 2.5, 3 * np.pi / 2, -theta + 3 * np.pi / 2, colour='white', strokewidth=1
                     )
    # Drawing the arc
    A.plate.press()

A.pause(60)

# Add theta
perturb_frames = 10
for i in range(perturb_frames):
    A.plate.bg()
    A.plate.draw_circle(x1, y1, r, fill='white')
    A.plate.draw_line(x1, y1, 0, y, colour='white', strokewidth=2)
    A.plate.draw_line(0, y, 0, y, colour='white', strokewidth=2, style='dashed', opacity=i/perturb_frames)
    A.plate.draw_circle(0, y, r2, fill='white')
    A.plate.draw_arc(0, y, 2.5, 3 * np.pi / 2, -theta + 3 * np.pi / 2, colour='white', strokewidth=1)

    phi = -(np.pi / 9) / 2

    x2 = 3 * np.cos(phi + 3 * np.pi / 2)
    y2 = 4 + 3 * np.sin(phi + 3 * np.pi / 2)
    A.plate.add_latex(r'$\theta$', x2, y2, colour='white', opacity=i / perturb_frames, scale=2)
    # Drawing the arc
    A.plate.press()
A.pause(60)

A.plate.add_inset(0, 0, 5, 1.3, position=[0, -2.5], origin=[-5, 0], border=True, bstroke=.5)

# Draw inset
perturb_frames = 20
for i in range(perturb_frames):
    A.plate.bg()
    A.plate.draw_circle(x1, y1, r, fill='white')
    A.plate.draw_line(0, y, 0, y, colour='white', strokewidth=2, style='dashed')
    A.plate.draw_line(x1, y1, 0, y, colour='white', strokewidth=2)
    A.plate.draw_circle(0, y, r2, fill='white')
    A.plate.draw_arc(0, y, 2.5, 3 * np.pi / 2, -theta + 3 * np.pi / 2, colour='white', strokewidth=1)
    A.plate.add_latex(r'$\theta$', x2, y2, colour='white', scale=2)
    h1 = 2.4
    w1 = 4
    A.plate.insets[0].update_properties(width=w1, height=h1)
    A.plate.insets[0].axes()
    A.plate.press()

# Simulating the pendulum
simulation_frames = 5 * 60
tlist = 16 * np.linspace(0, 1, simulation_frames)
theta_list = (np.pi / 9) * np.cos(tlist)
for i in range(simulation_frames):
    A.plate.bg()
    t = 16 * (i + 1) / simulation_frames
    theta = (np.pi / 9) * np.cos(t)
    y1 = y - y * np.sin(theta + np.pi / 2)
    x1 = y * np.cos(theta + np.pi / 2)
    y2 = 4 - 3 * np.sin(theta / 2 + np.pi / 2)
    x2 = 3 * np.cos(theta / 2 + np.pi / 2)
    A.plate.draw_circle(x1, y1, r, fill='white')
    A.plate.add_latex(r'$\theta$', x2, y2, colour='white', scale=2)
    A.plate.draw_line(0, 0, 0, y, colour='white', strokewidth=2, style='dashed')
    A.plate.draw_line(x1, y1, 0, y, colour='white', strokewidth=2)
    A.plate.draw_circle(0, y, r2, fill='white')
    A.plate.add_inset(w1, h1, 5, 1.5, position=[0, -2.5], origin=[-8, 0], border=True)
    A.plate.draw_arc(0, y, 2.5, 3 * np.pi / 2, - theta + 3 * np.pi / 2, colour='white', strokewidth=1)
    A.plate.insets[0].axes()
    A.plate.insets[0].grid()
    A.plate.insets[0].plot_points(tlist[:i], theta_list[:i], strokewidth=2,colour = Blues.teal)
    A.plate.press()

A.pause(60)

A.develop(cleanup=False)
