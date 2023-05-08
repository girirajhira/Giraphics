import numpy as np


def vec_to_hex(x):
    h = "#"
    for i in x:
        if i > 255 or i < 0:
            print("Invalid: values must be positive and less than 256", i)
            return None
        elif i < 16:
            h += "0" + str(hex(int(round(i))))[-1:]
        else:
            h += str(hex(int((round(i)))))[-2:]
    return h


def hex_to_vec(h):
    h1, h2, h3, = int(h[1:3], 16), int(h[3:5], 16), int(h[5:], 16)
    return [h1, h2, h3]


def norm(x):
    t = 0
    for v in x:
        t += v ** 2
    return t ** (0.5)


def max(x):
    m = 0
    for i in range(len(x)):
        if x[m] < x[i]:
            m = i
    return x[m]


def linear(init, end):
    '''deprecated'''
    init = np.array(init)
    end = np.array(end)

    def f(s):
        return vec_to_hex(init + (end - init) * s)

    return f


def colourScale(start_colour, end_colour):
    if isinstance(start_colour, str):
        start_colour = hex_to_vec(start_colour)
    if isinstance(end_colour, str):
        end_colour = hex_to_vec(start_colour)

    def f(t):
        return vec_to_hex(init + (end - init) * s)

    return f


class Colours:
    def __init__(self):
        pass


class colorObj:
    def __init__(self, colour):
        if isinstance(colour, str):  # if hexadecimal code
            if colour[0] == '#':
                self.colour = hex_to_vec(colour)
            else:
                pass
        elif isinstance(colour, list) or isinstance(colour, np.ndarray):
            self.colour = np.array(colour)

    def __add__(self, other):
        if isinstance(other, colorObj):
            return colorObj(self.colour + other.colour)
        else:
            return colorObj(self.colour + other)

    def __rmul__(self, other):
        self.colour *= other
        return self

    def __mul__(self, other):
        self.colour *= other
        return self

    def __neg__(self):
        self.colour *= -1
        return self

    def hex(self):
        return vec_to_hex(self.colour)


Blues = Colours()
Reds = Colours()
Greens = Colours()
Monotones = Colours()

# Defining colours
Reds.salmon = '#FA8072'
Blues.teal = '#008080'
Blues.aquamarine = '#7FFFD4'
Greens.pine = '#01796f'
Reds.maroon = '#c32148'
Reds.coral = '#FF7F50'
Blues.royal = '#4169E1'
Monotones.silver = '#C0C0C0'
Greens.spring = '#89DA59'
Blues.stone = '#336B87'
Greens.seafoam = '#C4DFE6'
Reds.crimson = '#8D230F'
Greens.olive = '#8EBA43'
