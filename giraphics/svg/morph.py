from giraphics.svg.svgkit import *
from xml.dom import minidom
from math import floor
import re
# from svgpath2mpl import parse_path
from svg.path import parse_path, Line, Arc, CubicBezier, QuadraticBezier, Move
import svgpathtools

test_code = '''  <path d="M 10 315
           L 110 215
           A 36 60 0 0 1 150.71 170.29
           L 172.55 152.45
           A 30 50 -45 0 1 215.1 109.9
           L 315 10" stroke="black" fill="green" stroke-width="2" fill-opacity="0.5"/>'''

test_code2 = '''M128.491,140C128.491,140 152.217,105.125 173.377,125.792C181.998,134.212 198.871,152.834 215.841,171.948C240.525,199.751 265.415,228.594 265.415,228.594C265.415,228.594 310.397,262.127 314.556,240C318.714,217.873 300,231.161 300,231.161C300,231.161 263.348,201.286 231.714,171.612C209.637,150.903 190.003,130.291 186.978,120C179.618,94.964 154.942,88.134 140,110.946C125.058,133.759 118.009,143 128.491,140Z'''
test_code2 = '''M128.491,140C128.491,140 152.217,105.125 173.377,125.792C181.998,134.212 198.871,152.834 215.841,171.948C240.525,199.751 265.415,228.594 265.415,228.594C265.415,228.594 310.397,262.127 314.556,240C318.714,217.873 300,231.161 300,231.161C300,231.161 263.348,201.286 231.714,171.612C209.637,150.903 190.003,130.291 186.978,120C179.618,94.964 154.942,88.134 140,110.946C125.058,133.759 118.009,143 128.491,140Z'''





def parse_svg_path(svg_code):
    '''
    Helper function
    :param svg_code:
    :return:
    '''
    doc = minidom.parseString(svg_code)
    path = [path.getAttribute('d') for path in doc.getElementsByTagName('path')][0]
    return path


def pathToCurve(path):
    path = (path.replace(',', ' '))  # removes commas
    path = re.sub("[A-Za-z]+", lambda group: " " + group[0] + " ",
                  path).strip()  # Adds a space between alphabets and numbers
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


class SVGPath:
    def __init__(self, path):
        curve = pathToCurve(path)


# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False


class Curve:
    def __init__(self, type, path=None):
        self.type = type
        self.path = path

    def __repr__(self):
        return f'{self.type} : {self.path}'

    def __len__(self):
        return len(self.path)


def get_svg_symbol_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('d') for symb in doc.getElementsByTagName('symbol')]
    doc.unlink()
    return symbols


def morph_path(path1, path2):
    # Potentiall need to remove z and m
    # path1 = [s for s in path1 if s.type!='z' or s.type!='Z' or s.type!='M' or s.type!='m' ]
    # path2 = [s for s in path2 if s.type!='z' or s.type!='Z' or s.type!='M' or s.type!='m' ]


    segment1 = len(path1)
    segment2 = len(path2)
    if segment2 > segment1:
        segments1, segment2 = segment2, segment1
        path1, path2 = path2, path1

    # Need to morph segments into eachother


# def morphLinear__(curve1, curve2):
#     if len(curve1) < len(curve2):
#         curve1, curve2 = curve1, curve2
#     elif len(curve1) == len(curve2):
#         '''
#         Simple linear interpolation
#         '''
#         pass
#     l1, l2 = len(curve1), len(curve1)
#     q, r = divmod(l1, l2)
#     for i in range(l2):
#         pass
#

def morph(coords1, coords2, style='linear'):
    if len(coords1) > len(coords2):
        coords1, coords2 = coords2, coords1
        tsign = - 1
        offset = 1
    else:
        tsign = 1
        offset = 0

    l1 = len(coords1)
    l2 = len(coords2)

    if style == 'linear':
        def parametrise(t0):
            t = t0 * tsign + offset
            output = np.zeros((l2, 2))
            output[:l1, :] = coords1[:, :] + (coords2[:l1, :] - coords1[:, :]) * t
            output[l1:l2, :] = coords1[l1, :] + (coords2[l1:l2, :] - coords1[l1, :]) * t
            return output

        return parametrise
    else:
        def parametrise(t0):
            t = t0 * tsign + offset
            output = np.zeros((l2, 2))
            output[:l1, :] = coords1[:, :] + (coords2[:l1, :] - coords1[:, :]) * t
            output[l1:l2, :] = coords1[l1, :] + (coords2[l1:l2, :] - coords1[l1, :]) * t
            return output

        return parametrise


#
# print(test_code2)
# print(pathToCurve(test_code2))


class Bezier:
    def __init__(self, order, points):
        if order != len(points) + 1:
            print(f'Error must input {order} control points, {len(points)} given.')
            pass
        self.order = order
        self.points = points


def path2svg(vertices, codes):
    svgpath = ''
    index = 0
    for i, cc in enumerate(codes):
        if i == 0 and cc == 2:
            svgpath += 'M '
            svgpath += f'{vertices[index,0]}, {vertices[index,1]}'
            index += 1
        elif cc == 2:
            svgpath += 'L '
            svgpath += f'{vertices[index,0]}, {vertices[index,1]}'
            index += 1
        elif cc == 4:
            svgpath += 'Q '
            svgpath += f'{vertices[index,0]}, {vertices[index,1]} {vertices[index+1,0]}, {vertices[index+1,1]}'
            index += 2

        elif cc == 6:
            svgpath += 'Q '
            svgpath += f'{vertices[index,0]}, {vertices[index,1]} {vertices[index+1,0]}, {vertices[index+1,1]} {vertices[index+2,0]}, {vertices[index+2,1]}'
            index += 3
        else:
            print('Something went wrong with svgreparsing')
        print(index)
    return svgpath
        # elif PARAMS[cc] == 'A':
        #     svgpath += 'A '
        #     svgpath += f'{vertices[index, 0]}, {vertices[index, 1]} {vertices[index + 1, 0]}, {vertices[index + 1, 1]} {vertices[index + 2, 0]}, {vertices[index + 2, 1]}'
        #     index += 3

test_code3 = '''M 10 315 L 110 215 A 30 50 0 0 1 162.55 162.45 L 172.55 152.45L 315 10'''
ppt = parse_path(test_code3)

# print(ppt.point)

def Path2svg(path):
    svgpath = ''
    for p in path:
        if isinstance(p, Line):
            start = p.start
            end = p.end
            svgpath += f'L {start.real}, {start.imag}  {end.real}, {end.imag}'
        elif isinstance(p, Move):
            start = p.start
            svgpath += f'M {start.real}, {start.imag}'
        elif isinstance(p, QuadraticBezier):
            start = p.start
            control = p.control
            end  = p.end
            smooth = p.smooth
            if smooth:
                svgpath += f'Q {start.real}, {start.imag} {control.real}, {control.imag} {end.real}, {end.imag}'
            else:
                svgpath += f'T {start.real}, {start.imag} {control.real}, {control.imag} {end.real}, {end.imag}'
        elif isinstance(p, QuadraticBezier):
            start = p.start
            control1 = p.control1
            control2 = p.control2
            end  = p.end
            smooth = p.smooth
            if smooth:
                svgpath += f'C {start.real}, {start.imag} {control1.real}, {control2.imag} {control2.real}, {control2.imag} {end.real}, {end.imag}'
            else:
                svgpath += f'S {start.real}, {start.imag} {control1.real}, {control2.imag} {control2.real}, {control2.imag} {end.real}, {end.imag}'
        elif isinstance(p, Arc):
            start = p.start
            end = p.end
            radius = p.radius
            rotation = p.rotation
            arc = p.arc
            sweep = p.sweep
            svgpath += f'M {start.real}, {start.imag}'
            svgpath += f'A {radius.real}, {radius.imag} {rotation} {int(arc)} {int(sweep)}'

    return svgpath


def path2points(path):
    'converts the path object into a 2d array of points to be morphed'
    points = []
    for p in path:
        if isinstance(p, Move):
            points.append(p.start)
        elif isinstance(p, Line):
            points.append(p.start)
            points.append(p.end)
        elif isinstance(p, QuadraticBezier):
            points.append(p.start)
            points.append(p.control)
            points.append(p.end)
        elif isinstance(p, CubicBezier):
            points.append(p.start)
            points.append(p.control1)
            points.append(p.control2)
            points.append(p.end)
        elif isinstance(p, Arc):
            points.append(p.start)
            points.append(p.end)
    arr = np.array(points)
    return np.stack((arr.real, arr.imag), axis=1)

def points2path(path, points):
    'converts the points object into a 2d array of points to be morphed'
    i = 0
    for k, p in enumerate(path):
        if isinstance(path[k], Move):
            path[k].start = points[i,0] + points[i,1]*1j
            i += 1
        elif isinstance(p, Line):
            path[k].start = points[i,0] + points[i,1]*1j
            path[k].end = points[i+1,0] + points[i+1,1]*1j
            i += 2
        elif isinstance(p, QuadraticBezier):
            path[k].start = points[i,0] + points[i,1]*1j
            path[k].control = points[i+1,0] + points[i+1,1]*1j
            path[k].end = points[i+2,0] + points[i+2,1]*1j
            i += 3
        elif isinstance(p, CubicBezier):
            path[k].start = points[i,0] + points[i,1]*1j
            path[k].control1 = points[i+1,0] + points[i+1,1]*1j
            path[k].control2 = points[i+2,0] + points[i+2,1]*1j
            path[k].end = points[i+3,0] + points[i+3, 1]*1j
            i += 4
        elif isinstance(p, Arc):
            path[k].start = points[i,0] + points[i,1]*1j
            path[k].end = points[i+1,0] + points[i+1,1]*1j
            i += 2
    return path





print(path2points(ppt))


print((ppt))
print(points2path(ppt, path2points(ppt)))



import numpy as np


def morph(coords1, coords2, style='linear'):
    if len(coords1) > len(coords2):
        coords1, coords2 = coords2, coords1
        tsign = - 1
        offset = 1
    else:
        tsign = 1
        offset = 0

    l1 = len(coords1)
    l2 = len(coords2)

    if style == 'linear':
        def parametrise(t0):
            t = t0 * tsign + offset
            output = np.zeros((l2, 2))
            output[:l1, :] = coords1[:, :] + (coords2[:l1, :] - coords1[:, :]) * t
            output[l1:l2, :] = coords1[l1, :] + (coords2[l1:l2, :] - coords1[l1, :]) * t
            return output
        return parametrise
    else:
        def parametrise(t0):
            t = t0 * tsign + offset
            output = np.zeros((l2, 2))
            output[:l1, :] = coords1[:, :] + (coords2[:l1, :] - coords1[:, :]) * t
            output[l1:l2, :] = coords1[l1, :] + (coords2[l1:l2, :] - coords1[l1, :]) * t
            return output
        return parametrise



class SVGPathObject:
    def __init__(self, type, coordinates, fill=None, stroke=None, strokewidth=1):
        self.type = type
        self.coordinates = coordinates
        self.fill = fill
        self.stroke = stroke

    def morph_to(self, other):
        pass





# print(Path2svg(ppt))
# print(ppt.vertices)
#
#
#
#
# print(len(ppt.codes), len(ppt.vertices))
#
#
# print(path2svg(ppt.vertices, ppt.codes))