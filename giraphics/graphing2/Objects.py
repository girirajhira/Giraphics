import numpy as np


class SVG_Object:
    def __init__(self, type, x, y, stroke, strokewidth, stroke_opacity,  colour, opacity, id, transform_arg ):
        self.type = type
        self.x = np.array(x)
        self.y = np.array(y)
        self.stroke = stroke
        self.stroke_opacity = stroke_opacity
        self.opacity = opacity
        self.strokewidth = strokewidth
        self.colour = colour
        self.id = id
        self.transform_arg = transform_arg

    def transform(self):
        '''transforms the coordinates'''
        pass



'''
Want a transform object that in general specifies changes to a SVG_Object's 
property 
'''


class Line(SVG_Object):
    def __init__(self, x, y, stroke, strokewidth, id, caps = 'butt', stroke_opacity = 1, style='None'):
        self.caps = caps
        self.style = style
        super.__init__('Line', x, y, stroke, strokewidth, stroke_opacity, 'none', 1, id, None)

    def transform(self, transform_obj):
        pass

    def write(self, graph_obj):
        graph_obj.draw_line(self.x[0], self.y[0], self.x[1], self.y[1], colour=self.stroke,
                            strokewidth=self.strokewidth, opacity = self.stroke_opacity, cap=self.caps, style = self.style)



class Transform_Obj:
    def __init__(self, coords_transform):
        pass

