import math
from svgwtr import *
from colour import *
import numpy as np

'''
TODO:
    : Create Axes labels
    : Create Legend

'''


class Graph:
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], fullsvg = True):
        self.svg = SVG(name, width, height, fullsvg=fullsvg)
        self.eps = xlim / 2000
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.origin = np.array(origin)

    def tranx(self, x):
        if x != None:
            return + round((self.width / (2 * self.xlim)) * (x + self.origin[0]) + self.width/2, 2)
        else:
            return None

    def trany(self, y):
        if y != None:
            return round(-(self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height/2, 2)
        else:
            return None


    def bg(self, colour):
        self.svg.draw_rect(self.tranx(-self.origin[0]),self.trany(-self.origin[1]), self.width, self.height, colour)

    def axes(self, colour="black", strokewidth=2.5):
        ox = self.origin[0]
        oy = self.origin[1]
        scale = strokewidth * self.height * 0.001

        self.svg.draw_line(self.tranx(-self.xlim + ox), self.trany(0) , self.tranx(self.xlim -ox), self.trany(0), stroke=colour,
                           strokewidth=strokewidth)
        self.svg.draw_line(self.tranx(0), self.trany(self.ylim - oy), self.tranx(0), self.trany(-self.ylim + oy), stroke=colour,
                           strokewidth=strokewidth)
        if (self.origin == [-self.xlim, -self.ylim]).all:
            self.svg.draw_arrowhead(self.tranx(self.xlim - ox) - 3 * scale, self.trany(0), scale, math.pi / 2,
                                    colour=colour)  # E
            self.svg.draw_arrowhead(self.tranx(0), self.trany(self.ylim - oy) + 3 * scale, scale, 0, colour=colour)  # N
        elif (self.origin == [-self.xlim, self.ylim]).all:
            self.svg.draw_arrowhead(self.tranx(0), self.trany(-self.ylim - oy) - 3 * scale, scale, math.pi, colour=colour) # S
            self.svg.draw_arrowhead(self.tranx(self.xlim-ox) - 3 * scale, self.trany(0), scale, math.pi / 2, colour=colour) # E
        elif (self.origin == [self.xlim, -self.ylim]).all:
            self.svg.draw_arrowhead(self.tranx(0), self.trany(self.ylim-oy) + 3 * scale, scale, 0, colour=colour) # N
            self.svg.draw_arrowhead(self.tranx(-self.xlim - ox) + 3 * scale, self.trany(0), scale, - math.pi / 2, colour=colour) # W
        elif (self.origin == [self.xlim, self.ylim]).all:
            self.svg.draw_arrowhead(self.tranx(0), self.trany(-self.ylim - oy) - 3 * scale, scale, math.pi, colour=colour)  # S
            self.svg.draw_arrowhead(self.tranx(-self.xlim - ox) + 3 * scale, self.trany(0), scale, - math.pi / 2, colour=colour)  # W
        else:
            self.svg.draw_arrowhead(self.tranx(0), self.trany(-self.ylim - oy) - 3 * scale, scale, math.pi, colour=colour) # S
            self.svg.draw_arrowhead(self.tranx(-self.xlim - ox) + 3 * scale, self.trany(0), scale, - math.pi / 2, colour=colour) # W
            self.svg.draw_arrowhead(self.tranx(self.xlim-ox) - 3 * scale, self.trany(0), scale, math.pi / 2, colour=colour) # E
            self.svg.draw_arrowhead(self.tranx(0), self.trany(self.ylim-oy) + 3 * scale, scale, 0, colour=colour) # N

    def grid(self, grids=[10, 10], colour="black", strokewidth=1, opac=0.4):
        a = self.tranx(self.origin[0]) * 0
        b = self.trany(self.origin[1]) * 0
        for i in range(grids[0]):
            self.svg.draw_line((i / grids[0]) * (self.width) + a, b, (i / grids[0]) * (self.width) + a, self.height + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)
        for i in range(grids[1]):
            self.svg.draw_line(a, (i / grids[0]) * (self.height) + b, self.width + a,
                               (i / grids[0]) * (self.height) + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)

    def text(self, x, y, text, fontsize=20, colour="white", fontweight="normal", fontstyle="normal", font="14", opac=1):
        self.svg.canvas += '<text x="%s" y="%s" fill="%s" font-size="%s" opacity="%s" > %s </text>' % (
            self.tranx(x), self.trany(y), colour, fontsize, opac, text)

    def ticks(self, stroke="white", strokewidth=1, tick=10, markers=False, fontsize=8):
        tickx = round(tick * 2)
        ticky = round(tick * 2)
        kx = self.width / 200
        ky = self.height / 200
        dx = self.width / tickx
        dy = self.height / ticky
        ox = self.xlim * 2 / tickx
        oy = self.ylim * 2 / ticky
        a = self.origin[0] * (self.width / (2 * self.xlim))
        b = -self.origin[1] * (self.height / (2 * self.ylim))
        p = 1
        for i in range(0, tickx):
            self.svg.draw_line(dx * i, -ky + self.trany(0) + b, dx * i, ky + self.height / 2 + b,
                               stroke=stroke, strokewidth=strokewidth)
            if markers:
                if i - self.xlim != 0:
                    self.text((i - self.xlim - fontsize / (p * dx)) * ox, 0 + fontsize / dy,
                              str(round((i - self.xlim - self.origin[0]) * ox, 1)),
                              fontsize=fontsize, colour="white", opac=0.3)

        for i in range(1, ticky):
            self.svg.draw_line(-kx + self.width / 2 + a, dy * i, kx + self.width / 2 + a, dy * i, stroke=stroke,
                               strokewidth=strokewidth)
            if markers:
                if i - self.ylim != 0:
                    self.text(0 + fontsize / dx, (i - self.ylim - fontsize / (p * dy)) * oy,
                              str(round((i - self.ylim + self.origin[1]) * oy, 1)),
                              fontsize=fontsize, colour="white", opac=0.3)

    def arrow(self, x1, y1, x2, y2, scale, stroke, strokewidth):
        self.svg.draw_arrow(x1, y1, x2, y2, scale, stroke=stroke, strokewidth=strokewidth)

    def graph(self, func, colour="red", strokewidth=1.5, opac=1, n0=1200):
        eps = self.xlim / n0
        X = [self.tranx(i * eps) for i in range(-n0, n0 + 1)]
        Y = [self.trany(func(i * eps)) for i in range(-n0, n0 + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def graph_points(self, X, Y, colour="red", strokewidth=1, opac=1):
        X1 = [self.tranx(x) for x in X]
        Y1 = [self.trany(y) for y in Y]
        self.svg.draw_polyline(X1, Y1, colour=colour, strokewidth=strokewidth, opac=opac)

    def scatter(self, X, Y, s=1, colour="white", opac=1):
        if len(X) != len(Y):
            print("Data sets are misaligned!")
        # s = (self.width + self.height) / 500
        for i in range(len(X)):
            self.svg.draw_circ(self.tranx(-X[i]), self.trany(Y[i]), s, fill=colour, stroke=colour,
                               strokewidth=0, opac=opac)

    def param_label(self, x, y, label, s, stroke="white", strokewidth=12):
        text = "%s = %s" % (label, s)
        self.text(x, y, text, strokewidth=strokewidth, stroke=stroke)

    def show(self):
        self.svg.save()
        self.svg.canvas = ""

    def embed_latex(self, expr, x, y, width=200, height=200, colour="white", size=45):
        A = LaText("expr.png", 0.5, 0.5, expr, colour=colour, size=size)
        A.save()
        self.svg.embed_image(self.tranx(x) - width / 2, self.trany(y) - height / 2, width=width,
                             height=height, href=os.getcwd() + "/expr.png")

    def embed_latex_anim(self, expr, x, y, width=200, height=200, colour="white", size=45):
        A = LaText(os.getcwd() + "/Plots/expr.png", 0.5, 0.5, expr, colour=colour, size=size)
        A.save()
        self.svg.embed_image(self.tranx(x) - width / 2, self.trany(y) - height / 2, width=width,
                             height=height, href=os.getcwd() + "/Plots/expr.png")



'''

def g(s):
    def f(x):
        return x**4 + s
    return f
g1 = g(0)
g2 = g(1)
g3 = g(2)
g4 = g(3)

g = Graph(800, 800, 5, 5, "50sd.svg", origin=[-2.,-2.])
g.bg("black")
g.axes(colour="white")
g.ticks(markers=True)
#g.grid(grids=[10,10], colour="white", strokewidth=0.5, opac=0.5)
#g.ticks(markers=True, tick=5)

#g.graph(f, "blue")
# g.embed_latex("$x^2+y^2=1$", 0, 0)
#dt = math.pi * 2 / 100
#g.svg.draw_arrow(23, 200, 34, 44, stroke="white")m
g.graph(g1)
g.graph(g2)
g.show()


'''
'''
def f(x):
    return math.sin(x) + 1

A = Graph(1000,1000,5,5,"c1.svg", origin=[0,0])
A.bg(colour="black")
A.axes(colour="yellow")
A.graph(math.sin)
A.grid(colour="white")
A.show()

A = Graph(1000,1000,5,5,"c2.svg", origin=[0,0])
A.bg(colour="black")
A.axes(colour="yellow")
A.graph1(math.sin)
A.grid(colour="white")
A.show()
'''
