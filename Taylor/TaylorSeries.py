from convert import *
from graph import *
import matplotlib.pyplot as plt
from math import floor

def fact(x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        t = 1
        for i in range(1,x+1):
            t*=i
        return t
def coeff_discrete(t0, t):
    if t <= t0:
        return 0
    elif t >= t0 + 1:
        return 1
    else:
        return t - t0
def taylor_series_sine(t, max_order=30):
    def f(x):
        total = 0
        for n in range(0, max_order+1):
            total += coeff_discrete(n, t)*((-1)**n)*(x**(2*n+1))/fact(2*n+1)
        return total
    return f

frames = 500 + 1
create_directory("ftp")
create_directory("ftprast")

for i in range(frames):
    t = i/80
    g = Graph(400, 400 , 10, 10,"ftp/g"+namer(i)+".svg", origin=[0,0])
    g.bg("black")
    g.grid()
    g.axes("yellow")
    g.embed_latex( "Order $n$ = " + str(floor(t)), -8, 8)
    g.graph(taylor_series_sine(t, max_order=round(frames/80)),colour="white", strokewidth=1.5)
    g.save()

create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# Creating the final video
create_mpeg('t4.mp4', 'p', frames, dir=os.getcwd()+"/ftprast")
