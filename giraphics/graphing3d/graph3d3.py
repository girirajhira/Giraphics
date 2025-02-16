from giraphics.utilities.convert import *
from giraphics.graphing.fancygraph import *
import numpy as np
from math import pi
from numpy import sin, cos


def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0],
                     [sin(theta), cos(theta), 0],
                     [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)],
                     [0, 1, 0],
                     [-sin(theta), 0, cos(theta)]])


class Graph3d(FancyGraph):
    self.view = np.eye(3)
    def tranx(self, v):
        """
        converts the x coordinate to svg coordinate
        :param x: float
            x coordinate in standard units
        :returns: float
            return the x coordinate in y
        """
        x =  self.view@v[0]
        if x is not None:
            return + round((self.width / (2 * self.xlim)) * (x + self.origin[0]) + self.width / 2, 2)
            return - round((self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height / 2, 2)

        else:
            return None

    def trany(self, v):
        """
        converts the y coordinate to svg coordinate
        :param y:
        :return: svg coordinate
        """
        y =  self.view@v[1]
        if y is not None:
            return round(-(self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height / 2, 2)
        else:
            return None

    def surface(self, func, rotator, yn=30, xn=30):
        mesh = np.mgrid[-5:5.1:0.5, -5:5.1:0.5]
        X = np.linspace(-self.xlim, self.xlim, xn)
        Y = np.linspace(-self.ylim, self.ylim, yn)
        Z = func(X, Y)
        P = np.matmul(rotator, np.column_stack((X, Y, Z)).T)
        for i in range(yn):
            # x lines
            self.plot(P[0], np.full(X.shape, P[1][i], dtype=float))
        for j in range(xn):
            # y lines
            self.plot(np.full(X.shape, P[0][j], dtype=float), P[1])

    def mesh_sphere(self, r, cx, cy, cz, rotator=Rz(1), density=12, dphi=0.05, dtheta=0.05, latitudes=True,
                    longitudes=True, colour="white", strokewidth=1):
        centre = np.array([cx, cy, cz])
        if latitudes:
            theta = np.radians(np.linspace(0, 180, density))
            phi = np.arange(0, 2 * pi + dphi, dphi)
            for i in range(density):
                X = r * sin(theta[i]) * cos(phi) + cx
                Y = r * sin(theta[i]) * sin(phi) + cy
                Z = r * cos(theta[i]) * np.full(phi.shape, 1, dtype=float) + cz
                P = np.matmul(rotator, np.column_stack((X, Y, Z)).T)
                self.plot(P[0], P[1], colour=colour, strokewidth=strokewidth)
        if longitudes:
            theta = np.arange(0, pi + dtheta, dtheta)
            phi = np.linspace(0, 2 * pi, density)
            for i in range(density):
                X = r * sin(theta) * cos(phi[i]) + cx
                Y = r * sin(theta) * sin(phi[i]) + cy
                Z = r * cos(theta) + cz
                P = np.matmul(rotator, np.column_stack((X, Y, Z)).T)
                self.plot(P[0], P[1], colour=colour, strokewidth=strokewidth)

    def axes3d(self, rotator):
        vecspos = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * self.xlim
        vecsneg = -np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * self.xlim
        V1 = np.matmul(rotator, vecspos)
        V2 = np.matmul(rotator, vecsneg)
        self.svg.draw_arrow(self.tranx(V2[0][0]), self.trany(V2[0][1]), self.tranx(V1[0][0]), self.trany(V1[0][1]),
                            stroke="white")
        self.svg.draw_arrow(self.tranx(V2[1][0]), self.trany(V2[1][1]), self.tranx(V1[1][0]), self.trany(V1[1][1]),
                            stroke="white")
        self.svg.draw_arrow(self.tranx(V2[2][0]), self.trany(V2[2][1]), self.tranx(V1[2][0]), self.trany(V1[2][1]),
                            stroke="white")
    def Rz(self, theta, r=1):
        return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])

    def Rx(self, theta, r=1):
        return np.array([[0, 0, 1], [cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0]])

    def Ry(self, theta, r=1):
        return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])

def f(x, y):
    return x * x - y * y


G3 = Graph3d(800, 800, 5, 5, 'test3d.svg')
G3.bg(colour='teal')
G3.axes3d(Rz(1)@Ry(1))
G3.mesh_sphere(4, 0, 0, 0, Rz(1) @ Ry(1), strokewidth=.4)
G3.save()
