from svgwtr import *
from grapher import *
import numpy as np


class Widget(Grapher):
    def __init__(self, win_width, win_height, xlim, ylim, x, y, origin=[0.0, 0.0], border = True):
        self.svg = SVG('None', win_width, win_height, fullsvg=False)
        self.eps = xlim / 2000
        self.height = win_height
        self.width = win_width
        self.xlim = xlim
        self.ylim = ylim
        self.absposx = x
        self.absposy = y
        self.origin = np.array([-xlim, -ylim]) + np.array(origin)

    def tranx(self, x):
        if x != None:
            return self.absposx + (self.width / (2 * self.xlim)) * (x + self.origin[0])
        else:
            return None

    def trany(self, y):
        if y != None:
            return self.absposy - (self.height / (2 * self.ylim)) * (y  + self.origin[1])
        else:
            return None


class Scene(Grapher):
    def createWidget(self, width, height, xlim, ylim, x, y, origin=[0.0, 0.0], border=True, bcol = "white", bstroke = 1):
        absx, absy = self.tranx(x), self.trany(y)
        # border
        self.svg.draw_rect(absx,absy,width, height, 'none', stroke=bcol, strokewidth=bstroke)
        return Widget(width, height, xlim, ylim, absx + width/2, absy- height/2, origin=origin)

    def commitWidgets(self, *args):
        self.svg.canvas += '\n'
        for g in args:
            self.svg.canvas += g.svg.canvas + '\n'

import math

def f(X):
    return  X*X
A = Scene(2000, 2000, 10, 10, 'Ascene.svg')
A.bg("black")
A.axes(colour="white")
G1 = A.createWidget(1000,1000,10,10,5,5, origin=[-10,-0])
G1.axes(colour="yellow")
G1.graph(f)
A.commitWidgets(G1)
A.show()
