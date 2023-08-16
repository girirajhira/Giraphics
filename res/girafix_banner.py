from giraphics.graphing.fancygraph import FancyGraph
from math import sin, cos

banner_width_px = 1200
banner_height_px = 600

banner_height = 3
banner_width = 6

g = FancyGraph(banner_width_px, banner_height_px, banner_width, banner_height, "banner.svg")

g.bg(colour="black")
g.grid(opac=0.3, grid_int=[12, 6])


def phase(x, y):
    return [sin(y - 0.0), cos(x + y + 2.45)]

g.VectorField(phase, arrow_scale=1.8, gridint=[12, 6], tail_length=0.32, strokewidth=2.3, constLength=True)
# g.draw_rect(-2.85,-.08, 1, 0.6, "red", opac=.64)
g.add_latex(r"$\mathbb{G}$iraphics", 0, 0, colour='white', scale=3, cleanup=False, background=True)
g.save()
g.display()

# from fancygraphs import FancyGraph
# from math import  sin, cos
# g = FancyGraph(1500, 600, 8, 3, "banner.svg")
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
