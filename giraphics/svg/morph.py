from giraphics.svg.svgkit import *
from xml.dom import minidom
from math import floor
import re

test_code  = '''  <path d="M 10 315
           L 110 215
           A 36 60 0 0 1 150.71 170.29
           L 172.55 152.45
           A 30 50 -45 0 1 215.1 109.9
           L 315 10" stroke="black" fill="green" stroke-width="2" fill-opacity="0.5"/>'''

test_code2 = '''M128.491,140C128.491,140 152.217,105.125 173.377,125.792C181.998,134.212 198.871,152.834 215.841,171.948C240.525,199.751 265.415,228.594 265.415,228.594C265.415,228.594 310.397,262.127 314.556,240C318.714,217.873 300,231.161 300,231.161C300,231.161 263.348,201.286 231.714,171.612C209.637,150.903 190.003,130.291 186.978,120C179.618,94.964 154.942,88.134 140,110.946C125.058,133.759 118.009,143 128.491,140Z'''


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class Curve:
    def __init__(self, type,  path = None):
        self.type = type
        self.path = path

    def __repr__(self):
        return  f'{self.type} : {self.path}'
    def __len__(self):
        return len(self.path)

def get_svg_symbol_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('d') for symb in doc.getElementsByTagName('symbol')]
    doc.unlink()
    return symbols


def parse_svg_path(svg_code):
    doc = minidom.parseString(svg_code)
    path = [path.getAttribute('d') for path in doc.getElementsByTagName('path')][0]
    return path

def pathToCurve(path):
    path =  (path.replace(',', ' ')) # removes commas
    path = re.sub("[A-Za-z]+", lambda group: " " + group[0] + " ", path).strip() # Adds a space between alphabets and numbers
    pathlist = path.split(' ')
    curveDef = []
    new_path = []
    for p in pathlist:
        if p.isalpha():
            curveDef.append(Curve(p))
            if len(new_path) != 0:
                curveDef[-2].path = new_path
                new_path = []
        else:
            new_path.append(float(p))
    return curveDef

def morph_path(path1, path2):
    # Potentiall need to remove z and m
    # path1 = [s for s in path1 if s.type!='z' or s.type!='Z' or s.type!='M' or s.type!='m' ]
    # path2 = [s for s in path2 if s.type!='z' or s.type!='Z' or s.type!='M' or s.type!='m' ]

    segment1 = len(path1)
    segment2 = len(path2)
    if segments2 > segment1:
        segments1, segment2 = segment2, segment1
        path1, path2 = path2, path1

    # Need to morph segments into eachother


def morphLinear__(curve1, curve2):
    if len(curve1) < len(curve2):
        curve1, curve2 = curve1, curve2
    elif len(curve1) == len(curve2):
        '''
        Simple linear interpolation
        '''
        pass
    l1, l2 = len(curve1), len(curve1)
    q, r = divmod(l1,l2)
    for i in range(l2):
        pass




print(pathToCurve(test_code2))

class Bezier:
    def __init__(self, order, points):
        if order != len(points) + 1:
            print(f'Error must input {order} control points, {len(points)} given.')
            pass
        self.order = order
        self.points = points





