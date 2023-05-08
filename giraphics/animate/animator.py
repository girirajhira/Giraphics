import multiprocessing
import os
from giraphics.utilities.utils import listlike
from giraphics.utilities import convert
import sys
from giraphics.graphing.fancygraph import FancyGraph
from giraphics.utilities.timer import Timer

'''
TODO: Fix grid issue, too bold
    : Quality control
    : Create work spaces
    : Do an eigen vector example
'''

def Error(error):
    print("Error!: " + error)
    sys.exit()


def create_directory(directory):
    try:
        os.mkdir(directory)
        print("Directory ", directory, " Created ")
    except FileExistsError:
        print("Directory ", directory, " already exists")


class Animator:
    def __init__(self, width, height, xlim=10, ylim=10, frames=10, eps=0.1, type="complex"):
        self.func = []
        self.height = height
        self.width = width
        self.xlim = xlim
        self.ylim = ylim
        self.frames = frames
        self.eps = eps
        self.type = type

    def epsf(self, i):
        return (i) ** 3

    def create_frame(self, name, func, i, axes=True, label=True, expr="", grid=True, axestroke=2, axescolour="white",
                     strokewidths=[2], colours=["yellow"], bg="black", grid_colour="yellow", grindint=10, scale=0.8,
                     grids=[10, 10], s=1, opac=1, display=False):
        if self.type == "complex":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            for i in range(len(func)):
                G.ComplexPlot(func[i], strokewidth=strokewidths[i])
            G.save()
            if display:
                G.display()
        elif self.type == "cart":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            if label:
                G.embed_latex_anim(expr % (i, i), self.xlim - 2, self.ylim - 2)
            for i in range(len(func)):
                G.plot(func[i], strokewidth=strokewidths[i], colour=colours[i], opac=opac)
            G.save()
            if display:
                G.display()
        elif self.type == "lineartrans":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            for i in range(len(func)):
                G.LinearTranforms(func, strokewidths=strokewidths)
            G.save()
            if display:
                G.display()
        elif self.type == "scatter":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            for i in range(len(func)):
                G.scatter(func[i], strokewidth=strokewidths[i])
            G.save()
            if display:
                G.display()
        elif self.type == "vectorfield":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            for i in range(len(func)):
                G.VectorField(func[i], strokewidth=strokewidths[i], stroke=colours[i], gridint=grindint, scale=scale,constcolour=False)
            G.save()
            if display:
                G.display()
        elif self.type == "complexscatter":
            G = FancyGraph(self.height, self.width, self.xlim, self.ylim, name)
            G.bg(bg)
            if axes:
                G.axes(colour=axescolour, strokewidth=axestroke)
            if grid:
                G.grid(colour=grid_colour)
            for i in range(len(func)):
                G.ComplexPlotScatter(func[i], s=s, colour=colours[i], grids=grids)
            G.save()
        else:
            Error(str(self.type) + " is not a valid plot type. Instead enter complex, cart or linstrans")

    def create_frames(self, i, label, axes, grid, strokewidths, grid_colour, bg,
                      colours, scale, grindint, s, grids, expr):
        self.create_frame('Plots/g%s.svg' % i, [f(i * self.eps) for f in self.func], i, label=label, expr=expr,
                          grid=grid, s=s, grids=grids, axes=axes, strokewidths=strokewidths, grid_colour=grid_colour,
                          bg=bg, colours=colours, scale=scale, grindint=grindint)
        print(i)

    def animate(self, func, outputFile, label=False, axes=True, grid=False, strokewidth=2, grid_colour="yellow", bg="black",
                colour="yellow", scale=0.8, grindint=10, s=1, grids=[10, 10], expr=""):
        self.func = listlike(func)
        colour = listlike(colour)*len(self.func)
        strokewidth = listlike(strokewidth)*len(self.func)
        create_directory("Plots")
        jobs = []
        for i in range(self.frames + 1):
            p = multiprocessing.Process(target=self.create_frames, args=(i, label, axes, grid, strokewidth, grid_colour, bg, colour, scale, grindint, s, grids, expr))
            jobs.append(p)
            p.start()

        t = Timer()
        t.start()
        convert.batch_convert_multi("Plots", outputFile, self.frames)
        t.stop()
        print("Done!")

    def test_frame(self, func, outputFile, n=1, label=False, axes=True, grid=False, strokewidth=2, grid_colour="yellow", bg="black",
                colour="yellow", scale=0.8, grindint=10, s=1, grids=[10, 10], expr="", display=True):
        self.func = listlike(func)
        colour = listlike(colour) * len(self.func)
        strokewidth = listlike(strokewidth) * len(self.func)
        self.create_frame((outputFile)[:-4]+"_test.svg", [f(n * self.eps) for f in self.func], n, label=label, expr=expr,
                          grid=grid, s=s, grids=grids, axes=axes, strokewidths=strokewidth, grid_colour=grid_colour,
                          bg=bg, colours=colour, scale=scale, grindint=grindint, display=display)


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


def f1(s):
    def f(x, y):
        p = x
        q = y*1j
        if p**2 + q**2 == 0:
            return 0
        else:
            return (p**2 - q**2)**(s/100)
    return f


K = Animator(1000, 1000, frames=400, eps=0.01, xlim=10, ylim=10, type="complex")

#K.test_frame(f1, "a5.mp4", n=400, scale=0.75, grindint=20, colour="white", stroke_width=[1], grid=True, axes=False, label=False, expr="$Z(x,%s) = sin(3x+%s)$")
K.animate(f1, "a2.mp4", scale=0.75, grindint=20, colour="white", strokewidth=[1], grid=True, axes=False, label=False, expr="$Z(x,%s) = sin(3x+%s)$")
