def dipole_field(x, y, m=(0, 1)):
    r = np.sqrt(x ** 2 + y ** 2)
    r5 = r ** 5
    m_dot_r = m[0] * x + m[1] * y

    Bx = (3 * m_dot_r * x) / r5 - m[0] / (r ** 3)
    By = (3 * m_dot_r * y) / r5 - m[1] / (r ** 3)

    return Bx, By


from giraphics.graphing.fancygraph import FancyGraph
import numpy as np

width = 600
height = 600
xlim = 1.6
ylim = 1.6

nx = 26
ny = 26

x = np.linspace(-xlim, xlim,nx)*1.1
y = np.linspace(-ylim, ylim,ny)*1.1

X, Y = np.meshgrid(x, y)

U, V = dipole_field(X, Y)

G = FancyGraph(width, height, xlim, ylim, 'magnetic_dipole.svg', origin=[0, 0])
t = np.linspace(-xlim, xlim, 600)
G.bg(colour='black')  # Plots black background
# G.axes(colour='white',strokewidth=.5)
G.grid2(strokewidth=.2, colour="white")
G.VectorField(X,Y,U,V, tail_length=1, constLength=True)

G.save()

