from giraphics.utilities.convert import *
from giraphics.graphing.fancygraph import *
import numpy as np
from math import cos, sin


def surface(func, x_int, y_int, n0 = 400):
    x = np.linspace(x_int[0], x_int[0], n0)
    y = np.linspace(y_int[0], y_int[0], n0)
    z = []
    for i in range(len(y)):
        z.append(func(x,  np.full((len(y),), y[i])))
    return np.array[x, y, z]

def draw_triangles(surf):
    for i in range(len(surf[0]-1)):
        for j in range(len(surf[1])-1):
            pass

def mesh_grid(func, x_int, y_int, n0 = 400):
    x = np.arrange(x_int[0], x_int[0], n0)
    y = np.arrange(y_int[0], y_int[0], n0)
    z = []
    for i in range(len(y)):
        z.append(func(x,  np.full((len(y),), y[i])))
    return np.array[x, y, z]

def mesh_sphere(r, cx , cy, cz, density = 6):
    centre = np.array([cx, cy, cz])
    theta = np.radians(np.linspace(0, 180, 6))
    data  =
    np.arange()
def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])
'''

v01 = np.array([0, 0, 0])
v02 = np.array([2, 8, 0])
A = Graph(1000, 1000, 10, 10, "Pl.svg")
A.bg("black")

A.svg.draw_arrow(v01[0], v01[1], v02[0], v02[1], stroke="white")
A.save()
'''

create_directory("Plotsr")
create_directory("plotsrast")

frames = 181
eps = 3.1415 / 180
v01 = np.array([0, 0, 0])
v02 = np.array([2, 8, 0])

X, Y, Z = lorentz(0,1,0, 1000)



for i in range(frames):
    A = Graph(1000, 1000, 10, 10, "Plotsr/g" + namer(i) + ".svg")
    A.bg("black")
    R = np.matmul(Rz(eps/2 * i), Ry(eps * i))
    v1 = np.matmul(R, v01)
    v2 = np.matmul(R, v02)
    A.svg.draw_arrow(A.tranx(0), A.trany(0), A.tranx(0), A.trany(10), stroke="white")
    A.svg.draw_arrow(A.tranx(0), A.trany(0), A.tranx(10), A.trany(0), stroke="white")
    A.svg.draw_arrow(A.tranx(v1[0]), A.trany(v1[1]), A.tranx(v2[0]), A.trany(v2[1]), stroke="white")
    A.save()

create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
create_mpeg('sav42ee.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")
