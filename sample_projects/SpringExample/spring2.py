from giraphics.graphing.Scenic import *
from giraphics.utilities.convert import *

frames = 250 + 1
create_directory("ftp")
create_directory("ftprast")

def y(t):
    return 5*math.sin(t)

def yg(s):
    def y(t):
        return 5 * math.sin(t/30 - s)
    return y

for i in range(frames):
    t = i/30
    # Setup
    A = Scene(1980, 1080, 16, 9,"ftp/g"+namer(i)+".svg", origin=[0,0])
    A.bg(colour="black")
    g = Widget(10, 10, A, pos=[-8,0], scale=[0.5,1], origin=[-10,0])
    # Graph
    g.grid()
    g.axes("yellow")
    g.graph(yg(t), colour="yellow")
    # Pendulum drawing
    A.draw_rect(0,y(t), 1.5, 1.5, fill="white")
    A.draw_line(0,0, 0, y(t), stroke="white")
    A.draw_line(-8,y(t), 0, y(t), stroke="red")
    # Savings
    A.commitWidget(g)
    A.save()

# Converting SVG to PNG
create_raster_batch("ftp", 'g', 'p', 'ftprast', frames)
# Creating the final video
create_mpeg('Springs5.mp4', 'p', frames, dir=os.getcwd() + "/ftprast", framerate=60)
