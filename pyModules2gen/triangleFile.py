from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett

from ..pyFiles import seed #steps, linewidth, seed

from ..pyFiles.Settings import settings#xmin, xmax, linewidth, steps

from ..pyFiles import plt, np, random

class triangle(plotSett):
    def __init__(self, seed = seed):#, xmin = xmin, xmax = xmax, steps = steps, seed = seed):
        super().__init__()#xmin, xmax, steps)
        self.A = point( draw = False )
        self.B = point( draw = False )
        self.C = point( draw = False )
        self.AB = None
        self.BC = None
        self.CA = None
        self.data = None
        self.rotate = False
        self._name = None
        self._color = random.choice(self.colors)

    def calc(self):
        self.AB = line( draw = False )
        self.BC = line( draw = False )
        self.CA = line( draw = False )
        self.AB.erase()
        self.BC.erase()
        self.CA.erase()
        self.AB.point[0] = self.A
        self.AB.point[1] = self.B
        self.BC.point[0] = self.B
        self.BC.point[1] = self.C
        self.CA.point[0] = self.C
        self.CA.point[1] = self.A
        
        """
        self.A.color = self.B.color = self.C.color
        self.AB.color = self.BC.color = self.CA.color
        """
        self.AB._cut = self.BC._cut = self.CA._cut = True

        self.AB.calc2()#two points
        self.BC.calc2()#two points
        self.CA.calc2()#two points
        # Concatenate the arrays in the lists
        self.data = [ np.concatenate( [ self.AB.data[0], self.BC.data[0], self.CA.data[0] ] ), np.concatenate( [ self.AB.data[1], self.BC.data[1], self.CA.data[1] ] ) ]

        #self.data = [ np.concatenate( [ self.AB.data[0], self.BC.data[0], self.CA.data[0] ), np.concatenate( [ self.AB.data[1], self.BC.data[1], self.CA.data[1] ) ]

    def draw(self, name = None):
        self.__del__()
        self._name = name
        if self.rotate == False:
            self.calc()

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color)

        self.lines = []
        self.lines.append(line)

        #copied from line class, not completed
        
    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]

        for j in range(2):
            self.point[j].coords = [None, None]
        #for u in self.point:
        #    u.coords = [None, None]

        self.angCoeff = None
        self.intercept = None

