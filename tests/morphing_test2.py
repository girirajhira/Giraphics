import numpy as np

from giraphics.animate.animation import Animation
from giraphics.svg.morph3 import SVGPathObject
from giraphics.graphing.graph import Graph

path1 = "M278.929,1078.35C278.929,1078.35 -110.151,868.617 488.661,868.617C1087.47,868.617 1126.46,1038.37 850.468,762.376C574.471,486.379 404.815,48.575 638.169,422.337C871.522,796.099 360.945,461.759 360.945,699.561C360.945,937.363 146.526,1005.99 388.019,1005.99C629.513,1005.99 796.565,1092.84 579.994,1092.84C363.422,1092.84 278.929,1078.35 278.929,1078.35Z"
path2 = "M884.922,458.935C884.922,458.935 371.357,910.292 884.922,910.292C1398.49,910.292 1413.88,694.506 1257.29,537.922C1100.71,381.338 918.11,425.747 884.922,458.935Z"

spo2 = SVGPathObject(path1, stroke='black', strokewidth=1)
spo1 = SVGPathObject(path2, stroke='black', strokewidth=4)


morphing1 = spo2.morph_to(spo1)

A = Animation('morph_test1.mp4', 2000, 2000, 10, 10)

frames = 120

speedfunc = lambda x:x**(.5)

for i in range(frames+1):
    t = speedfunc(i/frames)
    A.plate.bg(colour='white')
    morphing1(t).draw(A)
    # print(morphing1(i/frames).pathObj)
    A.plate.press()


A.pause(20)

for i in range(frames+1, 0, -1):
    t = speedfunc(i/frames)
    A.plate.bg(colour='white')
    morphing1(t).draw(A)
    # print(morphing1(i/frames).pathObj)
    A.plate.press()


A.develop(cleanup=True,  timeit=True)

#
# G = Graph(1000,1000,10,10,'mt.svg')
# G.bg(colour='white')
# G.draw_path(path1, translate=False)
# G.save()