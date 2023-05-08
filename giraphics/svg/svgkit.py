# Dependencies #
import math
import numpy as np
from giraphics.utilities.utils import getAngle


class SVG:
    def __init__(self, path, width, height, transform="none", grouped=False):
        """Arguments
            path (String): Where the SVG will be saved
            width (Int): Width of the SVG
            height (Int): Height of the SVG
        """
        self.grouped = grouped
        self.path = path
        self.definitions = []
        self.transform = transform
        self.canvas = ""
        if grouped:
            self.canvas += f'<g transform="none"> \n'

        if transform != 'none':
            grouped = True
            self.canvas += f'<g transform="{transform}"> \n'

        self.canvas += f'<svg version="1.1" \n baseProfile="full" \n width="{width}" \n height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        self.preamble = self.canvas


    def draw_rect(self, x, y, width, height, fill, stroke="black", strokewidth=0, opacity=1, fill_opacity=1):
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
        self.canvas += f'<rect x="{x - width / 2}" y="{y - height / 2}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="{strokewidth}" opacity="{opacity}" fill-opacity="{fill_opacity}"/>\n'

    def draw_circ(self, x, y, r, fill="none", stroke="black", strokewidth=1, fill_opacity=1, opac=1):
        """
        Draws a circle of radius r at (x,y)
        :param fill_opacity:
        :param x: x position
        :param y: y position
        :param r: radius
        :param fill: fill colour
        :param stroke: stroke colour
        :param strokewidth: stroke_width
        :param opac: opacity
        """
        self.canvas += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{strokewidth}" fill-opacity="{fill_opacity}" opacity="{opac}"/>\n'

    def draw_ellipse(self, x, y, rx, ry, fill, stroke="black", strokewidth=1, fill_opacity=1, ):
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
        self.canvas += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{strokewidth} fill-opacity="{fill_opacity}"/>\n'

    def draw_line(self, x1, y1, x2, y2, stroke="black", strokewidth="1", opacity="1", cap="butt", style=None):
        """
        Draws a line between (x1,y1) and (x2, y2).
    """
        style_dict = {'dotted': '5,5', 'dashed': '10,10'}
        if style is None:
            self.canvas += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{strokewidth}" opacity="{opacity}" />\n'
        else:
            if style in style_dict.keys():
                self.canvas += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{strokewidth}" opacity="{opacity}" stroke-linecap="{cap}"  stroke-dasharray="{style_dict[style]}"/>\n'
            else:
                self.canvas += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{strokewidth}" opacity="{opacity}" stroke-linecap="{cap}"  stroke-dasharray="{style}"/>\n'

    def draw_dotted_line(self, x1, y1, x2, y2, marker="-", stroke="black", strokewidth="1", opacity="1", cap="butt",
                         segments=20):
        dx, dy = abs((x1 - x2) / (2 * segments)), abs((y1 - y2) / (2 * segments))
        sx1, sy1 = x1, y1
        for s in range(segments * 2):
            if s % 2 == 0:
                if marker == "-":
                    self.canvas += '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" opacity="%s" stroke-linecap="%s"/>\n' % (
                        sx1, sy1, sx1 + dx, sy1 + dy, stroke, strokewidth, opacity, cap)
                elif marker == ".":
                    self.canvas += '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" fill-opacity="%s"/>\n' % (
                        sx1, sy1, dx / 7, stroke, stroke, strokewidth, opacity)

            sx1 += dx
            sy1 += dy

    def draw_arrowhead(self, x: float, y: float, scale: float, rot: float, colour: str = "black") -> None:
        rot = (rot - math.pi)
        R = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
        o = np.array([x, y]).T
        p10 = np.array([-4, -9]).T
        p20 = np.array([0, 0]).T
        p30 = np.array([4, -9]).T
        p40 = np.array([0, -7]).T
        p1, p2, p3, p4 = (R @ p10).T * scale + o, (R @ p20).T * scale + o, (R @ p30).T * scale + o, (
                    R @ p40).T * scale + o
        self.canvas += '<polygon points="%s %s, %s %s, %s %s, %s %s" fill="%s"/>' % (
            p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], colour)

    def draw_arrowhead2(self, x: float, y: float, scale: float, rot: float, colour: str = "black") -> None:
        rot = (rot - math.pi)
        R = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
        o = np.array([x, y]).T

        p10 = np.array([-3, -6]).T
        p20 = np.array([0, 0]).T
        p30 = np.array([3, -6]).T
        p40 = np.array([0, -6]).T
        p1, p2, p3, p4 = (R @ p10).T * scale + o, (R @ p20).T * scale + o, (R @ p30).T * scale + o, (
                    R @ p40).T * scale + o
        self.canvas += '<polygon points="%s %s, %s %s, %s %s, %s %s" fill="%s"/>' % (
            p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], colour)

    def draw_arrow(self, x1, y1, x2, y2, scale=1, stroke="black", strokewidth="1"):
        ang = getAngle(x1, y1, x2, y2)
        l0 = .96 * 7 * scale
        length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if length != 0:
            self.draw_line(x1, y1, (x2 - x1) * (1 - l0 / length) + x1, (y2 - y1) * (1 - l0 / length) + y1, stroke, strokewidth)
            self.draw_arrowhead(x2, y2, scale, ang, stroke)

    def draw_arrow2(self, x1, y1, x2, y2, scale=1, stroke="black", strokewidth="1"):
        ang = getAngle(x1, y1, x2, y2)
        l0 = .96 * 3 * scale
        length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if length != 0:
            self.draw_line(x1, y1, (x2 - x1) * (1 - l0 / length) + x1, (y2 - y1) * (1 - l0 / length) + y1, stroke, strokewidth)
            self.draw_arrowhead2(x2, y2, scale, ang, stroke)

    def draw_polygon(self, X, Y, fill='none', stroke='black', strokewidth=1, opacity=1):
        if len(X) != len(Y):
            raise Exception("Input arrays must be of the same size")
        points = ''
        for i in range(len(X)):
            for j in range(len(Y)):
                points += f'{X[i]},{Y[i]} '
        self.canvas += f'<polygon points="{points}" style="fill:{fill};stroke:{stroke};stroke-width:{strokewidth};fill-opacity:{opacity}"/>\n'

    def draw_polyline(self, X, Y, colour="red", strokewidth="2", opac=1, fill="none", style='none', fill_opacity = 1):
        self.canvas += '<polyline points="'
        start = True
        for i in range(len(X)):
            if Y[i] != None and X[i] != None:
                start = True
                self.canvas += f'{X[i]}, {Y[i]} '
            else:
                if start:
                    self.canvas += f'" stroke="{colour}" stroke-width="{strokewidth}" stroke-linejoin="round" stroke-opacity="{opac}" fill="{fill}" stroke-dasharray="{style}" fill-opacity="{fill_opacity}"/>\n'
                    self.canvas += '<polyline points="'
                start = False
        if not start:
            self.canvas += '-1,1'
        self.canvas += f'" fill="{fill}" stroke="{colour}" stroke-width="{strokewidth}" stroke-linejoin="round" stroke-opacity="{opac}"  stroke-dasharray="{style}" fill-opacity="{fill_opacity}"/>\n'

    def draw_path(self, path, colour="red", strokewidth="2", opac=1, fill="none", fill_opacity = 0):
        self.canvas += f'<path d="{path}" stroke="{colour}" stroke-width="{strokewidth}" fill="{fill}" opacity="{opac}" fill-opacity="{fill_opacity}"/>\n'



    # def text(self, expr,x, y,  fontsize = 14, colour = 'white', rotation=0, opacity = 0, fontfamily = 'sans-serif', centre_align = False):
    #     scale = 1
    #     mata = scale * np.cos(rotation)
    #     matc = scale * np.sin(rotation)
    #     matb = -scale * np.sin(rotation)
    #     matd = scale * np.cos(rotation)
    #     if centre_align:
    #         mate = self.width / 2 + x* self.xscale - scale * (
    #                 np.cos(rotation) * w_expr + np.sin(rotation) * h_expr) / 2
    #         matf = self.height / 2 - y * self.yscale - scale * (
    #                 -np.sin(rotation) * w_expr + np.cos(rotation) * h_expr) / 2
    #     else:
    #         mate = self.width / 2 + x0 * self.xscale
    #         matf = self.height / 2 - y0 * self.yscale
    #     self.svg.canvas += f'<g transform="matrix({mata}, {matb},{matc}, {matd}, {mate}, {matf})">\n'
    #
    #     self.canvas += '

    def draw_arc(self, x, y, r, start, stop, colour="red", strokewidth="2", opac=1, fill="none", fixflag=False):
        xstart, ystart = x + r * np.sin(start + math.pi / 2), y + r * np.cos(start + math.pi / 2)
        xstop, ystop = x + r * np.sin(stop + math.pi / 2), y + r * np.cos(stop + math.pi / 2)
        if not fixflag:
            if abs(start - stop) < math.pi / 2:
                laflag = 0
            else:
                laflag = 1
        else:
            laflag = fixflag
        if (start - stop) < 0:
            sweep = 0
        else:
            sweep = 1
        path = f'M {round(xstart, 2)} {round(ystart, 2)} A {r} {r} 0 {laflag} {sweep}  {round(xstop, 2)} {round(ystop, 2)}'
        self.canvas += f'<path d="{path}" stroke="{colour}" stroke-width="{strokewidth}" fill="{fill}" opacity="{opac}"/>\n'

    def draw_path_line(self, x_list, y_list, colour="red", strokewidth="2"):
        self.canvas += '<path d="'
        for i in range(len(x_list)):
            self.canvas += 'L%s, %s ' % (x_list[i], y_list[i])
        self.canvas += '" fill="none" stroke="%s" stroke-width="%spx"/>\n' % (colour, strokewidth)

    def embed_image(self, x, y, width, height, href):
        self.canvas += f'<image x="{x}" y="{y}" width="{width}" height="{height}" href="{href}"/>'

    def save(self, write_out=True):
        if not self.grouped:
            self.canvas += '\n </svg>'
        else:
            self.canvas += '\n </svg> \n </g>'

        if write_out:
            f = open(self.path, "w")
            f.write(self.canvas)
            f.close()
