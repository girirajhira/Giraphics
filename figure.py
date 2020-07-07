from graph import Graph
import math


class Figure(Graph):
    def __init__(self, width, height, xlim, ylim, name, origin=[0.0, 0.0], full_svg=True, theme="dark",
                 border_width=0.12, bg="white"):
        Graph.__init__(self, width, height, xlim, ylim, name, full_svg=full_svg, theme=theme)
        self.bw = 1 - border_width
        self.inner_graph = Graph(self.bw * width, self.bw * height, xlim, ylim, name, origin=origin, full_svg=full_svg,
                                 theme=theme, transform="translate("+str(width*border_width/2) + " " + str(height*border_width/2) + ")", grouped=True)
        # self.bg(colour=bg)

    def graph(self, func, colour="red", strokewidth=1.5, opac=1, n0=1200):
        self.inner_graph.graph(func, colour="red", strokewidth=1.5, opac=1, n0=1200)
        # Draw margins

    def graph_points(self, X, Y, colour="red", strokewidth=1, opac=1):
        self.inner_graph.graph_points(X, Y,colour=colour, strokewidth=strokewidth, opac=opac)

    def scatter(self, X, Y, s=1, colour="white", opac=1):
        self.inner_graph.scatter(X,Y,s=s, colour=colour, opac=opac)

    def include_model(self, S):
        self.inner_graph.include_model(S)

    def bg(self, colour="white"):
        self.bg("white")

    def axes(self, colour="yellow", strokewidth=1, arrows=False):
        self.inner_graph.axes(colour=colour, strokewidth=strokewidth, arrows=arrows)

    def grid(self, grids=[20, 20], colour="grey", strokewidth=0.7, opac=0.2):
        self.inner_graph.grid(grids=grids, colour=colour, strokewidth=strokewidth, opac=opac)

    def grid2(self, grids=[20,20], colour="white", strokewidth=0.7, opac=0.2):
        self.inner_graph.grid(grids=grids, colour=colour, strokewidth=strokewidth, opac=opac)

    def bg(self, colour):
        self.inner_graph.bg(colour=colour)

    def ticks(self, stroke="grey", strokewidth=1, tick=10, markers=False, fontsize=8):
        self.inner_graph.ticks(stroke=stroke, strokewidth=strokewidth, tick=tick, markers=markers, fontsize=fontsize)

    # Todo: Constructions #

    # Features

    def xlabel(self, label="x axis", fontsize=13):
        x = -(1-self.bw)*self.xlim
        y = -self.ylim*self.bw - (1-self.bw)*self.ylim/2
        self.text(x, y, text=label, colour="black", fontsize=fontsize)

    def ylabel(self, label="y axis", fontsize=13):
        y = -(1-self.bw)*self.ylim
        x = -self.xlim*self.bw + 2*self.xlim*fontsize/self.width
        self.text(x, y, text=label, colour="black", fontsize=13, rotation=30)

    def title(self, title_label, fontsize = 16):
        x = -(1-self.bw)*self.xlim
        y = self.ylim*self.bw + (1-self.bw)*self.ylim/3
        self.text(x, y, title_label, colour="black", fontsize=fontsize)

    def save(self):
        self.svg.canvas += self.inner_graph.svg.canvas + "\n </svg>\n </g>\n"
        self.draw_rect(0, 0, 2 * self.xlim * self.bw, 2 * self.ylim * self.bw, fill="none", stroke="black",
                       strokewidth=1.2)
        Graph.save(self)

def func(x):
    return 0.04 * x ** 2 * math.sin(6 * x) - 5

f = Figure(1200, 900, 15, 10, "fig.svg", origin=[-2,1])
# f.graph(func, colour="red")
f.grid()
f.grid2(colour="blue")
f.ticks(markers=True)
f.axes(colour="red")
f.xlabel()
f.ylabel()
f.title("are u ok?")
f.save()
f.display()
