from giraphics.graphing.graph import Graph



G = Graph(400,400,4,4,'arrow_test.svg')

G.bg(colour='white')
G.ticks(markers=True, colour='black', fontsize=5)
G.grid()
G.axes(colour='black')

G.draw_arrowhead(1,1,ang=23)
G.draw_arrow(0,0, 2, 1)
G.draw_arrow2(0,0, 1, 3)

G.save()