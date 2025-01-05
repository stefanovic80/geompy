from .. import plt, np, random
from ..pointFile import point

from ..Settings import settings
from .._plotSettFile import plotSett
from ..dataExploreFile import dataExplore
from ..pointFile import point


class circumferenceCalc(dataExplore):
    def __init__(self):
        super().__init__()

        self._centre = point(draw = False)
        self._a = -2*self._centre.coords[0]
        self._radius = random.uniform(0, (settings.ymax-settings.ymin)/2)
        
        self.addParams('a', self._a)
        self.addParams('radius', self._radius)
        self.addParams('centre', self._centre)
        
        self.angles = None
        self._angle = 2*np.pi
        self._color = random.choice(self.colors)

        self._centre._color = self._color
        self.j = 0
        self.k = 0
        
        self.p = 0


        self.dof = 3


    def po_po(self):
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]
        rmin = point0.dist(point1)
        r = random.uniform(rmin, 4*rmin)
        return x0, y0, x1, y1, r


    def calc_a_b_c(self, name = None, angle = 2*np.pi):
        print("a_b_c is working!")
        self._centre.coords[0], self._centre.coords[1] = self._centre.data[0], self._centre.data[1] = \
                -self._a/2, -self._b/2
        self._radius = np.sqrt( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )
        self.calc_ce_ra()


    def calc_a_b_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = (x0**2 +y0**2 - self._c)**.5
        self.calc_ce_ra()

    def calc_a_b_po(self, name = None, angle = 2*np.pi):
        xc, yc = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._c = -x0**2 - y0**2 - self._a*x0 - self._b*y0
        self._radius = ( ( x0 - xc )**2 + ( y0 - yc )**2 )**.5
        self.calc_ce_ra()

    def calc_a_b_ra(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = ( ( self._a**2 + self._b**2)/4 - self._c )**.5
        self.calc_ce_ra()


    def calc_a_c_ce(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'a' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_ra()
        elif 'c' == firstKey:
            self.noMethod()


    def calc_a_c_po(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._b = (-x0**2 - y0**2 - self._a*x0 - self._c)/y0
        self.calc_a_b_c()

    def calc_a_c_ra(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._b = -2*y0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_ce_ra()

    def calc_a_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'a' == firstKey:
            self.calc_ce_po()
        elif 'ce' == firstKey:
            self._b = random.uniform(settings.ymin/2, settings.ymax/2)
            u = getPoint()
            point = next(u)
            x, y = point.coords[0], point.coords[1]
            self._c = -x**2-y**2-self._a*x-self._b*y
            self.calc_a_b_c()
        else:
            self.noMethod()


    def calc_a_ce_ra(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'a' in firstKey:
            self._b = -2*self._centre.coords[1]
            self._c = self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._radius**2

            self.calc_ce_ra()
        elif 'ce' in firstKey:
            self.noMethod()
        else:
            self.noMethod()
 
    def calc_a_po_po(self, name = None, angle = 2*np.pi):
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]
        self._b = ( ( x1**2 - x0**2  ) - self._a*( x1 - x0  )  )/( y1 - y0  )
        self._c = -(x0**2 + y0**2 + self._a*x0 + self._b*y0 )
        xc, yc = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._radius = ((xc - x0)**2 + (yc - y0)**2)**.5#( xc**2 + yc**2 - self._c )**.5
        self.calc_ce_ra()

    def calc_a_po_ra(self, name = None, angle = 2*np.pi):
        self.noMethod()

    def calc_b_c_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*x0 
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._r = ( x0**2 + y0**2 - self._c )**.5
        self._calci_ce_ra()


    def calc_b_c_ce(self, name = None, angle = 2*np.pi):
        self.noMethod()

    def calc_b_c_po(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*x0
        self._radius = ( ( x0 - x1 )**2 + ( y0 - y1 )**2 )**.5
        self.calc_ce_ra()

    def calc_b_c_ra(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = ( self._radius**2 - self._b**2/4 - self._c )**.5, -self._b/2
        self._a = -2*x0
        self.calc_ce_ra()

    def calc_b_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'b' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_po()
        else:
            self.noMethod()



    def calc_b_ce_ra(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'b' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_ra()
        else:
            self.noMethod()


    def calc_b_po_po(self, name = None, angle = 2*np.pi):
        point1 = getPoint()
        point2 = getPoint()
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = ( y2 - y1 )*(x2 + x1)/(2*self._b), (x2 - x1)*(y2 + y1 )/(2*self._b)
        self._a = -2*x0
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._radius = ( (x1 - x0)**2 + (y1 - y0))**.5
        self.calc_c_ce()

    def calc_b_po_ra(self, name = None, angle = 2*np.pi):
        self.noMethod()

    def calc_c_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'c' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_po()
        else:
            self.noMethod()




    def calc_c_ce_ra(self):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'c' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_ra()
        else:
            self.noMethod()


    #circumference equation calculation from centre coordinates and radius
    def calc_c_ce_ra(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)

        if firstKey == 'c':
            self.noMethod()

        elif firstKey == 'ce':
            self.noMethod()
            
            """
            if len( self.params ) > 2:
                self.keys.popleft()
                del self.params[firstKey]
            """
        else:
            self.noMethod()

    def calc_c_po_po(self, name = None, angle = 2*np.pi):
        point1 = getPoint()
        point2 = getPoint()
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = (y2- y1)*(x1+x2)/(2*(x2 - x1)), (x2-x1)*(y1+y2)/(2*(y2 - y1))
        self._a, self._b = -2*x0, -2*y0
        self._c = -(x0**2 + y**2) - self._a*x0 - self._b*x0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_c_ce()

    def calc_c_po_ra(self, name = None, angle = 2*np.pi):
        self.noMethod()

    def calc_ce_po_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'po' in firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_po()
        elif 'ce' in firstKey:
            print("ce_po_po is working with 'ce' as first")
            x0, y0, x1, y1, self._radius = self.po_po()
            self.calc_po_po_ra()

















    def calc_ce_po_ra(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'ra' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_ce_po()
        else:
            self.noMethod()


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
        self.calc_ce_ra()
    


    """
    def gen(self, ls):
        for el in ls:
            yield el
    """
    def calc_po_po_ra(self, name = None, angle = 2*np.pi):
        x0, y0, x1, y1, r = self.po_po()

        gamma = -(x0 - x1)/(y0 - y1)
        delta = -(x0**2-x1**2+y0**2-y1**2)/(y0-y1)
        ar = 1 + gamma**2
        br = x0 + x1 + gamma*(y0 + y1 + delta)
        cr = 2*x0**2 + 2*x1**2 + 2*y0**2 + 2*y1**2 + 2*delta*(y0 + y1) - 4*self._radius**2 + delta**2
        
        #to be fixed
        DeltaR =  br**2 - ar*cr#Reduced Delta in second square equation
        solutions = [ (-br+DeltaR**.5)/ar, (-br-DeltaR**.5)/ar ] #two solutions of squared equation
        # to iterate
        #a = self.gen(ls = solutions)
        #self._a = next(a)
        j = self.p%2
        self._a = solutions[j]
        self.p += 1

        self._b = -(x0-x1)*(x0+x1+self._a)/(y0 -y1) - (y0 + y1)
        xc, yc = self._centre.coords[0], self._centre.coords[1] = \
                self._centre.data[0], self._centre.data[1] = -self._a/2, -self._b/2
        self._c = -self._radius**2 + xc**2 + yc**2
        print("press one more time 'obj.radius = value' to get the other possible solution\n")
        self.calc_a_b_c()

    #subMethods------------------------------------------------------------
    def calc_c_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._a, self._b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c )**.5
        self.calc_ce_ra()

    def calc_c_po(self, name = None, angle = 2*np.pi):
        point = getPoint()
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = point.coords[0], point.coords[1]
        a, b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_ce_ra()



    def calc_ce_ra(self, name = None, angle = 2*np.pi):

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
        
        #to be deprecated
        self._a = -2*self._centre.coords[0]
        self._b = -2*self._centre.coords[1]
        self._c = self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._radius**2


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
        
        self.calc_ce_ra()
