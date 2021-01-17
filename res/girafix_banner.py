from giraphics.graphing.fancygraphs import FancyGraphs
from math import  sin, cos
g = FancyGraphs(1200, 600, 6, 3, "banner.svg")

g.bg(colour="black")
g.grid(opac=0.3, grid_int=[12,6])

def phase(x, y):
    return [sin(y-0.0), cos(x+y+2.45)]

g.VectorField(phase, arrow_scale=1.8, gridint=[12,6],  tail_length=0.32, strokewidth=2.3, constLength=True)
g.draw_rect(-0.5,-.08, 5.7, 0.6, "black", opac=.64)
# g.draw_rect(-2.85,-.08, 1, 0.6, "red", opac=.64)
g.add_math_text("\mathbb{G}iraphics", -2.1, 0, scale=7)
g.save()
g.display()


# from fancygraphs import FancyGraphs
# from math import  sin, cos
# g = FancyGraphs(1500, 600, 8, 3, "banner.svg")
#
# g.bg(colour="black")
# g.grid(opac=0.3, grid_int=[25,10])
#
# def phase(x, y):
#     return [sin(y-0.4), cos(x+2.65)]
#
# g.VectorField(phase, arrow_scale=1., gridint=[25,10],  tail_length=0.3, constLength=True)
# g.add_math_text("\mathbb{G}ira\mathbb{F}i\mathbb{X}", 0, 0, scale=7)
# g.save()
# g.display()
