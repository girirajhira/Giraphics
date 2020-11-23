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
    h1, h2, h3, = int(h[1:3],16), int(h[3:5],16), int(h[5:],16)
    return [h1,h2,h3]

def norm(x):
    t = 0
    for v in x:
        t += v**2
    return t**(0.5)
def max(x):
    m = 0
    for i in range(len(x)):
        if x[m] < x[i]:
            m = i
    return x[m]

def linear(init, end):
    init = np.array(init)
    end = np.array(end)
    def f(s):
        return vec_to_hex(init + (end - init) * s)
    return f


