from . import plt, np, random
from .Settings import settings

class lineCalc():

    def calc_m_q(self): #calculate equation from angCoeff and intercept
        self.data = [self._x]
        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        self.angle = np.arctan(self.angCoeff)


    def calc_p_p(self): #calculate equation from two points

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

            self.calc1()
        else:
            L = len(self._y)
            self.data = [np.zeros(L) + x1]
            self.data = self.data + [ self._y ]

    def calc_m_p(self): #calculate equation from 1 point and angCoeff
        j = 0
        point = next(self.getPoint() )
        x0, y0 = point.coords[0], point.coords[1]
        self.intercept = -self.angCoeff*x0 + y0

        self.calc_m_q()


    def calc_m_p(self): #calculate equation from 1 point and angCoeff
        j = 0
        point = next(self.getPoint() )
        x0, y0 = point.coords[0], point.coords[1]
        self.intercept = -self.angCoeff*x0 + y0

        self.calc_m_q()


    def calc_q_p(self): #calculate equation from 1 point and intercept
        j = 0
        point = next(self.getPoint() )
        x0, y0 = point.coords[0], point.coords[1]
        self.angCoeff = (y0 - self.intercept)/x0
        self.calc_m_q()

