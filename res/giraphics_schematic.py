from giraphics.graphing.graph import *

g = Graph(500, 500, 5, 5, 'schematic.svg')

g.bg()
g.point(0, 0, s=3)
g.text(-.1,-.4, 'centre (0,0)', fontsize=12)

g.axes()
g.draw_line(0,0,g.xlim, 0, colour='white')
g.draw_rect(g.xlim/2, -0, 0.7, 0.1, 'black')
g.text(g.xlim/2, -0.1/2, 'xlim', colour='white', fontsize=10)

g.draw_line(0,0, 0, g.ylim,  colour='white')
g.draw_rect(0, g.ylim/2, 0.4, 0.35, 'black')
g.text(-0.05, g.ylim/2, 'ylim', fontsize=10)

g.draw_double_arrow(-0.9*g.xlim, g.ylim,-0.9*g.xlim, -g.ylim , colour='white')
g.draw_double_arrow(g.xlim, -0.9*g.ylim, -g.xlim, -0.9*g.ylim , colour='white')

g. draw_arrow(0,0,-1.25,-.6, colour='white')
g.save()
g.display()
