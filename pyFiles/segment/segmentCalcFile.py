# lineFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings

#plt.ion()

from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

from ..keys import segment_listOfKeys


class segmentCalc(dataExplore):
    def __init__(self, point0 = None, point1 = None, seed = seed, draw = True):
        #def __init__(self):

        super().__init__()
         
        _color = random.choice(self.colors)
        
        if point0 is None:
            point0 = point()
            point0.color = _color

        if point1 is None:
            point1 = point()
            point1.color = _color
        
        self.seed = seed
        self._color = random.choice(self.colors)
        self._point = [point0, point1]
        
        self.addParams('point0', self._point[0])
        self.addParams('point1', self._point[1])
        
        x0, y0 = self._point[0].coords[0], self._point[1].coords[0]
        x1, y1 = self._point[1].coords[0], self._point[1].coords[1]

        self._length = np.sqrt( ( x0 - x1  )**2 + ( y0 - y1 )**2  )
        #to prevent x0 = x1 
        
        self.addParams('length', self._length)

        m = ( y0 - y1  ) / ( x0 - x1  )
        #to be checked out
        self._angle = np.arctan( m ) + np.pi*np.heaviside(x0 - x1, 0)

    #twp points
    def calc_po_po(self):
        #sorted( self._point[0].x[0], self._point[1].x[0] )
        u = self.getPoint()
        self._point[0] = next(u)
        self._point[1] = next(u)
        self.data[0] =  np.array([self._point[0].coords[0], self._point[1].coords[0] ])
        self.data[1] = np.array([self._point[0].coords[1], self._point[1].coords[1] ])




        #to be fixed
        idxs = np.argsort( self.data[0] )
        self._point = [self._point[i] for i in idxs]
        self.data[0] = self.data[0][idxs]
        self.data[1] = self.data[1][idxs]

    #angle, length and one point
    def calc_an_le_po(self):
        #print("an_le_po is working")
        #u = self.getPoint()
        #self._point[0] = next(u)

        #to be fixed!
        x, y = self._length*np.cos(self._angle), self._length*np.sin(self._angle)
        self._point[1] = point(x, y)
        self.calc_po_po()

    def calc_an_po_po(self):
        #if 'an' == self.sflk[0]:
        self.calc_po_po()
        #else:
        #    print("work in progress")

    def calc_le_po_po(self):
        #if "le" == self.sflk[0]:
        self.calc_po_po()
        #else:
        #    print("work in progress!")

    def calc_po_po_po(self):
        self.calc_po_po()

    @property
    def dataGroup(self):
        return self.data + self.labCoords

    @dataGroup.setter
    def dataGroup(self, value):
        self.data = value[0:2]
        #self.labCoords = value[2:4]
        #to be implemented!

    

    def erase(self):
        self.__del__()

        self.data = [None, None]


    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m line\n"
            f"\033[93m.m = \033[0m {self.angCoeff}\n"
            f"\033[93m.q = \033[0m {self.intercept}\n"
            f"\033[93m.color = \033[0m {self._color}\n"
            f"\033[93m.linewdith =\033[0m {self._linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

