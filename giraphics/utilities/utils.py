import numpy as np
from math import cos, sin, atan, pi, atan2

import time


class Timer:
    """
    Times code between the start() and stop()
    """

    def __init__(self, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger

    def start(self, label="task"):
        """
        Starts the timer when run
        :param label: Label of the timer
        """
        self.label = label
        self.t1 = time.time()

    def stop(self):
        """
        Stops the timer when run and prints the time taken to complete the task
        :return:
        """
        self.t2 = time.time()
        print("Time lapsed for %s: %s" % (self.label, self.t2 - self.t1))


def listlike(var):
    """
    Takes a variable and returns the variable in a list if it is not already a list
    :param var: variable
    :return: List
    """
    if isinstance(var, list):
        return var
    else:
        return [var]


def getAngle(x1, y1, x2, y2):
    if x1 - x2 != 0:
        if x1 - x2 < 0:
            ang = atan((y2 - y1) / (x2 - x1)) + pi / 2
        else:
            ang = atan((y2 - y1) / (x2 - x1)) - pi / 2
    else:
        if y2 - y1 < 0:
            ang = 0
        else:
            ang = pi
    return ang


def max2d(arr):
    m, n = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] >= arr[m][n]:
                m, n = i, j
    return arr[m, n]


def min2d(arr):
    m, n = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] <= arr[m][n]:
                m, n = i, j
    return arr[m, n]


# Velocity Distribution
def identity(t):
    return t


def TopHeavy(i, k=4):
    return i ** k


def BottomHeavy(i, k=0.25):
    return i ** k


def Linear():
    pass


def Taper(self):
    pass


def Bounce(self):
    pass


def colourgradient(self, s):
    return "white"


def norm(x):
    t = 0
    for v in x:
        t += v ** 2
    return t ** (0.5)


def parity(x):
    if x >= 0:
        return 1
    else:
        return -1


# Rotations 3D
def Rx(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])
    pass


def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])
