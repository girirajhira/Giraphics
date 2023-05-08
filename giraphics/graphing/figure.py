import numpy as np

from giraphics.graphing.graph import Graph
from math import pi

class Figure(Graph):
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], theme="dark",
                 border_width=0.12, bg="white"):
        Graph.__init__(self, width, height, xlim, ylim, name, theme=theme)
        self.bw = 1 - border_width
        self.border_width = border_width
        self.inner_graph = Graph(self.bw * width, self.bw * height, xlim, ylim, name, origin=origin,
                                 theme=theme, transform="translate("+str(width*border_width/2) + " " + str(height*border_width/2) + ")", grouped=True)
        # self.bg(colour=bg)

    def plot(self, func, colour="red", strokewidth=1.5, opac=1, n=1200):
        self.inner_graph.plot(func, colour="red", strokewidth=1.5, opac=1, n=1200)
        # Draw margins

    def plot_points(self, X, Y, colour="red", strokewidth=1, opac=1):
        self.inner_graph.plot_points(X, Y, colour=colour, strokewidth=strokewidth, opac=opac)

    def scatter(self, X, Y, s=1, colour="white", opac=1):
        self.inner_graph.scatter(X,Y,s=s, colour=colour, opac=opac)

    def include_model(self, S):
        self.inner_graph.include_model(S)

    def bg(self, colour="white"):
        self.bg("white")

    # def axes(self, colour="yellow", strokewidth=1, arrows=False):
    #     self.inner_graph.axes(colour=colour, strokewidth=strokewidth, arrows=arrows)

    def grid(self, grids=[20, 20], colour="grey", strokewidth=0.7, opac=0.2):
        self.inner_graph.grid(grid_int=grids, colour=colour, strokewidth=strokewidth, opac=opac)

    def grid2(self, grids=[20, 20], colour="white", strokewidth=0.7, opac=0.2):
        self.inner_graph.grid(grid_int=grids, colour=colour, strokewidth=strokewidth, opac=opac)

    def bg(self, colour):
        self.inner_graph.bg(colour=colour)

    # def ticks(self, stroke="grey", strokewidth=1, tick=10, markers=False, fontsize=8):
    #     self.inner_graph.ticks(stroke=stroke, strokewidth=strokewidth, tick=tick, markers=markers, fontsize=fontsize)
    def ticks(self, stroke="black", strokewidth=1, tick=10, markers=False, fontsize=8):
        tickx = round(tick * 2)
        ticky = round(tick * 2)
        self.text(0,0,"here")
        a, b = self.width*self.border_width/2,  self.height*(self.border_width)/2
        dx = (1-self.border_width)*self.width / tickx
        dy = (1-self.border_width)*self.height / ticky
        ox = self.xlim * 2 / tickx
        oy = self.ylim * 2 / ticky
        # x axis
        for i in range(1, tickx):
            self.svg.draw_line(dx * i + a, self.trany(fontsize / (3 * dy) -self.ylim*self.bw ) , dx * i +a,  self.trany(-fontsize / (3 * dy)  -self.ylim*self.bw),
                               stroke=stroke, strokewidth=strokewidth)
            if markers:
                if i - self.xlim != 0:
                    self.text((i - self.xlim - self.origin[0] - self.border_width*self.xlim) * ox*self.bw, -2*fontsize / dy - self.ylim*self.bw,
                              str((round((i - self.xlim - self.origin[0]) * ox, 2))),
                              fontsize=fontsize, colour=stroke, opac=0.6)

        # y axis
        for i in range(1, ticky):
            self.svg.draw_line(self.tranx(-fontsize / (2 * dx)-self.xlim*self.bw), dy * i + b, self.tranx(fontsize / (2 * dx) -self.xlim*self.bw), dy * i + b,
                               stroke=stroke,
                               strokewidth=strokewidth)
            if markers:
                if i - self.ylim != -self.ylim :
                    self.text(-2*fontsize / dx - self.xlim*self.bw, (i - self.ylim - self.origin[1]) * oy*self.bw,
                              str((round((i - self.ylim - self.origin[1]) * oy, 2))),
                              fontsize=fontsize, colour=stroke, opac=0.6)

    # Todo: Constructions #

    # Features

    def xlabel(self, label="x", fontsize=13, use_latex=False, scale=2):
        if use_latex:
            x = self.origin[0]
            y = -self.ylim * self.bw - (1 - self.bw) * self.ylim / 2
            self.add_latex(label, x, y, scale=scale)
        else:
            x = self.origin[0]
            y = -self.ylim*self.bw - (1-self.bw)*self.ylim/2
            self.text(x, y, text=label, colour="black", fontsize=fontsize)

    def ylabel(self, label="f(x)", fontsize=13, use_latex=False,scale=2):
        if use_latex:
            y = self.origin[1]
            x = -self.xlim * self.bw - (1 - self.bw) * self.xlim/2
            self.add_latex(label, x, y, scale=2, rotation=pi/2)
        else:
            y = self.origin[1]
            x = -self.xlim*self.bw - (1-self.bw)*self.xlim/2
            self.text(x, y, text=label, colour="black", fontsize=fontsize, rotation="-90")

    def title(self, title_label, fontsize = 26, use_latex=False):
        if use_latex:
            x = self.origin[0]
            y = self.ylim * self.bw + (1 - self.bw) * self.ylim / 3
            self.add_latex(title_label,x,y)
        else:
            x = self.origin[0]
            y = self.ylim*self.bw + (1-self.bw)*self.ylim/3
            self.text(x, y, title_label, colour="black", fontsize=fontsize)


    def legend(self, data, loc = 'upper right'):
        for i in range(0,1)


    def save(self):
        self.svg.canvas += self.inner_graph.svg.canvas + "\n </svg>\n </g>\n </g>\n"
        self.draw_rect(0, 0, 2 * self.xlim * self.bw, 2 * self.ylim * self.bw, fill="none", colour="black",
                       strokewidth=1.2)
        Graph.save(self)


import math
def func(x):
    return 0.04 * x ** 2 * math.sin(6 * x) - 5


f = Figure(600, 450, 15, 10, "fig2.svg", origin=[0,0])
f.plot(func, colour="red")
f.plot_points(np.linspace(-15,15, 100),np.linspace(-15,15, 100)**2, colour='blue')
f.grid()
# f.grid2(colour="blue")
# f.ticks(markers=True)
# f.xlabel(label="$f(x)$", use_latex=True)
# f.ylabel(use_latex=True)
f.inner_graph.axes(colour='black')
f.xlabel(label ='$x$', use_latex=True)
f.ylabel(label ='$y$', use_latex=True)
f.add_latex('$f(x)$', 0, 0, scale=3, rotation=0)
# f.title("Title", use_latex=True)
f.save()
f.display()
