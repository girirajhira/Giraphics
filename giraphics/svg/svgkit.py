# Dependencies #
import math
import numpy as np
# from numba import njit, jit

class SVG:
    def __init__(self, path, width, height, transform="none", grouped=False):
        """Arguments
            path (String): Where the SVG will be saved
            width (Int): Width of the SVG
            height (Int): Height of the SVG
        """
        self.grouped = grouped
        self.path = path
        self.canvas = ""
        if grouped:
            self.canvas += '<g transform="' + str(transform) +'"> \n'

        self.canvas += '<svg version="1.1" \n baseProfile="full" \n width="' + str(
                width) + '" \n height="' + str(
                height) + '" \n xmlns="http://www.w3.org/2000/svg">\n'

    def draw_rect(self, x, y, width, height, fill, stroke="black", strokewidth=0, opacity=1):
        """"
            Draws a rectangle
            Arguments
                x (Float): x component of the centre of the rectangle
                y (Float): y component of the centre of the rectangle
                width (int): Width of the rectangle
                height (int): Height of the rectangle
                fill (String:colour): Colour of the rectangle
            Optional Arguments
                stroke (String:colour): Colour of the stroke
                stroke_width (Float): Stroke width
                opacity (Float:[0,1]): opacity of rectangle
        """
        self.canvas += '<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="%s" opacity="%s"/>\n' % (
            x - width / 2, y - height / 2, width, height, fill, stroke, strokewidth, opacity)

    def draw_circ(self, x, y, r, fill="none", stroke="black", strokewidth=1, opac=1):
        """
        Draws a circle of radius r at (x,y)
        :param x: x position
        :param y: y position
        :param r: radius
        :param fill: fill colour
        :param stroke: stroke colour
        :param strokewidth: stroke_width
        :param opac: opacity
        """
        self.canvas += '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" fill-opacity="%s"/>\n' % (
            x, y, r, fill, stroke, strokewidth, opac)

    def draw_ellipse(self, x, y, rx, ry, fill, stroke="black", strokewidth=1):
        """
        Draws an ellipse at (x,y)  with horizontal radius rx and vertical radius ry.
        :param x: x position
        :param y: y position
        :param rx: horizontal radius
        :param ry: vertial radius
        :param fill: fill colour
        :param stroke: stroke colour
        :param strokewidth: stroke width
        """
        self.canvas += '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" stroke="%s" stroke-width="%s"/>\n' % (
            x, y, rx, ry, fill, stroke, strokewidth)

    def draw_line(self, x1, y1, x2, y2, stroke="black", strokewidth="1", opacity="1", cap="butt"):
        """
        Draws a line between (x1,y1) and (x2, y2).
    """
        self.canvas += '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" opacity="%s" stroke-linecap="%s"/>\n' % (
            x1, y1, x2, y2, stroke, strokewidth, opacity, cap)

    def draw_dotted_line(self, x1, y1, x2, y2, marker="-", stroke="black", strokewidth="1", opacity="1", cap="butt", segments=20):
        dx, dy = abs((x1-x2)/(2*segments)), abs((y1-y2)/(2*segments))
        sx1, sy1 = x1, y1
        for s in range(segments*2):
            if s%2==0:
                if marker=="-":
                    self.canvas += '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" opacity="%s" stroke-linecap="%s"/>\n' % (
                sx1, sy1, sx1+dx, sy1+dy, stroke, strokewidth, opacity, cap)
                elif marker==".":
                    self.canvas += '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" fill-opacity="%s"/>\n' % (
                        sx1, sy1, dx/7, stroke, stroke, strokewidth, opacity)

            sx1 += dx
            sy1 += dy

    def draw_arrowhead(self, x: float, y: float, scale: float, rot: float, colour: str = "black") -> None:
        rot = (rot - math.pi)
        R = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
        o = np.array([x, y]).T
        p1, p2, p3, p4 = np.matmul(R, np.array([-4, -6]).T).T * scale + o, np.matmul(R, np.array(
            [0, 4]).T).T * scale + o, np.matmul(R, np.array([4, -6]).T).T * scale + o, np.matmul(R, np.array(
            [0, -4]).T).T * scale + o
        self.canvas += '<polygon points="%s %s, %s %s, %s %s, %s %s" fill="%s"/>' % (
            p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], colour)

    def draw_arrowhead2(self, x: float, y: float, scale: float, rot: float, colour: str = "black") -> None:
        rot = (rot - math.pi)
        R = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
        o = np.array([x, y]).T
        p1, p2, p3, p4 = np.matmul(R, np.array([-4, -6]).T).T * scale + o, np.matmul(R, np.array(
            [0, 4]).T).T * scale + o, np.matmul(R, np.array([4, -6]).T).T * scale + o, np.matmul(R, np.array(
            [0, -6]).T).T * scale + o
        self.canvas += '<polygon points="%s %s, %s %s, %s %s, %s %s" fill="%s"/>' % (
            p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], colour)

    def draw_arrow(self, x1, y1, x2, y2, scale=1, stroke="black", strokewidth="1"):
        if x1 - x2 != 0:
            if x1 - x2 < 0:
                ang = math.atan((y2 - y1) / (x2 - x1)) + math.pi / 2
            else:
                ang = math.atan((y2 - y1) / (x2 - x1)) - math.pi / 2
        else:
            if y2 - y1 < 0:
                ang = 0
            else:
                ang = math.pi
        self.draw_line(x1, y1, x2, y2, stroke, strokewidth)
        self.draw_arrowhead(x2, y2, scale, ang, stroke)

    def draw_arrow2(self, x1, y1, x2, y2, scale=1, stroke="black", stroke_width="1"):
        if x1 - x2 != 0:
            if x1 - x2 < 0:
                ang = math.atan((y2 - y1) / (x2 - x1)) + math.pi / 2
            else:
                ang = math.atan((y2 - y1) / (x2 - x1)) - math.pi / 2
        else:
            if y2 - y1 < 0:
                ang = 0
            else:
                ang = math.pi
        self.draw_line(x1, y1, x2, y2, stroke, stroke_width)
        self.draw_arrowhead2(x2, y2, scale, ang, stroke)

    def draw_polyline(self, X, Y, colour="red", strokewidth="2", opac=1, fill="none"):
        self.canvas += '<polyline points="'
        start = True
        for i in range(len(X)):
            if Y[i] != None and X[i] != None:
                start = True
                self.canvas += '%s, %s ' % (X[i], Y[i])
            else:
                if start:
                    self.canvas += '" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-opacity="%s" fill="%s" />\n' % (
                        colour, strokewidth, opac, fill)
                    self.canvas += '<polyline points="'
                start = False
        if not start:
            self.canvas += '-1,1'
        self.canvas += '" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-opacity="%s"/>\n' % ( fill,
            colour, strokewidth, opac)

    def draw_path_line(self, x_list, y_list, colour="red", strokewidth="2"):
        self.canvas += '<path d="'
        for i in range(len(x_list)):
            self.canvas += 'L%s, %s ' % (x_list[i], y_list[i])
        self.canvas += '" fill="none" stroke="%s" stroke-width="%spx"/>\n' % (colour, strokewidth)

    def embed_image(self, x, y, width, height, href):
        self.canvas += '<image x="%s" y="%s" width="%s" height="%s" href="%s"/>' % (x, y, width, height, href)

    def save(self, write_out=True):
        self.canvas += '\n </svg>'
        if write_out:
            f = open(self.path, "w")
            f.write(self.canvas)
            f.close()


