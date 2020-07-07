import math
from svgwtr import *
from colour import *
from latext import *
import numpy as np
import webbrowser
import os
import platform

class Graph:
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], full_svg=True, theme="dark",
                 transform="none", grouped=False):
        """
        :param width: specifies svg width
        :param height: specifies svg height
        :param xlim: sets horizontal axis limits
        :param ylim: sets vertical axis limits
        :param name: names of the svg file
        :param origin: sets the position of the origin in standard units
        :param full_svg: Soon to be useless
        :param theme:
        :param transform: sets transform rules for the svg
        :param grouped: whether the svg should be grouped
        """
        self.svg = SVG(name, width, height, fullsvg=full_svg, transform=transform, grouped=grouped)
        self.name = name
        self.eps = xlim / 2000
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.origin = np.array(origin)
        self.xscale = width / (2 * xlim)
        self.yscale = height / (2 * ylim)

        if theme == "dark":
            self.theme = {
                'background': 'black',
                'primary': 'yellow',
                'secondary': 'white'
            }
        else:
            self.theme = {
                'background': 'white',
                'primary': 'black',
                'secondary': 'black'
            }

    def tranx(self, x):
        """
        converts the x coordinate to svg coordinate
        """
        if x != None:
            return + round((self.width / (2 * self.xlim)) * (x + self.origin[0]) + self.width / 2, 2)
        else:
            return None

    def trany(self, y):
        """
        converts the y coordinate to svg coordinate
        :param y:
        :return: svg coordinat
        """
        if y != None:
            return round(-(self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height / 2, 2)
        else:
            return None

    def bg(self, colour="black"):
        """
        Sets the background colour
        :param colour: colour name or in Hexadecimal
        :return: None
        """
        self.svg.draw_rect(self.tranx(-self.origin[0]), self.trany(-self.origin[1]), self.width, self.height, colour)

    def axes(self, colour="yellow", strokewidth=1, arrows=False):
        """
        Creates x and y axes
        :param colour: colour of the axes
        :param strokewidth: thickness of the axes
        :param arrows: whether arrows are to required
        :return:
        """
        ox = self.origin[0]
        oy = self.origin[1]
        scale = strokewidth * self.height * 0.001 / 2

        self.svg.draw_line(self.tranx(-self.xlim + ox), self.trany(0), self.tranx(self.xlim - ox), self.trany(0),
                           stroke=colour,
                           strokewidth=strokewidth)
        self.svg.draw_line(self.tranx(0), self.trany(self.ylim + oy), self.tranx(0), self.trany(-self.ylim - oy),
                           stroke=colour,
                           strokewidth=strokewidth)
        if arrows:
            self.svg.draw_arrowhead2(self.tranx(self.xlim - ox) - 3 * scale, self.trany(0), scale, math.pi / 2,
                                     colour=colour)  # E
            self.svg.draw_arrowhead2(self.tranx(0), self.trany(self.ylim - oy) + 3 * scale, scale, 0,
                                     colour=colour)  # N
            self.svg.draw_arrowhead2(self.tranx(0), self.trany(-self.ylim - oy) - 3 * scale, scale, math.pi,
                                     colour=colour)  # S
            self.svg.draw_arrowhead2(self.tranx(-self.xlim - ox) + 3 * scale, self.trany(0), scale, - math.pi / 2,
                                     colour=colour)  # W

    def grid(self, grids=[20, 20], colour="white", strokewidth=0.7, opac=0.2):
        """
        Creates a grid
        :param grids: the number of gridlines horizontally and vertically
        :param colour:
        :param strokewidth:
        :param opac:
        :return:
        """
        a = self.tranx(self.origin[0]) * 0
        b = self.trany(self.origin[1]) * 0
        for i in range(grids[0]):
            self.svg.draw_line((i / grids[0]) * (self.width) + a, b, (i / grids[0]) * (self.width) + a, self.height + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)
        for i in range(grids[1]):
            self.svg.draw_line(a, (i / grids[0]) * (self.height) + b, self.width + a,
                               (i / grids[0]) * (self.height) + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)

    def grid2(self, grids=[20, 20], colour="white", strokewidth=0.7, opac=0.2):
        ox = self.width * self.origin[0] / (2 * self.xlim)
        oy = self.origin[1]
        for i in range(grids[0]):
            self.svg.draw_line((i / grids[0]) * (self.width), ox, (i / grids[0]) * (self.width) + ox, self.height + oy,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)

        for i in range(grids[1]):
            self.svg.draw_line(self.origin[0], (i / grids[0]) * (self.height) + oy, self.width + ox,
                               (i / grids[0]) * (self.height) + oy,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)

    def text(self, x, y, text, fontsize=20, colour="white", rotation=0,
             font="14", opac=1):
        self.svg.canvas += '<text x="%s" y="%s"  style=" font-family:Arial" fill="%s" font-size="%s" opacity="%s"  transform="rotate(%s)"> %s </text>' % (
        self.tranx(x), self.trany(y), colour, fontsize, opac, rotation, text)

    def ticks(self, stroke="yellow", strokewidth=1, tick=10, markers=False, fontsize=8):
        tickx = round(tick * 2)
        ticky = round(tick * 2)
        kx = self.width / 300
        ky = self.height / 300
        dx = self.width / tickx
        dy = self.height / ticky
        ox = self.xlim * 2 / tickx
        oy = self.ylim * 2 / ticky
        a = self.origin[0] * (self.width / (2 * self.xlim))
        b = -self.origin[1] * (self.height / (2 * self.ylim))
        p = 2
        for i in range(1, tickx):
            self.svg.draw_line(dx * i, -ky + self.trany(0) + b, dx * i, ky + self.height / 2 + b,
                               stroke=stroke, strokewidth=strokewidth)
            if markers:
                if i - self.xlim != 0:
                    self.text((i - self.xlim - fontsize / (p * dx)) * ox, 0 + fontsize / dy,
                              str(int(round((i - self.xlim - self.origin[0]) * ox, 1))),
                              fontsize=fontsize, colour=stroke, opac=0.6)

        for i in range(1, ticky):
            self.svg.draw_line(-kx + self.width / 2 + a, dy * i, kx + self.width / 2 + a, dy * i, stroke=stroke,
                               strokewidth=strokewidth)
            if markers:
                if i - self.ylim != 0:
                    self.text(0 + fontsize / dx, (i - self.ylim - fontsize / (p * dy)) * oy,
                              str(int(round((i - self.ylim + self.origin[1]) * oy))),
                              fontsize=fontsize, colour=stroke, opac=0.6)

    def arrow(self, x1, y1, x2, y2, scale, stroke, strokewidth):
        self.svg.draw_arrow(x1, y1, x2, y2, scale, stroke=stroke, strokewidth=strokewidth)

    def graph(self, func, colour="red", strokewidth=1.5, opac=1, n0=1200):
        """
        Graphs the inputted function
        :param func:
        :param colour:
        :param strokewidth:
        :param opac:
        :param n0:
        :return:
        """
        eps = self.xlim / n0
        X = [self.tranx(i * eps - self.origin[0]) for i in range(-n0, n0 + 1)]
        Y = [self.trany(func(i * eps - self.origin[0]) + self.origin[1]) for i in range(-n0, n0 + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def graph_points(self, X, Y, colour="red", strokewidth=1, opac=1):
        """
        Graphs the inputted points
        :param X:
        :param Y:
        :param colour:
        :param strokewidth:
        :param opac:
        :return:
        """
        X1 = [self.tranx(x) for x in X]
        Y1 = [self.trany(y) for y in Y]
        self.svg.draw_polyline(X1, Y1, colour=colour, strokewidth=strokewidth, opac=opac)

    def scatter(self, X, Y, s=1, colour="white", opac=1):
        """
        Scatter plots the points X,Y
        :param X:
        :param Y:
        :param s:
        :param colour:
        :param opac:
        :return:
        """
        if len(X) != len(Y):
            print("Data sets are misaligned!")
        for i in range(len(X)):
            self.svg.draw_circ(self.tranx(-X[i]), self.trany(Y[i]), s, fill=colour, stroke=colour,
                               strokewidth=0, opac=opac)

    def param_label(self, x, y, label, s, stroke="white", strokewidth=12):
        text = "%s = %s" % (label, s)
        self.text(x, y, text, strokewidth=strokewidth, stroke=stroke)

    def include_model(self, S):
        self.svg.canvas += '\n' + S.svg.canvas

    def save(self):
        """
        Saves the graph and clears the svg.canvas
        """
        self.svg.save()
        self.svg.canvas = ""

    def display(self):
        """
        Displays the graph in a webbrowser
        """
        print(platform.system())
        if platform.system() == "Darwin":
            webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(os.getcwd() + "/" + self.name)
        elif platform.system() == "Windows":
            webbrowser.get('chrome').open('file://' + os.getcwd() + "/" + self.name)
        else:
            print("OS error, your os is ", platform.system())

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

    # Construction

    def draw_arrow(self, x1, y1, x2, y2, scale=1, stroke="black", strokewidth=1):
        self.svg.draw_arrow(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=stroke,
                            strokewidth=strokewidth)

    def draw_circle(self, x, y, r, fill="none", stroke="black", strokewidth=1):
        self.svg.draw_circ(self.tranx(x), self.trany(y), self.xscale * r, fill=fill, stroke=stroke,
                           strokewidth=strokewidth)

    def draw_line(self, x1, y1, x2, y2, stroke="black", strokewidth=1, opacity=1, cap="butt"):
        self.svg.draw_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), stroke=stroke,
                           strokewidth=strokewidth, opacity=opacity, cap=cap)

    def draw_rect(self, x, y, width, height, fill, stroke="black", strokewidth=1):
        self.svg.draw_rect(self.tranx(x), self.trany(y), abs(self.xscale * (width)),
                           self.yscale * height, fill, stroke=stroke, strokewidth=strokewidth)

    def draw_dotted_line(self, x1, y1, x2, y2, marker="*", stroke="black", strokewidth=1, opacity=1, cap="butt",
                         segments=20):
        self.svg.draw_dotted_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), marker=marker,
                                  stroke=stroke,
                                  strokewidth=strokewidth, opacity=opacity, cap=cap, segments=segments)

    def point(self, x, y, s=1, colour="white"):
        self.draw_circ(x, y, s, fill=colour)


class Model(Graph):
    def __init__(self, width, height, xlim, ylim, name, origin=[0, 0], theme="dark"):
        self.svg = SVG('', width, height, fullsvg=False)
        self.eps = xlim / 2000
        self.name = name
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.origin = np.array(origin)
        if theme == "dark":
            self.theme = {
                'background': 'black',
                'primary': 'yellow',
                'secondary': 'white'
            }
        else:
            self.theme = {
                'background': 'white',
                'primary': 'black',
                'secondary': 'black'
            }

    def show(self):
        svg = SVG(self.name, self.width, self.height, fullsvg=True)
        svg.canvas += self.svg.canvas
        svg.save()
        self.display()

    def clear(self):
        self.svg.canvas = ""


"""
def func(x):
    return 0.04 * x ** 2 * math.sin(6 * x) + 5


def sq(x):
    return x * x


f = Figure(600, 500, 15, 10, "fig.svg", origin=[-0, -0])
f.graph(func)
f.axes(colour="black")
f.scatter([0.1 * i for i in range(-1500, 1500)], [sq(0.1 * i) for i in range(-1500, 1500)], colour="black")
f.save()
f.display()
"""
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
#g.grid(grids=[10,10], colour="white", stroke_width=0.5, opac=0.5)
#g.ticks(markers=True, tick=5)

#g.graph(f, "blue")
# g.embed_latex("$x^2+y^2=1$", 0, 0)
#dt = math.pi * 2 / 100
#g.svg.draw_arrow(23, 200, 34, 44, stroke="white")m
g.graph(g1)
g.graph(g2)
g.save()


'''
'''
def f(s):
    def k(x):
        return math.sin(x) + s -5
    return k

if __name__ == "__main__":
    A = Graph(1000,1000,5,5,"c1.svg", origin=[0,0])
    A.bg(colour="black")
    A.axes(colour="yellow")
    for i in range(12):
        A.graph(f(i))
    A.grid(colour="white")
    A.save()
    A.display()

'''

# def f(x):
#     return 0.1*(x-1)*(x+3)*(x+3/2)*(x-1/2)
# A = Graph(1000, 1000, 10, 10, 'svg.svg', origin=[0,0])
# A.bg()
# A.axes()
# A.grid()
# A.ticks(markers=True)
# A.graph(f)
# A.draw_dotted_line(0, 0, 6, 7, stroke="white", marker=".")
# A.save()
# A.display()
#

def func(x):
    return 0.04 * x ** 2 * math.sin(6 * x) - 5


def sq(x):
    return x * x

f = Graph(600, 500, 15, 10, "sggi.svg", origin=[-2, -0])
f.bg()
f.graph(func, colour="red")
f.axes(colour="white")
f.grid()
f.ticks()
f.scatter([0.1 * i for i in range(-1500, 1500)], [sq(0.1 * i) for i in range(-1500, 1500)], colour="black")
f.save()
f.display()
