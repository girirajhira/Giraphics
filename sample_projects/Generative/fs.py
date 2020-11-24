from giraphics.graphing.graph import *
from giraphics.utilities.convert import *
from math import sin
from random import randint

def g(s, t):
    def f(x):
        return 4*sin(0.3*x-t) + s
    return f

create_directory("Plotsr")
create_directory("plotsrast")


eps = 5/10
frames = 80
for j in range(0, 80):
    G = Graph(1600, 1600, 10, 10, "Plots/g"+namer(j)+".svg")
    G.bg("black")
    t = 0.02*j
    for i in range(0,50):
        e = eps * i - 8
        G.graph(g(e+t*randint(0,4), t), colour="white",opac=abs(sin(e+t)*2), n0=250)
    G.save()

create_raster_batch("Plots", 'g', 'p', 'plotsrast', 80)
create_mpeg('sav2e.mp4', 'p', 80, dir=os.getcwd() + "/plotsrast")



