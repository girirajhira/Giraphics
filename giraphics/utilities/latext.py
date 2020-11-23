class LaText():
    def __init__(self, name, x, y, text, size=12, rotation=0, transperant=True, dpi=200, colour="black"):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.rot = rotation
        self.name = name
        self.transperant = transperant
        self.dpi = dpi
        self.colour = colour

    def show(self):
        plt.text(self.x, self.y, self.text, size=self.size, rotation=self.rot,
                 ha="left", va="top")
        plt.show()
        plt.close()

    def save(self):
        plt.text(self.x, self.y, self.text, size=self.size,
                 rotation=self.rot, color=self.colour, ha="left", va="top")
        plt.axis('off')
        plt.xlim(0, 2.5)
        plt.ylim(0, 1)
        plt.savefig(self.name, transparent=self.transperant, dpi=self.dpi)
