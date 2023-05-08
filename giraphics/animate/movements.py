'''

Idea: want to create the entire sequence simply in terms of functions. without
having to paremetrisation everything manually. Zum Beispiel:


Create Scene
Define object Obj1
Obj1.fade_in() OR Obj2.draw_in()
Obj1.move(vel=parabola, [0,0])
Obj1.dynamics()
Obj1.fade_out()

Need to create relative positioning system.

Line =  [4 dofs; properties]
Circle = [4 dofs; properties]
Text = [2 dofs; properties ]
Path = [n dofs; properties]

'''

from giraphics.animate import *
import numpy as np


# class subobjects():
#     def __init__(self, *arg, **kwargs):
#         for k in kwargs
from sample_projects.Pendulum.pendulum import x1


def translate(array, change, degrees=[]):
    if len(degrees) == 0:
        array[:, 0] += change[0]
        array[:, 1] += change[1]
    else:
        for d in degrees:
            array[d, 0] += change[0]
            array[d, 1] += change[1]


class SubObject:
    def __init__(self):
        pass



class DObject:
    def __init__(self, label='', spatial=[]):
        self.spatial = np.array(spatial)
        self.label = label
        self.subobjects = []

    def transform(self, transformation):
        self.spatial = transformation(self.spatial)

    # Constructions
    def line(self, x1, y1, x2, y2, strokewidth=1, colour = 'white', opacity=1):
        properties = {'type': 'line', 'x0': np.array([x1,y1]), 'x1': np.array([x2,y2]), 'colour':colour, 'opacity': opacity,
                      'strokewidth': strokewidth}
        self.subobjects.append(properties)

    def circle(self, x, y, r, strokewidth=1, colour = 'white', opacity=1):
        properties = {'type': 'circle', 'center': np.array([x,y]), 'r': r, 'colour':colour, 'opacity': opacity}
        self.subobjects.append(properties)

    def plot_points(self, X, Y, colour =  'white', opacity= 1):
        properties = {'type': 'plot_points', 'X': np.array(X), 'Y': np.array(Y), 'colour': colour, 'opacity': opacity}
        self.subobjects.append(properties)

    # Setting properties
    def set_opacity(self, opacity):
        for i in range(len(self.subobjects)):
            self.subobjects[i]['opacity'] = opacity

    def scale(self, scale_factor):
        for i in range(len(self.subobjects)):
            self.subobjects[i]['scale'] = scale_factor

    def rotate(self, theta, center = [0, 0]):
        for sobj in self.subobjects:
            if sobj['type'] == '':
                pass




Pendulum = DObject('')
Pendulum.line(0,0, 2, 2, 0)
Pendulum.


class Studio:
    def __init__(self):
        pass

