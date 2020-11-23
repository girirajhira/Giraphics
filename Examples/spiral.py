from giraphics.graphing.graph import *
import numpy as np

f = Graph(1000, 1000, 5, 5, "spiral.svg")
f.bg(colour="black")

t = np.linspace(0, 40*np.pi, 1600)
X = np.sin(t)*((t**0.9))/50
Y = np.cos(t)*((t**0.9))/50
inital_state = np.random.randint(0,high=3, size=(100,100))
cols = {0: "blue", 1: "red", 2:"green"}
print(cols[inital_state[1][2]])
f.draw_rect(4, 2, 1, 1, cols[inital_state[1][2]])

f.scatter(X, Y, colour="white")
f.save()
f.display()