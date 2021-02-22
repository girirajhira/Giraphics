from giraphics.graphing.graph import *
from giraphics.utilities.convert import *
from giraphics.utilities.utils import Timer
w, h = 1000, 1000
r = 2
def f(s):
    def f1(x):
        return x*x+s
    return f1
g = Graph(w,h, 10,10, "b1.svg")
g.bg("black")
for i in range(-10,10,2):
    g.plot(f(i))
g.save()


g = Graph(w,h, 10,10, "b2.svg")
g.bg("black")
for i in range(-10,10,2):
    g.plot(f(i))
g.save()
t = Timer()
t.start()
create_raster("b1")
t.stop()
t.start()
create_raster2("b2")
t.stop()
