from giraphics.graphing.fancygraph import *


class Widget(FancyGraph):
    def __init__(self, xlim, ylim, Scene, scale=[0.25,0.25], pos=[0, 0], origin=[0.0, 0.0], border=True,
                bcol="white", bstroke=2.5):
        #Translations
        absx, absy = Scene.tranx(pos[0]) - Scene.width * scale[0]/2, Scene.trany(pos[1]) - Scene.height * scale[1]/2
        Graph.__init__(self,Scene.width * scale[0], Scene.height * scale[1], xlim, ylim, " ", origin=origin,
                           transform="translate(" + str(absx) + " " + str(absy) + ")", grouped=True)
        #Borders
        Scene.svg.draw_rect(Scene.tranx(pos[0]), Scene.trany(pos[1]), Scene.width * scale[0], Scene.height * scale[1], 'none', stroke=bcol,
                               strokewidth=bstroke)
    def save(self):
        self.svg.save(write_out=False)


class Scene(FancyGraph):
    def commitWidget(self, widget):
        widget.save()
        self.svg.canvas += widget.svg.canvas

# A = Scene(2560, 1440, 16, 9, 'Ascene.svg')
# A.bg(colour="black")
# A.axes()
# A.grid()
# A.plot(math.sin)
# g1 = Widget(10, 10, A, pos=[-0,0], scale=[0.5,.5], origin=[-10,0.1])
# g1.bg(colour="blue")
# g1.axes()
# g1.plot(math.sin)
# A.commitWidget(g1)
# A.save()
# A.display()