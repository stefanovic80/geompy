# lineFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings

#plt.ion()

from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

from ..keys import segment_listOfKeys

from collections import deque

class segmentCalc(dataExplore):
    #it fails to meet parabola structure
    def __init__(self, point0 = None, point1 = None, seed = seed, draw = True):

        super().__init__()
        
        dof = 2
        self.keys = deque(maxlen = dof)
        self.values = deque(maxlen = dof)

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
    
    #to be decorated
    #--------------------------
    def calc_length(self):
        x0, y0 = self._point[0].coords[0], self._point[0].coords[1]
        x1, y1 = self._point[1].coords[0], self._point[1].coords[1]
        
        self._length = np.sqrt( ( x0 - x1 )**2 + ( y0 - y1 )**2 )
    
    def calc_angle(self):
        x0, y0 = self._point[0].coords[0], self._point[0].coords[1]
        x1, y1 = self._point[1].coords[0], self._point[1].coords[1]

        self._angle = np.arctan( ( y0 - y1) / ( x0 - x1) ) if x0 != x1 else float('inf')

    def calc_po(self):
        pass
    #---------------------------

    #twp points
    def calc_po_po(self):
        u = self.getPoint()
        self._point[0] = next(u)
        self._point[1] = next(u)
        self.data[0] =  np.array([self._point[0].coords[0], self._point[1].coords[0] ])
        self.data[1] = np.array([self._point[0].coords[1], self._point[1].coords[1] ])

        idxs = np.argsort( self.data[0] )
        self._point = [self._point[i] for i in idxs]

        #self._length = np.sqrt( ( self._point[0].coords[0] - self._point[1].coords[0]  )**2 + ( self._point[0].coords[1] - self._point[1].coords[1] )**2  )

        self.data[0] = self.data[0][idxs]
        self.data[1] = self.data[1][idxs]
        
        #to be fixed, because called multiple times!
        self.calc_length()
        self.calc_angle()

    #angle, length and one point
    def calc_an_le(self):
        x, y = self._point[0].coords[0] + self._length*np.cos(self._angle), self._point[0].coords[1] + self._length*np.sin(self._angle)
        self._point[1] = point(x, y)
        #self.calc_po_po()

        #point with lower x value may have to be set as first one: to be checked out
        self.data[0] =  np.array([self._point[0].coords[0], self._point[1].coords[0] ])
        self.data[1] = np.array([self._point[0].coords[1], self._point[1].coords[1] ])


    def calc_an_po(self):
        x0, y0 = self._point[0].coords[0], self._point[0].coords[1]
        #self._length = np.sqrt( ( x0 - self._point[1].coords[0] )**2 + ( y0 - self._point[1].coords[1] )**2 )

        self._point[1].x = x0 + self._length*np.cos(self._angle)
        self._point[1].y = y0 + self._length*np.sin(self._angle)

        self.data[0] = np.array([self._point[0].coords[0], self._point[1].coords[0] ])
        self.data[1] = np.array([self._point[0].coords[1], self._point[1].coords[1] ])

        self.calc_length()
    
    def calc_le_po(self):
        x0, y0 = self._point[0].coords[0], self._point[0].coords[1]
        x1, y1 = self._point[1].coords[0], self._point[1].coords[1]
        previousLength = np.sqrt( ( x0 - x1 )**2 + ( y0 - y1 )**2 )

        cosine = (x1 - x0)/previousLength
        sine = (y1 - y0)/previousLength
        self._point[1].x = self._point[0].coords[0] + cosine*self._length
        self._point[1].y = self._point[0].coords[1] + sine*self._length

        self.data[0] = np.array([self._point[0].coords[0], self._point[1].coords[0] ])
        self.data[1] = np.array([self._point[0].coords[1], self._point[1].coords[1] ])
        
        self.calc_angle()

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

