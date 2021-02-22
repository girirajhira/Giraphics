import math

from giraphics.utilities.colour import *
from giraphics.utilities.colour import max, norm, vec_to_hex
from giraphics.utilities.utils import max2d, min2d
from giraphics.graphing.graph import Graph

'''
ToDOs:
Finish Vectorfields
Create tools - Distrs, velocities
 '''


class FancyGraphs(Graph):
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

    def VectorField(self, func, gridint=10, scale=0.08, strokewidth=1.25, stroke="white", arrow=True, constColour=False,
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

    def DenistyPlot(self, func, points=[60, 60], initColour=[10, 40, 30], endColour=[100, 240, 20]):
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

    def histogram(self, data, colour="yellow", width=3):
        dx = 2 * self.xlim / (len(data) + 1)
        dy = 2 * self.ylim / (max(data) + 2)
        ox = -1 * self.xlim
        oy = -1 * self.ylim
        for i in range(len(data)):
            self.draw_line(i * dx + ox, oy, i * dx + ox, data[i] * dy + oy, colour=colour, strokewidth=width)

    def Penrose(self, grids=10):
        self.bg(colour="black")
        self.draw_line(0, self.ylim, self.xlim, 0, colour="yellow")
        self.draw_line(0, self.ylim, -self.xlim, 0, colour="yellow")
        self.draw_line(-self.xlim, 0, 0, -self.ylim, colour="yellow")
        self.draw_line(self.xlim, 0, 0, -self.ylim, colour="yellow")
        self.axes()

# A = FancyGraphs(500, 500, 5, 5, "penrose.svg")
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
# A = FancyGraphs(500,500,5,5,"dense.svg", origin=[3,0])
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

# A = FancyGraphs(1400,1400,5,5,"Dipole.svg")
# #A.VectorField(func, gridint=5,  arrow_scale=2, stroke_width=2, stroke="white", arrow = True, constcolour=False,constLength=True)
# A.VectorField(func, gridint=25,  arrow_scale=1.5, tail_length=0.5, arrow = True, constLength=True, initColour=hex_to_vec('#000099'), endColour=hex_to_vec('#ff99cc'))
# A.save()

# A = FancyGraphs(500,500,5,5,"histo.svg", origin=[3,0])
# A.bg(colour="black")
# A.histogram([3,2,3,1,10])
# A.save()
# A.display()
