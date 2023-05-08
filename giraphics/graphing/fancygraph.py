import math
from giraphics.utilities.colour import *
from giraphics.utilities.colour import max, norm, vec_to_hex
from giraphics.utilities.utils import max2d, min2d, parity
from giraphics.graphing.graph import Graph
import numpy as np
from math import pi
from numpy import sin, cos
from giraphics.utilities.utils import Rz, Ry, Rz

'''
ToDOs:
Finish Vectorfields
Create tools - Distrs, velocities
 '''


class FancyGraph(Graph):
    def polar_grid(self, grids=[10, 10], colour="white", stroke=1, opac=0.8):
        r = self.xlim
        for i in range(1, grids[0] + 1):
            self.svg.draw_circ(0, 0, r * (i / grids[0]), stroke=colour)
        for i in range(1, grids[1] + 1):
            dt = 2 * math.pi * (i / grids[1])
            self.svg.draw_line(0, 0, 10 * self.xlim * math.cos(dt), 10 * self.xlim * math.sin(dt))
            # Draw Rays from the origin

    def VectorField_old(self, func, gridint=None, scale=0.08, strokewidth=1.25, stroke="white", arrow=True,
                        constcolour=False, initColour=[0, 130, 50], endColour=[2, 66, 130], grids=[10, 10], grid=False,
                        bg=True, bgColour="black", gridColour="white", constLength=False, length_scale=1,
                        arrow_scale=1):
        """
        :type gridint: int
        """

        epsx = self.xlim / gridint
        epsy = self.ylim / gridint
        if bg:
            self.bg(bgColour)
        if grid:
            self.grid(grids, colour=gridColour, opac=0.5)
        fl = 1
        if not constLength:
            fl = 0
        if constcolour:
            if not arrow:
                arrow_scale = 0

            for i in range(-gridint, gridint + 1):
                for j in range(-gridint, gridint + 1):
                    x, y = epsx * i, epsy * j
                    f = func(x, y)
                    x2 = self.tranx(x + (f[0]) * length_scale)
                    y2 = self.trany(y + (f[1]) * length_scale)
                    if abs(f[0]) <= 0.05 and abs(f[1]) <= 0.05:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=stroke,
                                            strokewidth=strokewidth, scale=arrow_scale)

        else:
            cl = linear(initColour, endColour)
            if not arrow:
                arrow_scale = 0
            L = []
            for i in range(-gridint, gridint + 1):
                for j in range(-gridint, gridint + 1):
                    x, y = epsx * i, epsy * j
                    f = func(x, y)
                    L.append(norm(f))
            M = max(L)
            for i in range(-gridint, gridint + 1):
                for j in range(-gridint, gridint + 1):
                    x, y = epsx * i, epsy * j
                    f = func(x, y)
                    fn = norm(f) * fl * gridint / (2 * self.xlim) if norm(f) * fl != 0 else 1
                    x2 = self.tranx(x + (f[0]) * length_scale / fn)
                    y2 = self.trany(y + (f[1]) * length_scale / fn)
                    if f == [0, 0]:
                        self.svg.draw_circ(self.tranx(x), self.trany(y), scale * 70, fill=vec_to_hex(endColour),
                                           strokewidth=0)
                    else:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=cl((norm(f)) / M),
                                            strokewidth=strokewidth, scale=arrow_scale)

    def VectorField(self, func, gridint=None, scale=0.08, strokewidth=1.25, stroke="white", arrow=True,
                    constColour=False,
                    initColour=[0, 130, 50], endColour=[2, 66, 130],
                    constLength=False, tail_length=1, arrow_scale=1, grid_multiplier=1):
        """
        :type gridint: int
        """

        if gridint is None:
            gridint = []
            if self.xlim < 5:
                gridint.append(round(2 * self.xlim * grid_multiplier))
            else:
                gridint.append(2 * self.xlim)
            if self.ylim < 5:
                gridint.append(round(2 * self.ylim * grid_multiplier))
            else:
                gridint.append(2 * self.ylim)

        epsx = self.xlim / gridint[0]
        epsy = self.ylim / gridint[1]

        fl = 1
        if not constLength:
            fl = 0
        if constColour:
            if not arrow:
                arrow_scale = 0

            for i in range(-gridint[0], gridint[0] + 1):
                for j in range(-gridint[1], gridint[1] + 1):
                    x, y = epsx * i - self.origin[1], epsy * j - self.origin[1]
                    f = func(x, y)
                    x2 = self.tranx(x + (f[0]) * tail_length)
                    y2 = self.trany(y + (f[1]) * tail_length)
                    if abs(f[0]) <= 0.05 and abs(f[1]) <= 0.05:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=stroke,
                                            strokewidth=strokewidth, scale=arrow_scale)

        else:
            cl = linear(initColour, endColour)
            if not arrow:
                arrow_scale = 0
            L = []
            for i in range(-gridint[0], gridint[0] + 1):
                for j in range(-gridint[1], gridint[1] + 1):
                    x, y = epsx * i - self.origin[1], epsy * j - self.origin[1]
                    f = func(x, y)
                    L.append(norm(f))
            M = max(L)
            for i in range(-gridint[0], gridint[0] + 1):
                for j in range(-gridint[1], gridint[1] + 1):
                    x, y = epsx * i - self.origin[1], epsy * j - self.origin[1]
                    f = func(x, y)
                    fn = norm(f) * fl * gridint[0] / (2 * self.xlim) if norm(f) * fl != 0 else 1
                    x2 = self.tranx(x + (f[0]) * tail_length / fn)
                    y2 = self.trany(y + (f[1]) * tail_length / fn)
                    if f == [0, 0]:
                        self.svg.draw_circ(self.tranx(x), self.trany(y), scale * 70, fill=vec_to_hex(endColour),
                                           strokewidth=0)
                    else:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=cl((norm(f)) / M),
                                            strokewidth=strokewidth, scale=arrow_scale)

    def hj(self, x, xlim):
        return 0.1 + 0.9 * x * x / xlim

    def ComplexPlotScatter(self, func, s=1, type="cart", grids=[10, 10], colour="white", opac=1):
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
                R.append(func(self.hj(x, self.xlim) * x * self.xlim / grids[0],
                              self.hj(y, self.ylim) * y * self.ylim / grids[0]).real)
                I.append(func(self.hj(x, self.xlim) * x * self.xlim / grids[0],
                              self.hj(y, self.ylim) * y * self.ylim / grids[0]).imag)
        self.scatter(R, I, s, colour=colour, opac=opac)

    def ComplexPlot(self, func, strokewidth=1, colour="red", N=100, epsfuncorder=1):
        eps = self.xlim / N

        for i in range(-N, N + 1):
            Y = []
            X = []
            for j in range(-N, N + 1):
                x = eps * i ** epsfuncorder
                y = eps * j ** epsfuncorder
                X.append(self.tranx(func(x, y).real))
                Y.append(self.trany(func(x, y).imag))
            self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth)
        for i in range(-N, N + 1):
            Y = []
            X = []
            for j in range(-N, N + 1):
                x = eps * i ** epsfuncorder
                y = eps * j ** epsfuncorder
                X.append(self.tranx(func(x, y).real))
                Y.append(self.trany(func(x, y).imag))
            self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth)

    def LinearTransforms(self, M, grids=[20, 20], strokewidth=1, colour="red"):
        self.bg(colour="black")
        func = 1
        self.axes(colour="white", strokewidth=2)
        self.grid(grids, colour="lightblue")
        Mat = np.array(M)
        P = np.array([[i, j] for i in range(-grids[0], grids[0] + 1) for j in range(-grids[1], grids[1] + 1)]).T
        Points = np.matmul(Mat, P)
        for i in range(-self.N, self.N + 1):
            Y, X = [], []
            for j in range(-self.N, self.N + 1):
                y = self.eps * i
                x = self.eps * j
                X.append(self.tranx(func(x, y).real))
                Y.append(self.trany(func(x, y).imag))
                self.svg.draw_polyline(X, Y, colour="yellow", strokewidth=strokewidth)

    def DenistyPlotFunction(self, func, points=[60, 60], initColour=[10, 40, 30], endColour=[100, 240, 20]):
        # Do simultaneous
        # Edge Issue
        xres = round(points[0] / 2)
        yres = round(points[1] / 2)
        field = np.array(
            [[func((x - self.origin[0]) * xres / (2 * self.xlim), (y - self.origin[1]) * yres / (2 * self.ylim))
              for x in range(-xres, xres + 1)]
             for y in range(-yres, yres + 1)])
        cl = linear(initColour, endColour)
        max = max2d(field)
        min = min2d(field)
        xx = xres / (self.xlim)
        yy = yres / (self.ylim)
        for j in range(0, 2 * xres):
            for k in range(0, 2 * yres):
                self.draw_rect((j - xres) * self.xlim / xres - self.origin[0],
                               (k - yres) * self.ylim / yres - self.origin[1], 1 / xx, 1 / yy,
                               cl((field[k][j] - min) / (max - min)), strokewidth=0)
                # self.text(j*self.xlim/xres, k*self.ylim/yres, str(round(j*self.xlim/xres,1)) +"," +str(round(k*self.ylim/yres,1)) , colour="red",fontsize=1)

    def DenistyPlot(self, field, initColour=[10, 40, 30], endColour=[100, 240, 20], strokewidth=0):
        # Do simultaneous
        # Edge Issue
        p1, p2 = field.shape
        xres = (p1)
        yres = (p2)
        cl = linear(initColour, endColour)
        max = max2d(field)
        min = min2d(field)
        xx = 1 / 2 * xres / (self.xlim)
        yy = 1 / 2 * yres / (self.ylim)
        for j in range(0, xres):
            for k in range(0, yres):
                self.draw_rect((2 * j - xres) * self.xlim / xres - self.origin[0] + 1 / xx / 2,
                               (2 * k - yres) * self.ylim / yres - self.origin[1] + 1 / yy / 2, 1 / xx, 1 / yy,
                               cl((field[k][j] - min) / (max - min)), strokewidth=strokewidth)
                # self.text(j*self.xlim/xres, k*self.ylim/yres, str(round(j*self.xlim/xres,1)) +"," +str(round(k*self.ylim/yres,1)) , colour="red",fontsize=1)

    def histogram(self, datax, datay, colour="yellow", width=1, opacity=1):
        if len(datax) != len(datay):
            raise ValueError('Data must be of the same length.')
        width = 19*width*self.nscale*(datax[-1]-datax[0])/len(datax)
        for i in range(len(datax)):
            self.draw_line(datax[i], 0, datax[i], datay[i], colour=colour, strokewidth=width, opacity=opacity)

    def Penrose(self, grids=10):
        self.bg(colour="black")
        self.draw_line(0, self.ylim, self.xlim, 0, colour="yellow")
        self.draw_line(0, self.ylim, -self.xlim, 0, colour="yellow")
        self.draw_line(-self.xlim, 0, 0, -self.ylim, colour="yellow")
        self.draw_line(self.xlim, 0, 0, -self.ylim, colour="yellow")
        self.axes()

    def add_inset(self, width, height, xlim, ylim, position=[0, 0], origin=[0.0, 0.0],
                  border=True, bcol="white", bstroke=1.5, bopacity=1, magnifier=False, magnifier_pos=[0, 0],
                  magnifier_dims=[1, 1], magnifier_fill=None, magnifier_opacity = 1):
        bstroke = bstroke*self.nscale
        width1 = width * self.xscale
        height1 = height * self.yscale

        absx = round(self.tranx(position[0]) - width1 / 2, 2)
        absy = round(self.trany(position[1]) - height1 / 2, 2)

        # if border:
        #     self.draw_rect(position[0], position[1], width, height, fill='None', colour=bcol, strokewidth=bstroke * 2,
        #                    opac=bopacity)

        if magnifier:
            self.draw_rect(magnifier_pos[0], magnifier_pos[1], magnifier_dims[0], magnifier_dims[1], fill=magnifier_fill,
                           fill_opacity=magnifier_opacity, opac=bopacity, strokewidth=bstroke, colour=bcol)
            px = parity(position[0] - magnifier_pos[0])
            py = parity(position[1] - magnifier_pos[1])
            x11 = magnifier_pos[0] - magnifier_dims[0] * px / 2
            y11 = magnifier_pos[1] + magnifier_dims[1] * py / 2
            x12 = position[0] - width * px / 2
            y12 = position[1] + height * py / 2
            x21 = magnifier_pos[0] + magnifier_dims[0] * px / 2
            y21 = magnifier_pos[1] - magnifier_dims[1] * py / 2
            x22 = position[0] + width * px / 2
            y22 = position[1] - height * py / 2
            self.draw_line(x11, y11, x12, y12, colour=bcol, strokewidth=bstroke, opacity=bopacity)
            self.draw_line(x21, y21, x22, y22, colour=bcol, strokewidth=bstroke, opacity=bopacity)

        self.insets.append(
            FancyGraph(width1, height1, xlim, ylim, '', origin=origin, transform=f'translate({absx} {absy})'))
        if border:
            self.insets[-1].draw_rect(origin[0], origin[1], xlim, ylim, fill='none', colour=bcol, strokewidth=bstroke, opac=bopacity)

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
        # centre = np.array([cx, cy, cz])
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

    def axes3d(self, rotator, colour='white'):
        # (3 x 3) @ (3, n)
        vecspos = np.array([[1,0,0], [0,1,0], [0,0,1]])*self.xlim
        vecsneg = -np.array([[1,0,0], [0,1,0], [0,0,1]])*self.xlim

        V1 = np.matmul(rotator, vecspos.T)
        V2 = np.matmul(rotator, vecsneg.T)
        self.svg.draw_arrow(self.tranx(V2[0][0]),self.trany(V2[0][1]), self.tranx(V1[0][0]), self.trany(V1[0][1]),stroke=colour)
        self.text( (V1[0][0]), (V1[0][1]), 'x', colour='black')
        self.svg.draw_arrow(self.tranx(V2[1][0]),self.trany(V2[1][1]), self.tranx(V1[1][0]), self.trany(V1[1][1]),stroke=colour)
        self.text( (V1[1][0]), (V1[1][1]), 'y', colour='black')
        self.svg.draw_arrow(self.tranx(V2[2][0]),self.trany(V2[2][1]), self.tranx(V1[2][0]), self.trany(V1[2][1]),stroke=colour)
        self.text( (V1[2][0]), (V1[2][1]), 'z', colour='black')


    def save(self, clear=False):
        if len(self.insets) != 0:
            for widg in self.insets:
                self.svg.canvas += widg.svg.canvas + '\n</svg>\n</g>'
                widg.svg.canvas = ''
                widg.svg.canvas = widg.svg.preamble
        self.svg.save()
        if clear:
            self.svg.canvas = ""

# A = FancyGraph(500, 500, 5, 5, "penrose.svg")
# A.Penrose()
# A.save()
# A.display()

# class Figure(Grapher):
# def f(x,y):
#     # return np.sin((x / 10) ** 2 + (y / 10) ** 2)
#     return np.sin(x)*np.cos(y)
# def spherical(x,y):
#     pass
#
# A = FancyGraph(500,500,5,5,"dense.svg", origin=[3,0])
# A.bg(colour="black")
# A.DenistyPlot(f)
# A.save()
# A.display()

# def func(x, y):
#
#     if (x != 1 !=  x != -1) or y != 0:
#         Ex = (x + 1) / ((x + 1) ** 2 + y ** 2) - (x - 1) / ((x - 1) ** 2 + y ** 2)
#         Ey = y / ((x + 1) ** 2 + y ** 2) - y / ((x - 1) ** 2 + y ** 2)
#         return [Ex, Ey]
#     else:
#         return [0, 0]
#

# A = FancyGraph(1400,1400,5,5,"Dipole.svg")
# #A.VectorField(func, gridint=5,  arrow_scale=2, stroke_width=2, stroke="white", arrow = True, constcolour=False,constLength=True)
# A.VectorField(func, gridint=25,  arrow_scale=1.5, tail_length=0.5, arrow = True, constLength=True, initColour=hex_to_vec('#000099'), endColour=hex_to_vec('#ff99cc'))
# A.save()

# y = np.array([-2,3,2,3,1,10,-4, 3,-3,1,2, 1, 13, 14])
# x = np.linspace(-4.5, 4.5, len(y))
# A = FancyGraph(500, 500, 5, 5, "histo.svg", origin=[0,0])
# A.bg(colour="black")
# A.histogram(x, y, width=1)
# A.save()
# A.display()
#
#
#
# class SVGPathObject:
#     def __init__(self, type, coordinates, fill=None, stroke=None, strokewidth=1):
#         self.type = type
#         self.coordinates = coordinates
#         self.fill = fill
#         self.stroke = stroke
#         self.strokewidth = strokewidth
#
#     def morph_to(self, other):
#         self
#



# def vecfield(x,y):
#     return [-x*y, x]
#
#
#
# A = FancyGraph(600, 600, 5, 5, 'Ascene.svg')
# from math import sin
# A.bg(colour="black")
# A.axes()
# A.grid()
# A.plot(math.sin)
# A.add_inset(3,3,1,1, position=[3,-3], magnifier=True)
# A.insets[0].bg()
# A.insets[0].axes()
# A.insets[0].plot(math.sin)
# A.add_inset(3,3,5,5, position=[3,3], magnifier=False)
# A.insets[1].bg()
# A.insets[1].VectorField(vecfield, scale=.5)
# A.save()
# A.display()


# def vecfield(x,y):
#     return [-x*y, x]
#
#
# import numpy as np
# from math import sin
# from scipy import interpolate
#
#
# x0 = np.linspace(-5,5,50)
# x, y= np.meshgrid(x0,x0)
#
# z = np.exp(-x*x/5 - y*y/5)*np.sin(x)*np.cos(y)
#
# A = FancyGraph(600, 600, 5, 5, 'Ascene.svg')
# A.bg(colour="black")
# A.axes()
# A.grid()
# A.DenistyPlot(z)
# A.save()
# A.display()


