import math
import numpy as np
from scipy.linalg import expm
from scipy.special import eval_hermite

# Parameters
from giraphics.graphing.fancygraphs import FancyGraphs
from giraphics.utilities.convert import *

N = 30
h = 0.2
w = 1
alpha = 0.0
beta = 0.01
intervals = 500
X = np.linspace(-10, 10, intervals)
time_intervals=600


# Annihilation operator
def a(n, m):
    if n == m + 1:
        return math.sqrt(n)
    else:
        return 0

# Potential
def potential(x):
    return h * w * np.power(x, 2) + alpha * np.power(x, 3) + beta * np.power(x, 4)

# Array containing <H_i(x)>
def hermite_array(x):
    return np.array(
        [(1 / math.sqrt(2 ** k * math.factorial(k))) * eval_hermite(k, x) * np.exp(-x ** 2 / 2) for k in range(0, N)])

def expectation(x, phi):
    normal = np.sum(phi)
    return np.matmul(x.T,phi)/normal


# Constructing a Basis
basis = []
for i in range(0, N):
    v = np.zeros(N)
    v[i] = 1.0
    basis.append(v)

# Coefficients of the initial state
C = np.zeros(N)
C[0] = 0.29
C[1] = 0.4
C[2] = 0.464
C[3] = 0.362

# Constructing the initial state
psi = np.zeros(N)
for i in range(0, N):
    psi += basis[i] * C[i]

# Constructing a, adag
A = np.array([[a(n, m) for n in range(0, N)] for m in range(0, N)])
Ad = A.T

# Hamiltonian
H = h * w * (np.matmul(Ad, A)) + alpha * np.power(Ad + A, 3) + beta * np.power(Ad + A, 4)


# Unitary operator U
def U(t):
    return expm(-1j * t * H / h)


# Find Eigen(values, vectors)

(vals, vectors) = np.linalg.eig(H)

print('vals=', vals)
print('vecs=', vectors)



#
#
time_evo_raw = np.array([np.matmul(U(k * 0.04), psi) for k in range(0, time_intervals, 1)])
time_evo_pos = np.array([np.matmul(time_evo_raw[k].T, hermite_array(X)) for k in range(0,time_intervals,1)])

# print(np.abs(TimeEvo[0]))


frames = 600
create_directory("ftp")
create_directory("ftprast")

for i in range(frames):
    t = i
    g = FancyGraphs(1000, 1000, 5, 1, "ftp/g" + namer(i) + ".svg", origin=[0, -0.5])
    g.bg("black")
    # g.axes("yellow")

    # #Position Basis
    # g.draw_line(-5, 0, 5, 0, colour="yellow")
    # g.graph_points(X, np.abs(time_evo_pos[t]), colour="white", strokewidth=1.5)
    # g.graph_points(X, (time_evo_pos[t]).real, colour="blue", strokewidth=.8)
    # g.graph_points(X, (time_evo_pos[t]).imag, colour="red", strokewidth=.8)
    # g.graph_points(X, potential(X), colour="yellow", strokewidth=1.2)
    # # ep = expectation(X, np.abs(time_evo_pos[t]))
    # # g.point(ep,potential(ep), s=3, colour="green")

    # Number Basis
    g.histogram(np.abs(time_evo_raw[t]))

    g.save()

# Crating
create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# Creating the final video
create_mpeg('wave11.mp4', 'p', frames, dir=os.getcwd() + "/ftprast", framerate=60)
