from giraphics.graphing.graph import *
from giraphics.animate.animation import *
import numpy as np

width = 600
height = 400
xlim = 6
ylim = 4

G = Graph(width, height, xlim,ylim, 'wick2feynman.svg')

# W = [[0., 0., 0., 0., 1., 0.],
#  [0., 0., 0., 0., 0., 1.],
#  [0., 0., 0., 1., 0., 0.],
#  [0., 0., 1., 0., 0., 0.],
#  [1., 0., 0., 0., 0., 0.],
#  [0., 1., 0., 0., 0., 0.]]


W = [[0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
 [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
 [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
 [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
 [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
 [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]
W = np.array(W)



wx = -2
fx = 2
wy =  0
fy = 0
n = int(len(W)/2 - 1)
num_vertices = int(len(W)/2)
ymax = ylim-1
ymin = -ymax
dy = 2*ymax/num_vertices
shift = int(len(W)/2)
W_pos = np.zeros((len(W), 2))

for i in range(len(W)):
    if i < len(W)/2:
        a = -1 # Left set
    else:
        a =  1 # right set
    W_pos[i,: ] = [0+a, ymax - (num_vertices-i%num_vertices)*dy]

t = np.linspace(0, 1, 200)



G.bg(colour="black")

interaction_blocks = [i for i in range(1, int(len(W)/2)-1, 2)]
for i in range(len(W)):
    if i in interaction_blocks or  i - shift in interaction_blocks:
        G.plot_decorated(W_pos[i,0]+wx+ 0*t, W_pos[i,1] + (W_pos[i+1,1]-W_pos[i,1])*t,
                         amplitude=.1, colour='yellow', strokewidth=.5)
    G.draw_circle(W_pos[i,0]+wx, W_pos[i,1], .1, colour='white', fill='white')
    G.draw_circle(W_pos[i,0]+wx, W_pos[i,1], .1, colour='white', fill='white')
    if i < shift:
        G.text(W_pos[i,0]+wx-.4, W_pos[i,1], f'{i}', colour='white', fontsize=20)
    else:
        G.text(W_pos[i,0]+wx+.4, W_pos[i,1], f'{i}', colour='white', fontsize=20)


for i in range(len(W)):
    for j in range(len(W)):
        if W[i,j] == 1:
            G.draw_line(W_pos[i,0]+wx, W_pos[i,1], W_pos[j,0]+wx,W_pos[j,1], colour='white', strokewidth=.5)


#
# Feynman Diagrams
for i in range(len(W)):
    if i in interaction_blocks:
        G.plot_decorated(fx + 0*t, W_pos[i,1] + (W_pos[i+1,1]-W_pos[i,1])*t,
                         amplitude=.1, colour='yellow', strokewidth=.5)
    if i != 0 and i != shift:
        G.draw_circle(fx, W_pos[i,1], .1, colour='white', fill='white')
        G.text(fx-.4, W_pos[i,1], f'{i}', colour='white', fontsize=20)
    else:
        G.draw_circle(W_pos[i,0]+fx, W_pos[i,1], .1, colour='white', fill='white')
        G.draw_circle(W_pos[i,0]+fx, W_pos[i,1], .1, colour='white', fill='white')
        if i < shift:
            G.text(W_pos[i,0]+fx-.4, W_pos[i,1], f'{i}', colour='white', fontsize=20)
        else:
            G.text(W_pos[i,0]+fx+.4, W_pos[i,1], f'{i}', colour='white', fontsize=20)


# for i in range(len(W)):
#     for j in range(len(W)):
#         if W[i, j] == 1:
#             G.p(W_pos[i, 0]+fx, W_pos[i, 1], W_pos[j, 0] + fx, W_pos[j, 1], colour='white', strokewidth=.5)
#




G.save()