from giraphics.graphing.graph import *
from giraphics.utilities.convert import *
from math import sin

timeSteps = 300
spaceMesh = 300
ca = 0.990632
cb = 374.974
db = 0.00265442
dx = 0.00499654
dt = 1.66667*10**(-11)
w = 6.28319*10**(9)
c = 2.99792*10**8
mu = 1.25664*10**(-6)
eField = np.zeros(spaceMesh)
hField = np.zeros(spaceMesh-1)
eList = [eField]
hList = [hField]
x = np.arange(0, (spaceMesh-1)*dt, dt)


def source(t):
    total = 0
    for n in range(0,12):
        total += sin((2*n+1)*w*t)/(2*n+1)
    return total

for t in range(timeSteps):
    eField[0] =0
    boundary = eField[-2]
    eFieldNext = ca*eField[1:-1] + cb*(hField[1:]- hField[0:-1])
    eField = np.concatenate([[sin(w*t*dt)], eFieldNext, [boundary]])
    hField = hField + db*(eField[1:] - eField[0:-1])
    eList.append(eField)
    hList.append(hField)

'''


G = Graph(1600, 1600, 5 * 10 ** (-9)/2, 2, "savee.svg", origin=[-5 * 10 ** (-9)/2, 0])
G.bg("black")
G.graph_points(x, mu*c*np.array(hList[700]), colour="white", strokewidth=2)
G.graph_points(x, (eList[700][:-1]), colour="yellow", strokewidth=2)

G.save()
'''


#'''
create_directory("ftp")
create_directory("ftprast")


for j in range(0, timeSteps):
    G = Graph(1600, 1600, 4*10**(-9)/2,2, "ftp/g"+namer(j)+".svg", origin=[-4*10**(-9)/2,0])
    G.bg("black")
    G.graph_points(x, mu*c*np.array(hList[j]), colour="white", strokewidth=2)
    G.graph_points(x, (eList[j][:-1]), colour="yellow", strokewidth=2)
    G.save()

create_raster_batch("ftp", 'g', 'p', 'ftprast', timeSteps)
create_mpeg('fdtd5.mp4', 'p', timeSteps, dir=os.getcwd()+"/ftprast")
#'''