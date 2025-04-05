import numpy as np


def vec_to_hex(x):
    h = "#"
    x = np.round(x,2)
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


class ColourObj:
    '''
    Colour object useful for a bunch of things
    '''
    def __init__(self, colour):
        self.opacity = 1.0  # default opacity

        if isinstance(colour, str):  # Hexadecimal color code
            if colour.startswith('#') and len(colour) == 7:
                self.colour = hex_to_vec(colour)
                self.hex = colour
            else:
                raise ValueError("Invalid hex color format.")

        elif isinstance(colour, (list, np.ndarray)):
            colour = np.array(colour)
            if colour.size == 3:
                self.colour = colour
                self.hex = vec_to_hex(colour)
            elif colour.size == 4:
                self.colour = colour[:3]
                self.opacity = colour[3]
                self.hex = vec_to_hex(self.colour)

            else:
                raise ValueError("List or array must have 3 (RGB) or 4 (RGBA) elements.")

        else:
            raise TypeError("Invalid input type for colour.")



def generate_cmap(color_list, ratios=None):
    colors = np.array([c.colour for c in color_list])
    opacities = np.array([c.opacity for c in color_list])

    if ratios is None:
        ratios = np.linspace(0, 1, len(colors))
    else:
        ratios = np.array(ratios)
        ratios = (ratios - ratios[0]) / (ratios[-1] - ratios[0])  # normalize ratios
    def cmap(t):
        t = np.clip(t, 0, 1)
        interpolated_colors = []
        interpolated_opacities = []
        for val in t:
            idx = np.searchsorted(ratios, val, side='right') - 1
            idx = np.clip(idx, 0, len(colors) - 2)
            frac = (val - ratios[idx]) / (ratios[idx + 1] - ratios[idx])
            interp_color = (1 - frac) * colors[idx] + frac * colors[idx + 1]
            interp_opacity = (1 - frac) * opacities[idx] + frac * opacities[idx + 1]
            interpolated_colors.append(vec_to_hex(interp_color))
            interpolated_opacities.append(interp_opacity)
        return interpolated_colors, interpolated_opacities
    return cmap

    def __add__(self, other):
        if isinstance(other, ColourObj):
            return ColourObj(self.colour + other.colour)
        else:
            return ColourObj(self.colour + other)

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
Blues.royal = '#4169E1'
Blues.stone = '#336B87'

Reds.maroon = '#c32148'
Reds.coral = '#FF7F50'
Reds.crimson = '#8D230F'

Greens.spring = '#89DA59'
Greens.pine = '#01796f'
Greens.seafoam = '#C4DFE6'
Greens.olive = '#8EBA43'

Monotones.silver = '#C0C0C0'
