import math
import numpy as np
from graph import *
from colour import *
from colour import max, norm, hex_to_vec

'''
ToDOs:
Finish Vectorfields
Create tools - Distrs, velocities
 '''

class Grapher(Graph):
    def polar_grid(self, grids = [10, 10], colour="white", stroke=1, opac = 0.8):
        r = self.xlim
        for i in range(1,grids[0]+1):
            self.svg.draw_circ(0,0,r*(i/grids[0]),stroke=colour)
        for i in range(1,grids[1]+1):
            dt = 2*math.pi*(i/grids[1])
            self.svg.draw_line(0,0,10*self.xlim*math.cos(dt),10*self.xlim*math.sin(dt))
            #Draw Rays from the origin

    def VectorField(self, func, gridint=10, scale=0.08, strokewidth = 1.25, stroke="white", arrow = True, constcolour=False, initColour=[0, 130, 50], endColour=[2, 66, 130], grids=[10,10], grid=False, bg=True, bgColour = "black", gridColour="white", constLength=False, length_scale= 1, arrow_scale=1 ):
        """

        :type gridint: int
        """
        epsx = self.xlim/gridint
        epsy = self.ylim/gridint
        if bg:
            self.bg(bgColour)
        if grid:
            self.grid(grids, colour=gridColour, opac=0.5)
        fl= 1
        if not constLength:
            fl = 0
        if constcolour:
            if not arrow:
                arrow_scale = 0

            for i in range(-gridint,gridint+1):
                for j in range(-gridint, gridint+1):
                    x, y = epsx*i, epsy*j
                    f = func(x, y)
                    x2 = self.tranx(x + (f[0])*length_scale)
                    y2 = self.trany(y + (f[1])*length_scale)
                    if abs(f[0]) <= 0.05 and abs(f[1]) <= 0.05:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=stroke, strokewidth=strokewidth, scale=arrow_scale)

        else:
            cl = linear(initColour, endColour)
            if not arrow:
                arrow_scale = 0
            L = []
            for i in range(-gridint,gridint+1):
                for j in range(-gridint, gridint+1):
                    x, y = epsx*i, epsy*j
                    f = func(x,y)
                    L.append(norm(f))
            M = max(L)
            for i in range(-gridint, gridint+1):
                for j in range(-gridint, gridint+1):
                    x, y = epsx*i, epsy*j
                    f = func(x,y)
                    fn = norm(f)*fl if norm(f)*fl != 0 else 1
                    x2 = self.tranx(x + (f[0])*length_scale/fn)
                    y2 = self.trany(y + (f[1])*length_scale/fn)
                    if abs(f[0]) <= 0.1 and abs(f[1]) <= 0.1:
                        self.svg.draw_circ(self.tranx(x), self.trany(y), scale * 6, fill=cl((norm(f))/(M)), strokewidth=0)
                    else:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=cl((norm(f))/(M)), strokewidth=strokewidth, scale=arrow_scale)

    def hj(self, x, xlim):
        return 0.1 + 0.9*x*x/xlim

    def ComplexPlotScatter(self, func, s = 1, type="cart", grids = [10,10], colour="white", opac = 1):
        self.bg(colour="black")
        if type == "cart":
            self.grid(grids, colour="lightblue")
        elif type == "polar":
            self.polar_grid(grids, colour="white")
        elif type == "false":
            pass
        R = []
        I = []
        for x in range(-grids[0], grids[0] + 1):
            for y in range(-grids[1], grids[1]):
                R.append(func(self.hj(x, self.xlim)*x*self.xlim/grids[0],self.hj(y, self.ylim)*y*self.ylim/grids[0]).real)
                I.append(func(self.hj(x, self.xlim)*x*self.xlim/grids[0],self.hj(y, self.ylim)*y*self.ylim/grids[0]).imag)
        self.scatter(R, I, s, colour=colour, opac=opac)

    def ComplexPlot(self, func, type="cart", grids = [20,20], grid = False, strokewidth = 1, colour="red", axes = True, N = 100, bg = False, epsfuncorder=1):
        eps = self.xlim / N
        if bg:
            self.bg(colour="black")
        if grid:
            if type == "cart":
                self.grid(grids, colour="lightblue")
            elif type == "polar":
                self.polar_grid(grids, colour="white")

        for i in range(-N,N+1):
            Y = []
            X = []
            for j in range(-N,N+1):
                x = eps*i**epsfuncorder
                y = eps*j**epsfuncorder
                X.append(self.tranx(func(x,y).real))
                Y.append(self.trany(func(x,y).imag))
            self.svg.draw_polyline(X, Y, colour="yellow", strokewidth=strokewidth)
        for i in range(-N,N+1):
            Y = []
            X = []
            for j in range(-N,N+1):
                x = eps * i ** epsfuncorder
                y = eps * j ** epsfuncorder
                X.append(self.tranx(func(x,y).real))
                Y.append(self.trany(func(x,y).imag))
            self.svg.draw_polyline(X, Y, colour="lightblue", strokewidth=strokewidth)

    def LinearTranforms(self, M, grids = [20,20], strokewidth = 1, colour="red"):
        self.bg(colour="black")
        func = 1
        self.axes(colour="white", strokewidth=2)
        self.grid(grids, colour="lightblue")
        Mat = np.array(M)
        P = np.array([[i,j] for i in range(-grids[0], grids[0]+1) for j in range(-grids[1], grids[1]+1)]).T
        Points = np.matmul(Mat,P)
        for i in range(-self.N, self.N + 1):
            Y, X = [], []
            for j in range(-self.N, self.N + 1):
                y = self.eps * i
                x = self.eps * j
                X.append(self.tranx(func(x, y).real))
                Y.append(self.trany(func(x, y).imag))
                self.svg.draw_polyline(X, Y, colour="yellow", strokewidth=strokewidth)

class Figure(Grapher):



#'''
from math import sin, sqrt
from math import e
def func(x, y):
    if x != 0 or y != 0:
        return [(y+x)/sqrt(x**2 + y**2), -x*sin(x)/sqrt(x**2 + y**2)]
    else:
        return [0, 0]

A = Grapher(1400,1400,10,10,"collaz3.svg")
#A.VectorField(func, gridint=5,  arrow_scale=2, strokewidth=2, stroke="white", arrow = True, constcolour=False,constLength=True)
A.VectorField(func, gridint=15,  arrow_scale=1.5, strokewidth=2, length_scale=0.5, grids=[30,30], arrow = True, constcolour=False, bg=True, constLength=True, initColour=hex_to_vec('#000099'), endColour=hex_to_vec('#ff99cc'), grid=True)

A.show()

#'''