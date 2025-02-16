from giraphics.graphing.fancygraph import *


def Rz(theta, r=1):
    return np.array([[cos(theta), -sin(theta), 0],
                     [sin(theta), cos(theta), 0],
                     [0, 0, 1]])

def Rx(theta, r=1):
    return np.array([[1, 0, 0],
                     [0,cos(theta), -sin(theta)],
                     [0,sin(theta), cos(theta)],
                     ])
def Ry(theta, r=1):
    return np.array([[cos(theta), 0, sin(theta)],
                     [0, 1, 0],
                     [-sin(theta), 0, cos(theta)]])
class Isometric(FancyGraph):
    # Default 2d view is the positive z unit vector
    def __init__(self, width, height, xlim, ylim, zlim, name, origin=[0.0, 0.0, 0.0], theme="dark",
                 border_width=0.12, bg="white",view=[0, 0]):
        self.rotmat = Ry(view[1])@Rz(view[0])
        self.zlim = zlim
        zunit = np.array([0,0,1])
        self.new_origin = self.rotmat@ zunit
        Graph.__init__(self, width, height, xlim, ylim, name, theme=theme, origin=origin[:2])

    def draw_line(self, p1, p2, marker="*", colour="black", strokewidth=1, opacity=1, cap="butt",
                  segments=20, style=None):
        pr1 = self.rotmat@ p1
        pr2 = self.rotmat@ p2
        # strokewidth = strokewidth * self.nscale
        Graph.draw_line(self,  (pr1[0]),  (pr1[1]),  (pr2[0]),  (pr2[1]), marker="*", colour=colour, strokewidth=strokewidth, opacity=1, cap=cap,
                segments=20, style=None)
    def grid3(self, num_lines = [3,3, 3], margin =.75, colour = 'grey', opacity = .7, strokewidth=.35):
        xspan = np.linspace(-self.xlim, self.xlim, num_lines[0])
        yspan = np.linspace(-self.ylim, self.ylim, num_lines[1])
        zspan = np.linspace(-self.zlim, self.zlim, num_lines[2])

        for i in range(num_lines[0]):
            for j in range(num_lines[1]):
                for k in range(num_lines[2]):
                    # Xlines
                    x1 = [-self.xlim, yspan[j], zspan[k]]
                    x2 = [ self.xlim, yspan[j], zspan[k]]
                    self.draw_line(x1,x2, colour =colour, opacity=opacity,strokewidth=strokewidth)
                    # Xlines
                    y1 = [xspan[i], -self.ylim, zspan[k]]
                    y2 = [xspan[i], self.ylim, zspan[k]]
                    self.draw_line(y1,y2, colour =colour, opacity=opacity,strokewidth=strokewidth)
                    # Xlines
                    z1 = [xspan[i], yspan[j],-self.zlim,]
                    z2 = [xspan[i], yspan[j], self.zlim]

                    self.draw_line(z1,z2, colour =colour, opacity=opacity,strokewidth=strokewidth)

theta = pi/2 + pi/4
phi = pi/6
gso = Isometric(500,500, 5, 5,5, 'iso.svg', view=[theta,phi])

gso.bg(colour="white")
gso.grid3(num_lines=[5,5,5])
o1 = [0, 0, 0]
x1 = [3, 0, 0]
y1 = [0, 3, 0]
z1 = [0, 0, 3]
gso.draw_line(o1,x1, colour="red")
gso.draw_line(o1,y1, colour="blue")
gso.draw_line(o1,z1, colour="black")

gso.save()
