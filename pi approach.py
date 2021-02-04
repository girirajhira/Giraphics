import math
import numpy as np
from scipy.linalg import expm
from scipy.special import eval_hermite
from scipy.integrate import odeint, solve_bvp
# from scipy.signal import find_peaks
from numpy.linalg import norm
import matplotlib.pyplot as plt

from giraphics.animate.animation import Animation

# Parameters
N = 40  # Dimension of the hilbert space
h = 1  # hbar
m = 1
w = 1  # omega
alpha = 0.0
p = 2
beta = 0.001  # strength of quartic
intervals = 50  # space intervals
X = np.linspace(-7.5, 7.5, intervals)  # Space
time_intervals = 1000
time_step = 0.01
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


def Action(x, v, param=beta):
    A = (0.5 * m * np.power(v, 2) - 0.5 * m * w * w * np.power(x, 2) - param * np.power(x, 4))
    return np.array([np.sum(A[:t]) * time_step / (h) + (1 / (2 * h)) * x[t] * v[t] for t in range(time_intervals)])

def compute_action(x, v, param=beta):
    A = (0.5 * m * np.power(v, 2) - 0.5 * m * w * w * np.power(x, 2) - param * np.power(x, 4))
    return np.sum(A) * time_step


def quartic(vals, t, param=beta):
    x, v = vals
    dvdt = [v, -w * w * x - 4 * param * np.power(x, 3) / m]
    return dvdt


### Evolving ###

(eigenvals, eigenvectors) = np.linalg.eigh(H)

groundstate = eigenvectors[np.argmin(eigenvals)]
excited = np.zeros(N)
excited[1] = 1


psi0 = eigenvectors[0]
psi = psi0/norm(psi0)

psi_kick = D@psi
time_evo_raw = np.array([ U(k * time_step)@ psi_kick for k in range(0, time_intervals, 1)])
time_evo_pos = np.array([time_evo_raw[k].T @ hermite_array(X) for k in range(0,time_intervals,1)])


X2 = []
Acts = []

for x in X:
    iv = [x, p/ m]
    sol = odeint(quartic, iv, T, args=(beta,))
    pos = sol[:, 0]
    vel = sol[:, 1]
    action_cl = Action(pos, vel)
    X2.append(pos)
    Acts.append(action_cl)

X2 = np.array(X2).T
Acts = np.array(Acts).T

print(X2.shape)
print(hermite_array(X2[0]).shape)

hydro_approx = [(psi@hermite_array(X2[j])*np.exp(1j*Acts[j]/h)) for j in range(time_intervals)]


A = Animation('QHO_kick_eigen15.mp4', time_intervals, 1980, 1080, 10, 1, origin=[0,-.8])

for i in range(time_intervals):
    A.plate.bg()
    for j in range(len(X2[i])):
        A.plate.draw_line(X[j], -.3, X2[i][j],  0,colour='white', opacity=0.4)
    A.plate.graph_points(X, np.abs(time_evo_pos[i]))
    A.plate.graph_points(X, np.abs(hydro_approx[i]), colour='blue')

    A.plate.press()

A.develop()
