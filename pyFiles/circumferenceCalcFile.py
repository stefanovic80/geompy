from . import plt, np, random
from .pointFile import point

from .Settings import settings
from ._plotSettFile import plotSett
from .dataExploreFile import dataExplore



class circumferenceCalc(dataExplore):
    def __init__(self):
        super().__init__()

        self._radius = random.uniform(0, (settings.ymax-settings.ymin)/2)
        self.addParams('radius', self._radius)
        self._centre = point(draw = False)
        self.addParams('Centre', self._centre)

        self.angles = None
        self._angle = 2*np.pi
        self._color = random.choice(self.colors)

        self._centre._color = self._color
        self.j = 0
        self.k = 0

        self.dof = 3

        self._a = None
        self._b = None
        self._c = None
        
        self.calc_a_b_c(self, name = None, angle = 2*np.pi)
        if draw: self.drawSetts()


    def calc_a_b_c(self, name = None, angle = 2*np.pi):
        self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._radius = np.sqrt( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )
        self.calc_C_r()

    def calc_a_b_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = (x0**2 +y0**2 - self_c)**.5
        self.calc_C_r()

    def calc_a_b_po(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        point = getPoint()
        self._radius = ( ( x0 - x1 )**2 + ( y0 - y1 )**2 )**.5
        self.calc_ce_r()

    def calc_a_b_r(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = ( ( self._a**2 + self._b**2)/4 - self._c )**.5
        self.calc_ce_r()

    def calc_a_c_r(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._b = -2*y0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_ce_r()

    def calc_b_c_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*x0 
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._r = ( x0**2 + y0**2 - self._c )**.5
        self._calci_ce_r()

    def calc_b_c_po(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*x0
        self._radius = ( ( x0 - x1 )**2 + ( y0 - y1 )**2 )**.5
        self.calc_ce_r()

    def calc_b_c_r(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = ( self._radius**2 - self._b**2/4 - self._c )**.5, -self._b/2
        self._a = -2*x0
        self.calc_C_r()

    def calc_c_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._a, self._b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c )**.5
        self.calc_ce_r()

    def calc_c_po(self, name = None, angle = 2*np.pi):
        point = getPoint()
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = point.coords[0], point.coords[1]
        a, b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_ce_r()

    #circumference equation calculation from centre coordinates and radius
    def calc_ce_r(self, name = None, angle = 2*np.pi):

        data = [None, None]

        #1) (pi/2 pi/4)
        data[0] = self._x[ (self._x >= 0 ) & (self._x <= self._radius/2**.5)]
        data[1] = list( np.sqrt( ( self._radius  )**2 - ( data[0]  )**2  ) )

        data[0] = list(data[0])
        idx = len(data[0])

        #2) extended from (pi/2 pi/4) to (pi/2 0)
        data[0] = data[1] + data[0][::-1]
        data[1] = data[0][idx:][::-1] + data[1][::-1]

        angles = [ np.arctan(y/x) for (y, x) in zip(data[1], data[0]) ]

        #3) extended from (pi/2 0) to (pi 0)
        data[0] = data[0] + [ -x for x in data[0][::-1] ]
        data[1] = data[1] + data[1][::-1]

        angles = angles + [ np.pi/2 + ang for ang in angles]

        #4) extended from (pi 0) to (2pi 0)
        data[0] = data[0] + data[0][::-1]
        data[1] = data[1] + [ -x for x in data[1][::-1] ]

        angles = angles + [ np.pi + ang for ang in angles]

        #5) connect at the end of the circle
        #data[0] = data[0] + data[0][0]
        #data[1] = data[1] + data[1][1]

        self.angles = np.array(angles)

        self.data = [np.array(data[0]) + self._centre.coords[0], np.array(data[1]) + self._centre.coords[1] ]

        self.pointsSelect(angle = angle)

        self._a = -2*self._centre.coords[0]
        self._b = -2*self._centre.coords[1]
        self._c = self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._radius**2


    # calculate from three points the circumference passing through (to be fixed!)
    def calc_po_po_po(self, name = None, angle = 2*np.pi):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        point1 = next(u)
        x1, y1 = point1.coords[0], point1.coords[1]
        point2 = next(u)
        x2, y2 = point2.coords[0], point2.coords[1]

        A = np.matrix([ [ x0, y0, 1  ], [ x1, y1, 1  ], [ x2, y2, 1  ] ])
        Ainv = np.linalg.inv(A)
        squares = np.array( [ -x0**2 - y0**2  , -x1**2 - y1**2  , -x2**2 - y2**2 ] )
        #circParams = np.dot(Ainv, squares)
        circParams = np.dot(Ainv, squares)

        self._a, self._b, self._c = circParams[0, 0], circParams[0, 1], circParams[0, 2]

        self._centre = point(-circParams[0, 0]/2, -circParams[0, 1]/2, draw = False)

        self._radius = np.sqrt( (circParams[0, 0]/2)**2 + (circParams[0, 1]/2)**2 - circParams[0, 2]  )
        self.calc_C_r()


    def calc_a_po_po(self, name = None, angle = 2*np.pi):
        point1 = self.getPoint()
        point2 = self.getPoint()
        x1, y1 = point0.coords[0], point0.coords[1]
        x2, y2 = point1.coords[0], point1.coords[1]
        self._b = ( ( x2**2 - x1**2  ) - self._a*( x2 - x1  )  )/( y2 - y1  )
        self._c = -(x1**2 + y1**2 + self._a*x1 + self._b*y1 )
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._radius = ( x**2 + y**2 - self._c )**.5
        self.calc_C_r()

    def calc_b_po_po(self, name = None, angle = 2*np.pi):
        point1 = getPoint()
        point2 = getPoint()
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = ( y2 - y1 )*(x2 + x1)/(2*self._b), (x2 - x1)*(y2 + y1 )/(2*self._b)
        self._a = -2*x0
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = ( (x1 - x0)**2 + (y1 - y0))**.5
        self.calc_C_c()

    def calc_c_po_po(self, name = None, angle = 2*np.pi):
        point1 = getPoint()
        point2 = getPoint()
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = (y2- y1)*(x1+x2)/(2*(x2 - x1)), (x2-x1)*(y1+y2)/(2*(y2 - y1))
        self._a, self._b = -2*x0, -2*y0
        self._c = -(x0**2 + y**2) - self._a*x0 - self._b*x0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_C_c()


    # calculate from centre coordinates and a point passing through
    def calc_ce_po(self, name = None, angle = 2*np.pi):
        u = self.getPoint()
        point0 = next(self.getPoint())
        point1 = next(self.getPoint())
        x0 = point0.coords[0]
        x1 = point1.coords[0]
        y0 = point0.coords[1]
        y1 = point1.coords[1]
        self._radius = np.sqrt( ( x0 - x1  )**2 + ( y0 - y1  )**2  )

        self._a = -2*x1
        self._b = -2*y1
        self._c = x1**2 + y1**2 - x0**2 - y0**2
        
        #self.calc_a_b_c()
        self.calc_ce_r()
    
    def calc_ce_p_r(self):
        self.calc_ce_p()
        #r to be removed

