from giraphics.graphing.fancygraph import *
from giraphics.animate import *
import numpy as np


elements = []
def plot_surface(func, X, Y):
    Z = func(X,Y)
    return np.array([X,Y,Z])

a = Animation()
a = Animation()