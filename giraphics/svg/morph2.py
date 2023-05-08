from giraphics.svg.svgkit import *
from xml.dom import minidom
import numpy as np

from math import floor
import re
# from svgpath2mpl import parse_path
from svg.path import parse_path, Line, Arc, CubicBezier, QuadraticBezier, Move, Path
from giraphics.utilities.colour import colorObj

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


def get_svg_symbol_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('d') for symb in doc.getElementsByTagName('symbol')]
    doc.unlink()
    return symbols


test_code3 = '''M 10 315 L 110 215 A 30 50 0 0 1 162.55 162.45 L 172.55 152.45L 315 10'''
ppt = parse_path(test_code3)


def path2svg(path):
    '''Converts Path obj to svgpathstring - unsure what Arc.end is '''
    svgpath = ''
    for p in path:
        if isinstance(p, Line):
            start = p.start
            end = p.end
            svgpath += f'L {start.real}, {start.imag}  {end.real}, {end.imag} '
        elif isinstance(p, Move):
            start = p.start
            svgpath += f'M {start.real}, {start.imag} '
        elif isinstance(p, QuadraticBezier):
            start = p.start
            control = p.control
            end = p.end
            smooth = p.smooth
            if smooth:
                svgpath += f'Q {start.real}, {start.imag} {control.real}, {control.imag} {end.real}, {end.imag} '
            else:
                svgpath += f'T {start.real}, {start.imag} {control.real}, {control.imag} {end.real}, {end.imag} '
        elif isinstance(p, QuadraticBezier):
            start = p.start
            control1 = p.control1
            control2 = p.control2
            end = p.end
            smooth = p.smooth
            if smooth:
                svgpath += f'C {start.real}, {start.imag} {control1.real}, {control2.imag} {control2.real}, {control2.imag} {end.real}, {end.imag} '
            else:
                svgpath += f'S {start.real}, {start.imag} {control1.real}, {control2.imag} {control2.real}, {control2.imag} {end.real}, {end.imag} '
        elif isinstance(p, Arc):
            start = p.start
            end = p.end
            radius = p.radius
            rotation = p.rotation
            arc = p.arc
            sweep = p.sweep
            svgpath += f'M {start.real}, {start.imag} '
            svgpath += f'A {radius.real}, {radius.imag} {rotation} {int(arc)} {int(sweep)} '
    return svgpath


def convert_points2giraphics(coords, xt, yt):
    return np.array([[xt(coords[i, 0]), yt(coords[i,1])] for i in range(len(coords))])


def convert_points2giraphics2(path, xt, yt):
    'converts the path object into a 2d array of points to be morphed'
    for i, p in enumerate(path):
        if isinstance(p, Move):
            path[i].start = xt(p.start.real) + yt(p.start.imag)*1j
        elif isinstance(p, Line):
            path[i].start = xt(p.start.real) + yt(p.start.imag)*1j
            path[i].end = xt(p.end.real) + yt(p.end.imag)*1j
        elif isinstance(p, QuadraticBezier):
            path[i].start = xt(p.start.real) + yt(p.start.imag)*1j
            path[i].control = xt(p.control.real) + yt(p.control.imag)*1j
            path[i].end = xt(p.end.real) + yt(p.end.imag)*1j
        elif isinstance(p, CubicBezier):
            path[i].start = xt(p.start.real) + yt(p.start.imag)*1j
            path[i].control1 = xt(p.control1.real) + yt(p.control1.imag)*1j
            path[i].control2 = xt(p.control2.real) + yt(p.control2.imag)*1j
            path[i].end = xt(p.end.real) + yt(p.end.imag)*1j
        elif isinstance(p, Arc):
            path[i].start = xt(p.start.real) + yt(p.start.imag)*1j
            path[i].radius = xt(p.radius.real) + yt(p.radius.imag)*1j
            path[i].end = xt(p.end.real) + yt(p.end.imag)*1j
    return path





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
        if isinstance(p, Move):
            path[k].start = points[i, 0] + points[i, 1] * 1j
            i += 1
        elif isinstance(p, Line):
            path[k].start = points[i, 0] + points[i, 1] * 1j
            path[k].end = points[i + 1, 0] + points[i + 1, 1] * 1j
            i += 2
        elif isinstance(p, QuadraticBezier):
            path[k].start = points[i, 0] + points[i, 1] * 1j
            path[k].control = points[i + 1, 0] + points[i + 1, 1] * 1j
            path[k].end = points[i + 2, 0] + points[i + 2, 1] * 1j
            i += 3
        elif isinstance(p, CubicBezier):
            path[k].start = points[i, 0] + points[i, 1] * 1j
            path[k].control1 = points[i + 1, 0] + points[i + 1, 1] * 1j
            path[k].control2 = points[i + 2, 0] + points[i + 2, 1] * 1j
            path[k].end = points[i + 3, 0] + points[i + 3, 1] * 1j
            i += 4
        elif isinstance(p, Arc):
            path[k].start = points[i, 0] + points[i, 1] * 1j
            path[k].end = points[i + 1, 0] + points[i + 1, 1] * 1j
            i += 2

    print('lld',path)
    return path


# print(path2points(ppt))
#
# print((ppt))
# print(points2path(ppt, path2points(ppt)))



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
    print(coords1.shape)
    def parametrise(t0):
        t = t0 * tsign + offset
        output = np.zeros((l2, 2))
        output[:, :] = coords1[:, :] + (coords2[:, :] - coords1[:, :]) * t
        return output

    return parametrise


def transform_control_points(coords1, coords2, t):
    if len(coords1) > len(coords2):
        coords1, coords2 = coords2, coords1
        tsign = - 1
        offset = 1
        l1 = len(coords1)
        l2 = len(coords2)
        coords = np.zeros(coords2.shape)
        coords[:l1, :] = offset + coords1[:, :] + (coords1[:, :] - coords2[:l1, :]) * t * tsign
        coords[l1:l2, :] = offset + coords1[-1, :] + (coords1[-1, :] - coords2[l1:l2, :]) * t * tsign
        return coords
    elif len(coords1) == len(coords2):
        tsign = 1
        offset = 0
        coords = np.zeros(coords2.shape)
        coords[:, :] = offset + coords1[:, :] + (coords1[:, :] - coords2[:, :]) * t * tsign
    else:
        tsign = 1
        offset = 0
        l1 = len(coords1)
        l2 = len(coords2)
        coords = np.zeros(coords2.shape)
        coords[:l1, :] = offset + coords1[:, :] + (coords1[:, :] - coords2[:l1, :]) * t * tsign
        coords[l1:l2, :] = offset + coords1[-1, :] + (coords1[-1, :] - coords2[l1:l2, :]) * t * tsign
    return coords




# def ConstructPath(*args):
#     for a in args:


class SVGPathObject:
    def __init__(self, path, fill=None, stroke=None, strokewidth=1, fill_opacity=1, stroke_opacity=1):
        if isinstance(path, Path):
            self.pathObj = path
            self.path = path2svg(path)
        else:
            self.path = path
            self.pathObj = parse_path(path)
        self.coords = path2points(self.pathObj)
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.stroke_opacity = stroke_opacity
        self.stroke = np.array(stroke)
        self.strokewidth = strokewidth

    def morph_to(self, other, reverse=False):
        if reverse:
            offset = 1
            tsign = -1
        else:
            offset = 0
            tsign = 1



        initStrokeWidth = self.strokewidth
        endStrokeWidth = other.strokewidth

        # coordsFunction = morph(self.coords, other.coords)


        def parametrisation(t):
            # coords = self.coords + (other.coords - self.coords)*t
            # path = points2path(other.path, coordsFunction(t))
            coords = transform_control_points(self.coords, other.coords, t)
            path = points2path(other.pathObj, coords)
            strokewidth = initStrokeWidth + (endStrokeWidth - initStrokeWidth) * t
            return SVGPathObject(path, stroke=self.stroke, strokewidth=strokewidth, fill_opacity=other.fill_opacity,
                                 fill=other.fill)

        return parametrisation

    def draw(self, writerObj):
        writerObj.plate.draw_path(self.path, colour=self.stroke, strokewidth=self.strokewidth, opacity=self.stroke_opacity,
                                  fill=self.fill, fill_opacity=self.fill_opacity)

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
