from giraphics.utilities.convert import *
from giraphics.graphing.fancygraph import *
import numpy as np
from math import pi
from numpy import sin, cos


def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])



'''

for i in range(frames):
    A = Graph(1000, 1000, 35, 35, "Plotsr/g" + namer(i) + ".svg", origin=[-10,-2])
    A.bg("black")
    V = np.matmul(Ry(i*epss), P)
    #print(i*epss)
    A.plot_points(V[0][:], V[1][:])
    A.save()
print('l')
create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
create_mpeg('sav424ee.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")
'''
'''
def f(t, eps = 0.015, N = 15000):
    def fx(X):
        k = round(eps*t)
        A = np.concatenate([X[0][:k], [None for i in range(len(X)-k-1)]])
        B = np.concatenate([X[1][:k], [None for i in range(len(X)-k-1)]])
        return np.array([A,B])
    return fx
for i in range(frames):
    A = Graph(1000, 1000, 30, 30, "Plotsr/g" + namer(i) + ".svg")
    A.bg("black")
    #print(i*epss)
    V = f(i, eps=N/frames)
    A.plot_points(V(P)[0][:], V(P)[1][:], colour="yellow")
    A.save()
print('l')
create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
create_mpeg('LiveLorent3.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")

'''

class Graph3d(FancyGraph):
    def surface(self, func, rotator, yn = 60, xn = 60):
        mesh = np.mgrid[-5:5.1:0.5, -5:5.1:0.5]
        X = np.linspace(-self.xlim, self.xlim, xn)
        Y = np.linspace(-self.ylim, self.ylim, yn)
        Z = func(X, Y)
        P = np.matmul(rotator, np.column_stack((X,Y,Z)).T)
        for i in range(yn):
            # x lines
            self.plot_points(P[0], np.full(X.shape, P[1][i], dtype=float))
        for j in range(xn):
            # y lines
            self.plot_points(np.full(X.shape, P[0][j], dtype=float), P[1])

    def mesh_sphere(self, r, cx, cy, cz, rotator=Rz(1), density=12, dphi=0.05, dtheta=0.05, latitudes=True, longitudes=True, colour="white"):
        centre = np.array([cx, cy, cz])
        if latitudes:
            theta = np.radians(np.linspace(0, 180, density))
            phi = np.arange(0, 2 * pi + dphi, dphi)
            for i in range(density):
                X = r*sin(theta[i])*cos(phi) + cx
                Y = r*sin(theta[i])*sin(phi) + cy
                Z = r*cos(theta[i])*np.full(phi.shape, 1, dtype=float) + cz
                P = np.matmul(rotator, np.column_stack((X,Y,Z)).T)
                self.plot_points(P[0], P[1], colour=colour)
        if longitudes:
            theta = np.arange(0, pi+dtheta, dtheta)
            phi = np.linspace(0, 2 * pi, density)
            for i in range(density):
                X = r * sin(theta) * cos(phi[i]) + cx
                Y = r * sin(theta) * sin(phi[i]) + cy
                Z = r * cos(theta) + cz
                P = np.matmul(rotator, np.column_stack((X, Y, Z)).T)
                self.plot_points(P[0], P[1], colour=colour)

    def axes3d(self, rotator):
        vecspos = np.array([[1,0,0], [0,1,0], [0,0,1]])*self.xlim
        vecsneg = -np.array([[1,0,0], [0,1,0], [0,0,1]])*self.xlim
        V1 = np.matmul(rotator, vecspos)
        V2 = np.matmul(rotator, vecsneg)
        self.svg.draw_arrow(self.tranx(V2[0][0]),self.trany(V2[0][1]), self.tranx(V1[0][0]), self.trany(V1[0][1]),stroke="white")
        self.svg.draw_arrow(self.tranx(V2[1][0]),self.trany(V2[1][1]),self.tranx(V1[1][0]), self.trany(V1[1][1]),stroke="white")
        self.svg.draw_arrow(self.tranx(V2[2][0]),self.trany(V2[2][1]),self.tranx(V1[2][0]), self.trany(V1[2][1]),stroke="white")

    def Rz(self,theta, r=1):
        return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])

    def Rx(self,theta, r=1):
        return np.array([ [0, 0, 1],[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0]])

    def Ry(self,theta, r=1):
        return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])

# frames = 200
# create_directory("Plotsr")
# create_directory("plotsrast")
#
# def rtr(t, w = 0.02):
#     return np.matmul(Rz(0.33), Ry(w*t))
# def funx(x,y):
#     return -0.3*(x**2 + sin(y))
#
# for i in range(frames):
#     A = Graph3d(1000, 1000, 30, 30, "Plotsr/g" + namer(i) + ".svg")
#     A.bg("black")
#     A.surface(funx, rtr(i))
#     A.axes_3d(rtr(i))
#    # A.mesh_sphere(6, 0, 0, 0, rotator=rtr(i))
#     A.save()
#
# create_raster_batch("Plotsr", 'g', 'p', 'plotsrast', frames)
# create_mpeg('../../sample_projects/Videos/surf1.mp4', 'p', frames, dir=os.getcwd() + "/plotsrast")
class Animation