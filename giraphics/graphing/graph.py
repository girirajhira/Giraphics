from giraphics.svg.svgkit import *
from giraphics.utilities.latext import *
from giraphics.utilities.mathtext import *
from giraphics.utilities.convert import *
from IPython.display import SVG as IPSVG
from IPython.display import Image
import numpy as np
import webbrowser
import os
import platform
# from numba import njit, jit


class Graph:
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                 transform="none", grouped=False):
        """
        Initial
        :param width: int
            svg width
        :param height: int
            svg height
        :param xlim: float
            sets horizontal axis limits half
        :param ylim: float
            sets vertical axis limits
        :param name:
            names of the svg file
        :param origin: list (of length 2)
            sets the position of the origin in standard units
        :param transform: bool
            sets transformation rules for the svg
        :param grouped: bool
            whether the svg should be grouped
        """
        self.svg = SVG(name, width, height, transform=transform, grouped=grouped)
        self.name = name
        self.eps = xlim / 2000
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.origin = np.array(origin)
        self.xscale = width / (2 * xlim)
        self.yscale = height / (2 * ylim)
        self.TexLoader = []
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
        :param x: float
            x coordinate in standard units
        :returns: float
            return the x coordinate in y
        """
        if x is not None:
            return + round((self.width / (2 * self.xlim)) * (x + self.origin[0]) + self.width / 2, 2)
            return - round((self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height / 2, 2)

        else:
            return None
    def trany(self, y):
        """
        converts the y coordinate to svg coordinate
        :param y:
        :return: svg coordinate
        """
        if y is not None:
            return round(-(self.height / (2 * self.ylim)) * (y + self.origin[1]) + self.height / 2, 2)
        else:
            return None

    def bg(self, colour="black"):
        """
        Sets the background colour
        :param colour: colour name or in Hexadecimal
        :return: Nonef
        """
        self.svg.draw_rect(self.tranx(-self.origin[0]), self.trany(-self.origin[1]), self.width, self.height, colour)

    def axes(self, colour="yellow", strokewidth=1, arrows=False):
        """
        Constructs x and y axes

        :param colour: string
            colour of the axes
        :param strokewidth: float
            thickness of the axes
        :param arrows: bool
            whether arrows are to required
        :return: None
        """
        ox = self.origin[0]
        oy = self.origin[1]
        scale = strokewidth * self.height * 0.001 / 2

        self.svg.draw_line(self.tranx(-self.xlim - ox), self.trany(0), self.tranx(self.xlim - ox), self.trany(0),
                           stroke=colour,
                           strokewidth=strokewidth)
        self.svg.draw_line(self.tranx(0), self.trany(self.ylim - oy), self.tranx(0), self.trany(-self.ylim - oy),
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

    # Todo: Fix Grid, origin changes

    def grid(self, grid_int=None, colour="#A7A7A7", grid_multiplier=1, strokewidth=0.7, opac=0.5):
        """
        Creates a grid
        :param grids: list (length 2)
        the number of gridlines horizontally and vertically
        :param colour: string
            set the colour of the grid
        :param strokewidth: float
            sets the thickness of the grid
        :param opac: float (0-1)
            sets the opacity of the grid
        :return: None
        """
        if grid_int is None:
            grid_int = []
            if self.xlim < 5:
                grid_int.append(round(2 * self.xlim * grid_multiplier))
            else:
                grid_int.append(2 * self.xlim)
            if self.ylim < 5:
                grid_int.append(round(2 * self.ylim * grid_multiplier))
            else:
                grid_int.append(2 * self.ylim)

        a = self.tranx(self.origin[0]) * 0
        b = self.trany(self.origin[1]) * 0
        for i in range(2 * grid_int[0]):
            self.svg.draw_line((i / grid_int[0]) * self.xscale * self.xlim + a, b,
                               (i / grid_int[0]) * self.xscale * self.xlim + a, self.height + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)
        for i in range(2 * grid_int[1]):
            self.svg.draw_line(a, (i / grid_int[1]) * self.yscale * self.ylim + b, self.width + a,
                               (i / grid_int[1]) * self.yscale * self.ylim + b,
                               stroke=colour, strokewidth=strokewidth, opacity=opac)

    # def text(self, x, y, text, fontsize=20, colour="white", rotation=0,
    #          font="14", opac=1):
    #     self.svg.canvas += '<text x="%s" y="%s"  style=" font-family:Arial" fill="%s" font-size="%s" opacity="%s"  transform="rotate(%s)"> %s </text>' % (
    #     self.tranx(x), self.trany(y), colour, fontsize, opac, rotation, text)

    def text(self, x, y, text, fontsize=20, colour="white", rotation=0,
             font="14", opac=1):
        """
        Draws specified text at the given coordinates (in standard units)
        :param x: float
            x coordinate
        :param y: float
            y coordinate
        :param text: string
            text to be drawn
        :param fontsize: float
            font size
        :param colour:
            colour of the text
        :param rotation: float
            specifies the how the text should be rotated
        :param font: string
            specifies the font to be used
        :param opac: float (0-1)
        :return: None
        """
        self.svg.canvas += '<text x="%s" y="%s"  font-family="Recursive" fill="%s" font-size="%s" alignment-baseline="middle" text-anchor="middle" opacity="%s"  transform="rotate(%s,%s,%s)"> %s </text>\n' % (
            self.tranx(x), self.trany(y), colour, fontsize, opac, rotation, self.tranx(x), self.trany(y), text)

    def math_text(self, expression, x, y, colour="White", scale=4):
        math_to_svg(expression, os.getcwd() + "/temp.txt")
        with open("temp.txt", 'r') as file:
            code = file.read()
        os.remove(os.getcwd() + "/temp.txt")
        dx = len(expression) * scale
        dy = 9 * scale
        self.svg.canvas += '\n <g transform-origin="bottome" transform="translate(' + str(
            self.tranx(x) - dx) + ' ' + str(self.trany(y) - dy) + '),' + 'scale(' + str(scale) + ',' + str(
            scale) + ')' + ' ">'
        self.svg.canvas += code.replace('currentColor', colour).replace('8.781ex', str(scale))
        self.svg.canvas += '</g> \n'

    def add_math_text(self, expr, x, y, colour="white", scale=4):
        self.TexLoader.append([expr, x, y, colour, scale])

    def ticks(self, colour="yellow", strokewidth=1, markers=False, fontsize=8):
        """
        Adds ticks to x and y axes
        :param colour: string
        :param strokewidth: float
        :param tick: int
            the number of ticks
        :param markers: bool
        :param fontsize: float
        :return: None
        """
        tickx, ticky = round(2 * self.xlim), round(2 * self.ylim)
        dx = self.width / tickx
        dy = self.height / ticky
        ox = self.xlim * 2 / tickx
        oy = self.ylim * 2 / ticky
        # x axis
        for i in range(1, tickx):
            self.svg.draw_line(dx * i, self.trany(fontsize / (3 * dy)), dx * i, self.trany(-fontsize / (3 * dy)),
                               stroke=colour, strokewidth=strokewidth)
            if markers:
                if i - self.xlim != self.origin[0]:
                    self.text((i - self.xlim - self.origin[0]) * ox, fontsize / dy,
                              str((round((i - self.xlim - self.origin[0]) * ox, 2))),
                              fontsize=fontsize, colour=colour, opac=0.6)

        # y axis
        for i in range(1, ticky):
            self.svg.draw_line(self.tranx(-fontsize / (2 * dx)), dy * i, self.tranx(fontsize / (2 * dx)), dy * i,
                               stroke=colour,
                               strokewidth=strokewidth)
            if markers:
                if i - self.ylim != self.origin[1]:
                    self.text(fontsize / dx, (i - self.ylim - self.origin[1]) * oy,
                              str((round((i - self.ylim - self.origin[1]) * oy, 2))),
                              fontsize=fontsize, colour=colour, opac=0.6)

    def arrow(self, x1, y1, x2, y2, scale, colour, strokewidth):
        """
        Draws a line from (x1, y1) to (x2, y2)
        :param x1: float
            Start x coordinate
        :param y1: float
            Start y coordinate
        :param x2: float
            End x coordinate
        :param y2: float
            End y coordinate
        :param scale: float
            Size of the arrow
        :param : string
            Colour of the arrow
        :param strokewidth: float
            Width of arrow tail
        :return: None
        """
        self.svg.draw_arrow(x1, y1, x2, y2, scale, stroke=colour, strokewidth=strokewidth)


    def plot(self, func, colour="red", strokewidth=1.5, opac=1, n=500):
        """
        Graphs the given function
        :param func: function
            function to be plotted
        :param colour: string
            colour of the curve
        :param strokewidth: float
            width of curve
        :param opac: string
            opacity of the curve
        :param n: int
            Number of points used in the curve
        :return: None
        """
        eps = self.xlim / n
        X = [self.tranx(i * eps - self.origin[0]) for i in range(-n, n + 1)]
        Y = [self.trany(func(i * eps - self.origin[0])) for i in range(-n, n + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def graph_polar(self, func, colour="red", strokewidth=1.5, opac=1, n=500):
        """
        Graphs the given function
        :param func: function
            function to be plotted
        :param colour: string
            colour of the curve
        :param strokewidth: float
            width of curve
        :param opac: string
            opacity of the curve
        :param n: int
            Number of points used in the curve
        :return: None
        """

        eps = self.xlim / n
        X = [self.tranx(i * eps - self.origin[0]) for i in range(-n, n + 1)]
        Y = [self.trany(func(i * eps - self.origin[0])) for i in range(-n, n + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def area(self, func, limits, colour="red", area_colour="orange", strokewidth=0, opac=1, n=500):
        eps = (limits[1] - limits[0]) / n
        X = [self.tranx(i * eps + limits[0]) for i in range(n + 1)]
        X.append(self.tranx(limits[1]))  # Ensure uniform area
        Y = [self.trany(func(i * eps + limits[0])) for i in range(n + 1)]
        Y.append(self.trany(func(limits[0])))  # Ensure uniform area
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac, fill=area_colour)

    def dotted_plot(self, func, colour="red", strokewidth=1.5, opac=1, n=500):
        """
           Graphs the given function width a dotted line
           :param func: function
               function to be plotted
           :param colour: string
               colour of the curve
           :param strokewidth: float
               width of curve
           :param opac: string
               opacity of the curve
           :param n: int
               Number of points used in the curve
           :return: None
           """
        eps = self.xlim / n
        X = [self.tranx(i * eps - self.origin[0]) if i % 15 > 7 else None for i in range(-n, n + 1)]
        Y = [self.trany(func(i * eps - self.origin[0])) for i in range(-n, n + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def plot_points(self, X, Y, colour="red", strokewidth=1, opac=1):
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
        :param X: list
        :param Y: list
        :param s: float
        :param colour: string
        :param opac: float (0-1)
        :return: None
        """
        if len(X) != len(Y):
            print("Data sets are misaligned!")
        for i in range(len(X)):
            self.svg.draw_circ(self.tranx(-X[i]), self.trany(Y[i]), s, fill=colour, stroke=colour,
                               strokewidth=0, opac=opac)

    def param_label(self, x, y, label, s, stroke="white", strokewidth=12):
        text = "%s = %s" % (label, s)
        self.text(x, y, text, strokewidth=strokewidth, stroke=stroke)

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

    def draw_arrow(self, x1, y1, x2, y2, scale=1, colour="black", strokewidth=1):
        self.svg.draw_arrow(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=colour,
                            strokewidth=strokewidth)

    def draw_double_arrow(self, x1, y1, x2, y2, scale=1, colour="black", strokewidth=1):
        self.svg.draw_arrow(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=colour,
                            strokewidth=strokewidth)
        self.svg.draw_arrow(self.tranx(x2), self.trany(y2), self.tranx(x1), self.trany(y1), scale, stroke=colour,
                            strokewidth=strokewidth)


    def draw_circle(self, x, y, r, fill="none", colour="black", strokewidth=1):
        self.svg.draw_circ(self.tranx(x), self.trany(y), self.xscale * r, fill=fill, stroke=colour,
                           strokewidth=strokewidth)

    def draw_line(self, x1, y1, x2, y2, colour="black", strokewidth=1, opacity=1, cap="butt"):
        self.svg.draw_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), stroke=colour,
                           strokewidth=strokewidth, opacity=opacity, cap=cap)

    def draw_rect(self, x, y, width, height, fill, colour="black", strokewidth=1, opac=1):
        self.svg.draw_rect(self.tranx(x), self.trany(y), abs(self.xscale * (width)),
                           self.yscale * height, fill, stroke=colour, strokewidth=strokewidth, opacity=opac)

    def draw_line(self, x1, y1, x2, y2, marker="*", colour="black", strokewidth=1, opacity=1, cap="butt",
                  segments=20, dotted=False):
        if not dotted:
            self.svg.draw_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), stroke=colour,
                               strokewidth=strokewidth, opacity=opacity, cap=cap)
        else:
            self.svg.draw_dotted_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), marker=marker,
                                      stroke=colour,
                                      strokewidth=strokewidth, opacity=opacity, cap=cap, segments=segments)

    def point(self, x, y, s=1, colour="white"):
        self.draw_circle(x, y, 15 * s / self.width, fill=colour, strokewidth=0)

    def save(self):
        if len(self.TexLoader) != 0:
            for t in self.TexLoader:
                self.math_text(t[0], t[1], t[2], colour=t[3], scale=t[4])
        """
        Saves the plot and clears the svg.canvas
        """
        self.svg.save()
        self.svg.canvas = ""

    def jupyter_display(self, raster=False):
        self.save()
        print(os.getcwd())
        if not raster:
            return IPSVG(filename=os.getcwd()+'/'+self.name)
        else:
            convert_image(self.name+'.svg', self.name+'.png')
            return Image(filename=self.name+'.png')

    def display(self):
        """
        Displays the plot in a webbrowser
        """
        if platform.system() == "Darwin":
            webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(os.getcwd() + "/" + self.name)
        elif platform.system() == "Windows":
            webbrowser.get('chrome').open('file://' + os.getcwd() + "/" + self.name)
        else:
            print("OS error, your os is ", platform.system())


"""
def func(x):
    return 0.04 * x ** 2 * math.sin(6 * x) + 5

def sq(x):
    return x * x

f = Figure(600, 500, 15, 10, "fig.svg", origin=[-0, -0])
f.plot(func)
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

#g.plot(f, "blue")
# g.embed_latex("$x^2+y^2=1$", 0, 0)
#dt = math.pi * 2 / 100
#g.svg.draw_arrow(23, 200, 34, 44, stroke="white")m
g.plot(g1)
g.plot(g2)
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
        A.plot(f(i))
    A.grid(colour="white")
    A.save()
    A.display()

'''

#
# def f(x):
#     return x
#
#
# def g(x):
#     return x * x
#
#
# A = Graph(400, 400, 5, 5, 'svg.svg', origin=[-5, -5])
# A.bg()
# A.axes()
# A.grid()
# A.ticks(markers=True)
# A.plot(f)
# A.plot(g)
#
# A.draw_dotted_line(0, 0, 6, 7, stroke="white", marker=".")
# A.save()
# A.display()
#
#
# g = Graph(1000,1000,3,3,'giraphics.svg')
# g.bg(colour="black")
# g.math_text('GiraFix', 0,0)
# g.save()
# # g.display()
# G = Graph(1000,1000,10,10,'ss')
#
# from giraphics.utilities.timer import Timer
#
#
# t = Timer()
# t.start()
# G.tranx1(100)
# t.stop()