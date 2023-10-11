from pyFiles.segmentFile import segment
from pyFiles.pointFile import point
from pyFiles._plotSettFile import plotSett

from pyFiles import xmin, xmax, steps, linewidth, seed


class triangle(plotSett):
    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, seed = seed):
        super().__init__(xmin, xmax, steps)
        self.A = point()
        self.B = point()
        self.C = point()
        self.AB = None
        self.BC = None
        self.CA = None

    def calc(self):
        self.AB = segment()
        self.BC = segment()
        self.CA = segment()
        self.AB.erase()
        self.BC.erase()
        self.CA.erase()
        self.AB.point[0] = self.A
        self.AB.point[1] = self.B
        self.BC.point[0] = self.B
        self.BC.point[1] = self.C
        self.CA.point[0] = self.C
        self.CA.point[1] = self.A
        
        self.A.color = self.B.color = self.C.color
        self.AB.color = self.BC.color = self.CA.color
        self.data = None

    def draw(self):
        self.calc()
        self.A.draw("A")
        self.B.draw("B")
        self.C.draw("C")
        self.AB.draw(cut = True)
        self.BC.draw(cut = True)
        self.CA.draw(cut = True)
