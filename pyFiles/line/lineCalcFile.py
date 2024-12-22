from .. import plt, np, random
from ..Settings import settings
from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

#to be checked out
from .. import seed
from collections import deque

class lineCalc(dataExplore):
    def __init__(self):
        super().__init__()

        self.seed = seed
        self._color = random.choice(self.colors)

        #values to calculate straight line data (self.data[1])
        angle = random.uniform(0, np.pi)
        self.angle = angle
        self.angCoeff =  np.tan(angle)
        self.addParams('m', self.angCoeff)

        self.intercept = np.random.uniform(settings.ymin, settings.ymax)
        self.addParams('q', self.intercept)
        #to be removed
        self.keys = deque(maxlen = self.dof)
        self.values = deque(maxlen = self.dof)


        
    def calc_m_q(self): #calculate equation from angCoeff and intercept
        self.data = [self._x]
        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        self.angle = np.arctan(self.angCoeff)


    def calc_po_po(self): #calculate equation from two points

        u = self.getPoint()
        point0 = next( u )
        x0, y0 = point0.coords[0], point0.coords[1]
        point1 = next( u )
        x1, y1 = point1.coords[0], point1.coords[1]

        self.length = ( ( x0 - x1  )**2 + ( y0 -y1  )**2  )**.5

        if x1 != x0:
            self.angCoeff = (y1 - y0)/(x1 - x0)
            self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
            j = 0

            lims = [ point0.coords[j], point1.coords[j] ]
            lims.sort()
            settings.xmin = lims[0]
            settings.xmax = lims[1]

            self.calc_m_q()
        else:
            L = len(self._y)
            self.data = [np.zeros(L) + x1]
            self.data = self.data + [ self._y ]

    def calc_m_po(self): #calculate equation from 1 point and angCoeff
        j = 0
        point = next(self.getPoint() )
        x0, y0 = point.coords[0], point.coords[1]
        self.intercept = -self.angCoeff*x0 + y0

        self.calc_m_q()


    def calc_po_q(self): #calculate equation from 1 point and intercept
        j = 0
        point = next(self.getPoint() )
        x0, y0 = point.coords[0], point.coords[1]
        self.angCoeff = (y0 - self.intercept)/x0
        self.calc_m_q()

