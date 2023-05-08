from giraphics.svg.svgkit import *
# from giraphics.utilities.latext import *
# from giraphics.utilities.mathtext import *
from giraphics.svg.morph2 import *
from giraphics.utilities.latex2 import latex_expression
from giraphics.utilities.convert import *
from giraphics.utilities.latex_svg_decoder import *
from IPython.display import SVG as IPSVG
from IPython.display import Image
import numpy as np
from math import sqrt
import webbrowser
import os
import platform


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
        self.height = height
        self.width = width
        self.xlim = xlim
        self.transform = transform
        self.ylim = ylim
        self.origin = np.array(origin)
        self.xscale = width / (2 * xlim)
        self.yscale = height / (2 * ylim)
        self.nscale = sqrt(self.xscale ** 2 + self.yscale ** 2) / sqrt(2) / 30
        self.insets = []
        self.latex_history = {}
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
        strokewidth = strokewidth * self.nscale
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
        strokewidth = strokewidth * self.nscale
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

    def text(self, x, y, text, fontsize=12, colour="white", rotation=0, opac=1, fontfamily='sans-serif'):
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
        fontsize *= self.nscale
        self.svg.canvas += f'<text x="{self.tranx(x)}" y="{self.trany(y)}"  font-family="{fontfamily}" fill="{colour}" font-size="{fontsize}" alignment-baseline="middle" text-anchor="middle" color="{colour}" opacity="{opac}"  transform="rotate({rotation},{self.tranx(x)},{self.trany(y)})"> {text} </text>\n'

    # def math_text(self, expression, x, y, colour="White", scale=4):
    #     math_to_svg(expression, os.getcwd() + "/temp.txt")
    #     with open("temp.txt", 'r') as file:
    #         code = file.read()
    #     os.remove(os.getcwd() + "/temp.txt")
    #     dx = len(expression) * scale
    #     dy = 9 * scale
    #     self.svg.canvas += '\n <g transform-origin="bottome" transform="translate(' + str(
    #         self.tranx(x) - dx) + ' ' + str(self.trany(y) - dy) + '),' + 'scale(' + str(scale) + ',' + str(
    #         scale) + ')' + ' ">'
    #     self.svg.canvas += code.replace('currentColor', colour).replace('8.781ex', str(scale))
    #     self.svg.canvas += '</g> \n'
    #
    # def add_math_text(self, expr, x, y, colour="white", scale=4):
    #     self.TexLoader.append([expr, x, y, colour, scale])

    def ticks(self, colour="yellow", strokewidth=1, markers=False, fontsize=4):
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
        strokewidth = strokewidth * self.nscale
        fontsize = fontsize * self.nscale
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

    def arrow(self, x1, y1, x2, y2, scale=1, colour='white', strokewidth=2):
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
        strokewidth = strokewidth * self.nscale
        scale = scale * self.nscale
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
        strokewidth = strokewidth * self.nscale
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
        strokewidth = strokewidth * self.nscale
        eps = self.xlim / n
        X = [self.tranx(i * eps - self.origin[0]) for i in range(-n, n + 1)]
        Y = [self.trany(func(i * eps - self.origin[0])) for i in range(-n, n + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def area(self, func, limits, colour="red", area_colour="orange", strokewidth=0, opac=1, n=500):
        strokewidth = self.nscale * strokewidth
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
        strokewidth = self.nscale * strokewidth
        eps = self.xlim / n
        X = [self.tranx(i * eps - self.origin[0]) if i % 15 > 7 else None for i in range(-n, n + 1)]
        Y = [self.trany(func(i * eps - self.origin[0])) for i in range(-n, n + 1)]
        self.svg.draw_polyline(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def plot_points(self, X, Y, colour="red", strokewidth=1, opac=1, style='none', fill='none', fill_opacity = 1):
        """
        Graphs the inputted points
        :param X:
        :param Y:
        :param colour:
        :param strokewidth:
        :param opac:
        :return:
        """
        strokewidth = strokewidth * self.nscale
        X1 = [self.tranx(x) for x in X]
        Y1 = [self.trany(y) for y in Y]
        self.svg.draw_polyline(X1, Y1, colour=colour, strokewidth=strokewidth, opac=opac, fill=fill, fill_opacity=fill_opacity)

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
        s = s * self.nscale
        if len(X) != len(Y):
            print("Data sets are misaligned!")
        for i in range(len(X)):
            self.svg.draw_circ(self.tranx(-X[i]), self.trany(Y[i]), s, fill=colour, stroke=colour,
                               strokewidth=0, opac=opac)

    def add_latex(self, expr, x0, y0, scale=1, rotation=0, centre_align=True, colour=None, preamble=None,
                  usepackages=None, cleanup=True, opacity=1, background=False, bg_colour='black', bg_opacity=.4,
                  box=False, boxcolour='white', boxwidth=2, boxmult=1.6):
        scale = scale * self.nscale
        if expr in self.latex_history:
            tex_info = self.latex_history[expr]
            expr_code, w_expr, h_expr = tex_info[0].replace('fill-opacity:1', f'fill-opacity:{round(opacity, 3)}'), \
                                        tex_info[1], tex_info[2]
        else:
            expr_code, w_expr, h_expr = latex_expression(expr, colour=colour, preamble=preamble,
                                                         usepackages=usepackages,
                                                         cleanup=cleanup)
            # Data processing
            index = len(self.latex_history)
            symbols = get_svg_symbol_ids(expr_code)
            clips = get_svg_clip_ids(expr_code)
            for symb in symbols:
                expr_code = expr_code.replace(symb, symb + f'-{index}')
            for clip in clips:
                expr_code = expr_code.replace(clip, clip + f'-{index}')

            self.latex_history[expr] = [expr_code, w_expr, h_expr, colour]

            expr_code = expr_code.replace('fill-opacity:1', f'fill-opacity:{round(opacity, 3)}')

        mata = scale * np.cos(rotation)
        matc = scale * np.sin(rotation)
        matb = -scale * np.sin(rotation)
        matd = scale * np.cos(rotation)
        if centre_align:
            mate = self.width / 2 + x0 * self.xscale - scale * (
                    np.cos(rotation) * w_expr + np.sin(rotation) * h_expr) / 2
            matf = self.height / 2 - y0 * self.yscale - scale * (
                    -np.sin(rotation) * w_expr + np.cos(rotation) * h_expr) / 2
        else:
            mate = self.width / 2 + x0 * self.xscale
            matf = self.height / 2 - y0 * self.yscale

        if background:
            self.svg.draw_rect(mate + scale * w_expr / 2, matf + scale * h_expr / 2, w_expr * scale, h_expr * scale,
                               fill=bg_colour, opacity=bg_opacity,
                               strokewidth=0)

        if box:
            self.svg.draw_rect(mate + scale * w_expr / 2, matf + scale * h_expr / 2, w_expr * scale * boxmult,
                               h_expr * scale * boxmult, 'None', strokewidth=boxwidth,
                               stroke=boxcolour)

        self.svg.canvas += f'<g transform="matrix({mata}, {matb},{matc}, {matd}, {mate}, {matf})">\n'
        self.svg.canvas += expr_code
        self.svg.canvas += '</g>\n'

    # Constructions

    def draw_arrow(self, x1, y1, x2, y2, scale=1, colour="black", strokewidth=1):
        strokewidth = strokewidth * self.nscale
        scale = scale * self.nscale
        self.svg.draw_arrow(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=colour,
                            strokewidth=strokewidth)

    def draw_arrow2(self, x1, y1, x2, y2, scale=1, colour="black", strokewidth=1):
        strokewidth = strokewidth * self.nscale
        scale = scale * self.nscale
        self.svg.draw_arrow2(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=colour,
                             strokewidth=strokewidth)

    def draw_double_arrow(self, x1, y1, x2, y2, scale=1, colour="black", strokewidth=1):
        strokewidth = strokewidth * self.nscale
        scale = scale * self.nscale
        self.svg.draw_arrow(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), scale, stroke=colour,
                            strokewidth=strokewidth)
        self.svg.draw_arrow(self.tranx(x2), self.trany(y2), self.tranx(x1), self.trany(y1), scale, stroke=colour,
                            strokewidth=strokewidth)

    def draw_polygon(self, X, Y, fill="none", colour="black", strokewidth=1, fill_opacity=1):
        strokewidth = strokewidth * self.nscale
        X1 = [self.tranx(x) for x in X]
        Y1 = [self.trany(y) for y in Y]
        self.svg.draw_polygon(X1, Y1, fill=fill, stroke=colour, strokewidth=strokewidth, opacity=fill_opacity)

    def draw_circle(self, x, y, r, fill="none", colour="black", strokewidth=1, fill_opacity=1):
        strokewidth = strokewidth * self.nscale
        self.svg.draw_circ(self.tranx(x), self.trany(y), self.xscale * r, fill=fill, stroke=colour,
                           strokewidth=strokewidth, fill_opacity=fill_opacity)

    def draw_rect(self, x, y, width, height, fill, colour="black", strokewidth=1, opac=1, fill_opacity=1):
        strokewidth = strokewidth * self.nscale
        self.svg.draw_rect(self.tranx(x), self.trany(y), abs(self.xscale * (width)),
                           self.yscale * height, fill, stroke=colour, strokewidth=strokewidth, opacity=opac,
                           fill_opacity=fill_opacity)

    def draw_ellipse(self, x, y, rx, ry, fill="none", fill_opacity=1, colour="black", strokewidth=1):
        strokewidth = strokewidth * self.nscale
        self.svg.draw_ellipse(self.tranx(x), self.trany(y), self.nscale * rx, self.nscale * ry, fill=fill,
                              stroke=colour,
                              strokewidth=strokewidth, fill_opacity=fill_opacity)

    def cubic_bezier(self, path, colour="red", strokewidth=2, opacity=1, fill="none"):
        pathstr = f'M {self.tranx(path[0, 0])} {self.trany(path[0, 1])} C '
        strokewidth = strokewidth * self.nscale
        for i in range(1, 4):
            pathstr += f'{self.tranx(path[i, 0])} {self.trany(path[i, 1])},'

        self.svg.draw_path(pathstr[:-1], colour=colour, strokewidth=strokewidth, opac=opacity, fill=fill)


    def quadratic_bezier(self, path, colour="red", strokewidth=2, opacity=1, fill="none"):
        pathstr = f'M {self.tranx(path[0, 0])} {self.trany(path[0, 1])} Q '
        strokewidth = strokewidth * self.nscale
        for i in range(1, 3):
            pathstr += f'{self.tranx(path[i, 0])} {self.trany(path[i, 1])},'

        self.svg.draw_path(pathstr[:-1], colour=colour, strokewidth=strokewidth, opac=opacity, fill=fill)

    def draw_path(self, path, colour="red", strokewidth=2, opacity=1, fill="none", fill_opacity = 0):
        strokewidth = strokewidth * self.nscale
        pobj = parse_path(path)
        print('rr', (pobj))
        translated_pobj = convert_points2giraphics2(pobj, self.tranx, self.trany)
        print('ll', len(translated_pobj))
        cc = path2svg(translated_pobj)
        self.svg.draw_path(cc, colour=colour, strokewidth=strokewidth, opac=opacity, fill=fill, fill_opacity = fill_opacity)

    def draw_line(self, x1, y1, x2, y2, marker="*", colour="black", strokewidth=1, opacity=1, cap="butt",
                  segments=20, style=None):
        strokewidth = strokewidth * self.nscale
        self.svg.draw_line(self.tranx(x1), self.trany(y1), self.tranx(x2), self.trany(y2), stroke=colour,
                           strokewidth=strokewidth, opacity=opacity, cap=cap, style=style)

    def draw_arc(self, x, y, r, start, stop, colour="red", strokewidth=2, opac=1, fill="none", fixflag=False):
        strokewidth = strokewidth * self.nscale
        self.svg.draw_arc(self.tranx(x), self.trany(y), r * self.xscale, start, stop, colour=colour,
                          strokewidth=strokewidth, opac=opac, fill=fill, fixflag=fixflag)

    def point(self, x, y, s=1, colour="white", opacity=1):
        s = s * self.nscale
        self.draw_circle(x, y, 15 * s / self.width, fill=colour, strokewidth=0, fill_opacity=opacity)

    def update_properties(self, width=None, height=None, xlim=None, ylim=None, transform=None):
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if xlim is not None:
            self.xlim = xlim
        if ylim is not None:
            self.ylim = ylim
        if transform is not None:
            self.transform = transform
        self.__init__(self.width, self.height, self.xlim, self.ylim, self.name, origin=self.origin,
                      transform=self.transform)

    def save(self, clear=False):
        self.svg.save()

        if clear:
            self.svg.canvas = ""

    # def save(self, clear=False):
    #     if len(self.TexLoader) != 0:
    #         for t in self.TexLoader:
    #             self.math_text(t[0], t[1], t[2], colour=t[3], scale=t[4])
    #     """
    #     Saves the plot and clears the svg.canvas
    #     """
    #     self.svg.save()
    #     if clear:
    #         self.svg.canvas = ""

    def jupyter_display(self, raster=False):
        self.save()
        print(os.getcwd())
        if not raster:
            return IPSVG(filename=os.getcwd() + '/' + self.name)
        else:
            convert_image(self.name + '.svg', self.name + '.png')
            return Image(filename=self.name + '.png')

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

# def f(x):
#     return x
#
#
# def g(x):
#     return x * x
# # #
# # #
# A = Graph(400, 400, 5, 5, 'svg2.svg', origin=[0, 0])
# A.bg(colour='black')
# A.axes()
# x, y = 3, 3
# A.draw_arrow2(1, 0, 3, 3, scale=2, colour='white')
# # A.point(x, y, s = .4, colour='red')
# A.ticks()
# A.draw_polygon([0,2,1], [0,0,1], colour='white', fill='white',fill_opacity=.2)
# A.grid([5,5])
# A.ticks(markers=True)
# # A.svg.draw_arrowhead2(200, 200, 10, 2,colour='white')
# A.save()
# A.display()

# # #
# from giraphics.utilities.utils import getAngle
# a,b = getAngle(0,0, 1,1)
# print(a+b, a-b)

# A.ticks(markers=True)
# A.text(0,0,'hello', colour='white')
# # A.plot(f)
# # A.plot(g)
# # A.add_latex('$x_1$', 0, 0, background=False, colour='white', scale=4, centre_align=False,
# #             box=True,boxcolour='white', boxwidth=2, opacity=1)
# #
# # A.add_latex2('a', 0, 0, scale=6, rotation=0*np.pi/2, colour=[0,0,0])
# #
# # A.add_latex2('b', 2, 3, scale=6, rotation=0*np.pi/2, colour=[0,0,0])
# #
# # # # A.draw_dotted_line(0, 0, 6, 7, stroke="white", marker=".")
# # A.add_inset(2,2,2,2,position=[3,3])
# # A.bg(colour='blue')
# # A.grid()
# # # A.draw_arrow(0,0, 4,4,colour='white')
# # A.axes()
# # # A.draw_rect(0,0,8,8,'none', colour='white')
# # # A.draw_arrow2(0,0, -4,-4, colour='white')
# # A.draw_line(0,0, 4, 0, colour='white')
# # A.draw_line(0,0, 4, 4, colour='white', style='dotted')
# # A.draw_arc(0,0, 3, 0, -np.pi/4)
# A.save()
# #
# # # A.display()
