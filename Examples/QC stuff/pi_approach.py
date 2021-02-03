import math
import numpy as np
from scipy.linalg import expm
from scipy.special import eval_hermite
from scipy.integrate import odeint, solve_bvp
from scipy.signal import find_peaks
from numpy.linalg import norm

from giraphics.animate.animation import Animation

# Parameters
N = 40  # Dimension of the hilbert space
h = 1  # hbar
m = 1
w = 1  # omega
alpha = 0.0
p = 3
beta = 0.000  # strength of quartic
intervals = 800  # space intervals
X = np.linspace(-7.5, 7.5, intervals)  # Space
time_intervals = 2000
time_step = 0.02
T = np.linspace(0, time_intervals * time_step, time_intervals)


### Functions ###

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
    norml = (m * w / (np.pi * h)) ** (1 / 4)
    fr = math.sqrt(m * w / h)
    return np.array([

        norml * (1 / math.sqrt(2 ** k * math.factorial(k))) * eval_hermite(k, fr * x) * np.exp(-x ** 2 / 2)

        for k in range(0, N)])


def expectation(x, phi):
    normal = np.sum(phi)
    return np.matmul(x.T, phi) / normal


def gamma(t):
    np.abs(matmul(psi_kick.T, matmul(U(t * time_step), psi_kick)))


## Constructions ###


# Constructing a, adag
A = np.array([[a(n, m) for n in range(0, N)] for m in range(0, N)])
Ad = A.T

# Hamiltonian
H = h * w * (Ad @ A + (1 / 2) * np.identity(N)) + beta * np.linalg.matrix_power(Ad + A, 4)
H0 = h * w * (Ad @ A + (1 / 2) * np.identity(N))


# Unitary operator U
def U(t):
    return (expm(-1j * t * H / h))


# Displacement Operator
D = expm(1j * (p / h) * (h / (2 * m * w)) ** 0.5 * (A + Ad))


def Kick(po):
    return expm(1j * (po / h) * (h / (2 * m * w)) ** 0.5 * (A + Ad))


def Phi(par, state):
    return np.angle(state.T.conjugate() @ U(par) @ state)


### Evolving ###

(eigenvals, eigenvectors) = np.linalg.eigh(H)

groundstate = eigenvectors[np.argmin(eigenvals)]
excited = np.zeros(N)
excited[1] = 1


psi = eigenvectors[1]

psi_kick = D@psi

time_evo_raw = np.array([ U(k * time_step)@ psi_kick for k in range(0, time_intervals, 1)])

time_evo_pos = np.array([time_evo_raw[k].T @ hermite_array(X) for k in range(0,time_intervals,1)])


A = Animation('QHO_kick_eigen1.mp4', time_intervals, 1980,1080, 10, 3)

for i in range(time_intervals):
    A.plate.bg()
    A.plate.graph_points(X,np.abs(time_evo_pos[i]))
    A.press()

A.develop()


