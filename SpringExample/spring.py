from graph import *
from convert import *
import matplotlib.pyplot as plt
S = Model(1000, 1000 ,10 ,10 ,"springmdoel.svg", origin=[-9,-8])
from math import sin, cos, exp
def spring(L, height = 1.5, end_x=0, end_y=0, units=10):
    dx = L/units
    for x in range(0,units):
        S.draw_line(end_x + x*dx, ((-1)**x)*height/2 + end_y, end_x + (x+1)* dx, ((-1)**(x+1))*height/2 + end_y, stroke="white")
    #S.draw_rect(end_x+L-dx*1/2, end_y, 0.5, 0.5, "white", strokewidth=0)

def harmonic(s, y0=1, v0=0, w=2, decay=0):
    def f(t):
        if t<s:
            return exp(-decay*(t+s))*(y0*cos(w*(t+s))+ v0*sin(w*(t+s))/w)
        else:
            return None
    return f


'''
S.bg()
spring(10)
spring(5, end_y=3)
spring(12.3, end_y=-3, end_x=-3)
S.show()
'''
#'''
frames = 100
create_directory("ftp")
create_directory("ftprast")

for i in range(frames):
    t = i/1000
    g = Graph(1000, 1000, 10, 10, "ftp/g"+namer(i)+".svg", origin=[0, 0])
    g.bg("black")
    g.grid()
    f = harmonic(frames*10)
    spring(f(t*100), end_x=0,end_y=4)
    g.include_model(S)
    S.clear()
    g.axes("yellow")
    g.graph(harmonic(i))
    g.save()

create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# Creating the final video
create_mpeg('t4.mp4', 'p', frames, dir=os.getcwd()+"/ftprast")
#'''