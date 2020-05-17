import math
import os
import convert
import sys
from grapher import Grapher

'''
TODO: Fix grid issue, too bold
    : Quality control
    : Create work spaces
    : Do an eigen vector example

'''
def Error(error):
    print("Error!: " + error)
    sys.exit()

def createDir(dirName):
    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

class Animate:
    def __init__(self, width, height, func, xlim = 10, ylim = 10 ,frames=10, eps = 0.1, strokewidth=1, type="complex"):
        self.func = func
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.frames = frames
        self.eps = eps
        self.type = type

    def epsf(self, i):
        return (i)**3

    def create_frame(self, name, func, i,axes = True, label=True, expr = "",  grid = True, axestroke = 2, axescolour = "white", strokewidths=[2], colours=["yellow"], bg="black", gridcolour="yellow", grindint=10, scale=0.8, grids=[10,10], s=1, opac=1):
        if self.type == "complex":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            for i in range(len(func)):
                G.ComplexPlot(func[i], strokewidths=strokewidths[i])
            G.show()
        elif self.type == "cart":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            if label:
                G.embed_latex_anim(expr % (i, i), self.xlim-2, self.ylim-2)
            for i in range(len(func)):
                G.graph(func[i], strokewidth=strokewidths[i], colour=colours[i], opac=opac)
            G.show()
        elif self.type == "lineartrans":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            for i in range(len(func)):
                G.LinearTranforms(func, strokewidths=strokewidths)
            G.show()
        elif self.type == "scatter":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            for i in range(len(func)):
                G.scatter(func[i], strokewidth=strokewidths[i])
            G.show()
        elif self.type == "vectorfield":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            for i in range(len(func)):
                G.VectorField(func[i], strokewidth=strokewidths[i], stroke=colours[i], gridint=grindint, scale=scale, constcolour=False)
            G.show()
        elif self.type == "complexscatter":
            G = Grapher(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=gridcolour)
            for i in range(len(func)):
                G.ComplexPlotScatter(func[i], s = s, colour=colours[i], grids = grids)
            G.show()
        else:
            Error(str(self.type) + " is not a valid plot type. Instead enter complex, cart, linstrans")


    def animate(self, outputFile,label = False, axes= True, grid = False, strokewidths=[2], gridcolour="yellow", bg="black", colours=["yellow"], scale=0.8, grindint=10, s = 1, grids = [10,10], expr=""):
        createDir("Plots")
        for i in range(self.frames+1):
            self.create_frame('Plots/g%s.svg' % i, [f(i*self.eps) for f in self.func], i, label = label, expr=expr, grid=grid, s = s, grids = grids, axes=axes, strokewidths=strokewidths, gridcolour=gridcolour, bg=bg, colours=colours, scale = scale, grindint = grindint)
            print(i)
        convert.BatchConvert("Plots",outputFile, self.frames)
        print("Done!")
    def live_animate(self):
        pass
'''
def sin(s):
    def f(x):
        return math.sin(s*x)*x*x
    return f


def f1(s):
    def f2(x, y):
        if x == 0 and y == 0:
            return 0
        else:
            return (x + y * 1j)**(1-s)
    return f2

M = [[1,4], [-2, 3]]
def func(t):
    def f(x,y):
        a, b, c, d = M[0][0], M[1][0], M[0][1], M[1][1]
        R = (1 + (a-1)*t)*x + b*t*y
        I = c*t*x + (1 + (d-1)*t)*y
        return R + 1j*I
    return f

def square(t):
    def f(x,y):
        return (x+1j*y)**(1+t)
    return f

def gamma(v):
    return 1/math.sqrt(1-v*v)

def fg(s):
    def gg(x,t):
        return gamma(
        s)*(x-s*t) + gamma(s)*(t-s*x)*1j
    return gg

'''
from math import sin
def f1(s):
    def f(x):
        if x < 10*s:
            return sin(x)
        else:
            return None
    return f

'''

K = Animate(1000, 1000, [f1] ,strokewidth=2, frames=100, eps=0.01, xlim=10, ylim=10, type="cart")

K.animate("wavepacket33.mp4", scale=0.75, grindint=20, colours=["white"], strokewidths= [1], grid=False, axes=False, label=False, expr = "$Z(x,%s) = sin(3x+%s)$" )
'''