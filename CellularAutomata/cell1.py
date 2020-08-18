from graph import Graph
from convert import *
import numpy as np
gg = Graph(1000,1000,100,100,namer(1) + ".svg")

cols = {0: "blue", 1: "red"}

cells = 30
class Auto:
    def __init__(self, initial_state):
        self.state = initial_state
        self.height = 500
        self.id = initial_state
        self.width = 500
        self.xlim = cells
        self.ylim = cells

    def check_cell(self, i, j):
        total = 0
        for k in range(-1, 2,2):
            for l in range(-1,2,2):
                if (self.state[i][j]+1)%2 == self.state[i + k][j + l]:
                    total += 1
                elif (self.state[i][j])%2 == self.state[i + k][j + l]:
                    total += 1

            return total


    def __update(self):
        for i in range(self.state.shape[0]):
            for j in range(self.state.shape[1]):
                if j != 0 and j != self.state.shape[1]-1:
                    if i != 0 and i != self.state.shape[0]-1:
                        if self.state[i][j] == 1:
                            if (self.check_cell(i, j)) >= 4:
                                self.state[i][j] = (self.state[i][j])%2
                            elif (self.check_cell(i, j)) >= 0:
                                self.state[i][j] = (self.state[i][j]+1)%2
                        if self.state[i][j] == 0:
                            if (self.check_cell(i, j)) < 0:
                                self.state[i][j] = (self.state[i][j])%2




    def create_movie(self,frames = 50):
        create_directory("ftp")
        create_directory("ftprast")
        for i in range(frames):
            g = Graph(self.width, self.height, self.xlim, self.ylim, "ftp/g"+namer(i)+".svg", origin=[-self.xlim, -self.ylim])
            g.svg.canvas = '<svg version="1.1" \n baseProfile="full" \n width="' + str(
                self.width) + '" \n height="' + str(
                self.height) + '" \n xmlns="http://www.w3.org/2000/svg">\n'
            for j in range(1, 2*self.xlim-1):
                for k in range(1, 2*self.ylim-1):
                    g.draw_rect(j, k, 1, 1, cols[self.state[j][k]])
            g.save()
            self.__update()
        create_raster_batch("ftp", 'g', 'p', 'ftprast', num=frames)
        create_mpeg('c9.mp4', 'p', frames, dir=os.getcwd() + "/ftprast", framerate=4)


inital_state = np.random.randint(0, high=2, size=(2*cells, 2*cells))
# inital_state = np.full((20,20), 0, dtype=int)
a = Auto(inital_state)
a.create_movie()

