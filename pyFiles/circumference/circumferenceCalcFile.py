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
        #to be debbugged
        #rmin = point0.dist(point1)
        rmin = ( (x0 -x1)**2 + (y0 - y1)**2)**.5
        r = random.uniform(rmin, 4*rmin)
        return x0, y0, x1, y1, r


    def calc_a_b_c(self, name = None, angle = 2*np.pi):
        self._centre.coords[0], self._centre.coords[1] = self._centre.data[0], self._centre.data[1] = \
                -self._a/2, -self._b/2
        self._radius = np.sqrt( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )
        self.calc_cx_cy_ra()


    def calc_a_b_ce(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)

        self._radius = np.random.uniform(0, abs(max([ settings.ymin,\
                settings.ymax])))
        
        #self.addParamLeft('r', self._radius)
        
        if 'ce' in firstKey:
            self._centre.coords[0] = self._centre.data[0] = -self._a/2
            self._centre.coords[1] = self._centre.data[1] = -self._b/2
        else:
            xc, yc = self._centre.coords[0], self._centre.coords[1]
            self._a = -2*xc
            self._b = -2*yc
            self._c = -self._radius**2 + xc**2 + yc**2
        
        self.calc_cx_cy_ra()

    def calc_a_b_po(self, name = None, angle = 2*np.pi):
        xc, yc = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._c = -x0**2 - y0**2 - self._a*x0 - self._b*y0
        self._radius = ( ( x0 - xc )**2 + ( y0 - yc )**2 )**.5
        self.calc_cx_cy_ra()

    def calc_a_b_ra(self, name = None, angle = 2*np.pi):
        xc, yc = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._c = -self._radius**2 + xc**2 + yc**2
        self.calc_cx_cy_ra()


    def calc_a_c_ce(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'a' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_cx_cy_ra()
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
        self.calc_cx_cy_ra()

    def calc_a_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'a' == firstKey:
            self.calc_ce_po()
        elif 'ce' == firstKey:
            self._b = random.uniform(settings.ymin/2, settings.ymax/2)
            u = self.getPoint()
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

            self.calc_cx_cy_ra()
        elif 'ce' in firstKey:
            xc = -self._a/2
            yc = np.random.uniform( settings.xmin, settings.xmax)
            self._b = -2*yc
            self._c = -self._radius**2 + xc**2 + yc**2
            self.calc_a_b_c()

        elif 'ra' in firstKey:
            self.noMethod()
 
    def calc_a_po_po(self, name = None, angle = 2*np.pi):
        print("a_po_po is running\n")
        x0, y0, x1, y1, r = self.po_po()
        
        A = np.matrix( [ [y0, 1], [y1, 1] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [-x0**2 - y0**2 - self._a**x0, -x1**2 - y1**2 - self._a*x1 ])
        parabParams = np.dot(Ainv, y)

        self._b = parabParams[0, 0]
        self._c = parabParams[0, 1]
        #self.calc_ce_ra()
        self.calc_a_b_c()

    def calc_a_po_ra(self, name = None, angle = 2*np.pi):
        xc = self._centre.coords[0] = self._centre.data[0] = -self._a/2
        yc = self._centre.coords[1] = self._centre.data[1] = np.random.uniform(settings.ymin, settings.ymax)
        self._b = -2*yc
        self._c = -self._radius**2 + xc**2 + yc**2
        self.calc_cx_cy_ra()

    def calc_b_c_ce(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*x0 
        self._c = -(x0**2 + y0**2) - self._a*x0 - self._b*y0
        self._r = ( x0**2 + y0**2 - self._c )**.5
        self._calci_cx_cy_ra()

    def calc_b_c_po(self, name = None, angle = 2*np.pi):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        xc, yc = self._centre.coords[0], self._centre.coords[1] = -self._a/2, -self._b/2
        self._a = -2*xc
        self._radius = ( ( xc - x0 )**2 + ( yc - y0 )**2 )**.5
        self.calc_cx_cy_ra()

    def calc_b_c_ra(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = ( self._radius**2 - self._b**2/4 - self._c )**.5, -self._b/2
        self._a = -2*x0
        self.calc_cx_cy_ra()

    def calc_b_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'b' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_cx_cy_po()
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
        print("b_po_po is working!")
        x0, y0, x1, y1, r = self.po_po()
        A = np.matrix( [ [ x0, 1 ], [x1, 1] ] )
        Ainv = np.linalg.inv(A)
        y = np.array( [-x0**2 - y0**2 -self._b*y0 - self._c, -x1**2 - y1**2 - self._b*y1 - self._c ] )
        parabParams = np.dot(Ainv, y)
        self._a = parabParams[0, 0]
        self._c = parabParams[0, 1]
        self.calc_a_b_c()

    def calc_b_po_ra(self, name = None, angle = 2*np.pi):
        self.noMethod()

    def calc_c_ce_po(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'c' == firstKey:
            self._radius = ( self._centre.coords[0]**2 + self._centre.coords[1]**2 - self._c  )**.5
            self.calc_cx_cy_po()
        elif 'ce' == firstKey[:2]:
            self.noMethod()




    def calc_c_ce_ra(self):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'c' == firstKey:
            self.calc_ce_ra()
        elif 'ce' in firstKey:
            yc = self._centre.coords[1] = self._centre.data[1] = np.random.uniform(settings.ymin, settings.ymax)
            xc = self._centre.coords[0] = self._centre.data[0] = ( abs( self._radius**2 - yc**2) )**.5
            self.calc_ce_ra()
        elif 'ra' in firstKey:
            xc, yc = self._centre.coords[0], self._centre.coords[1]
            self._a, self._b = -2*xc, -2*yc
            self.calc_a_b_c()


    def calc_c_po_po(self, name = None, angle = 2*np.pi):
        #to be fixed
        x0, y0, x1, y1, r = self.po_po()

        A = np.matrix( [ [ x0, y0 ], [x1, y1] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ - self._c - x0**2 - y0**2, -self._c - x1**2 - y1**2 ] )
        parabParams = np.dot(Ainv, y)
        self._a = parabParams[0, 0]
        self._b = parabParams[0, 1]

        xc, yc = self._centre.coords[0], self._centre.coords[1] = - self._a/2, -self._b/2
        self._radius = ( (xc - x0)**2 + (yc - y0)**2 )**.5
        self.calc_a_b_c()
        #self.calc_c_ce()

    def calc_c_po_ra(self, name = None, angle = 2*np.pi):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if 'c' in firstKey:
            pass
        elif 'ra' == firstKey[:2]:
            pass
        elif 'po' == firstKey[:2]:
            pass


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
        if 'ra' == firstKey[:2]:
            self.calc_ce_po()
        elif 'po' == firstKey[:2]:
            self.calc_ce_ra()
        else:
            self._centre.coords = self.centre.data = [ np.random.uniform(settings.ymin, settings.ymax) for j in range(2)]
        
        self.calc_cx_cy_po()



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
        
        circParams = np.dot(Ainv, squares)

        self._a, self._b, self._c = circParams[0, 0], circParams[0, 1], circParams[0, 2]

        self._centre = point(-circParams[0, 0]/2, -circParams[0, 1]/2, draw = False)

        self._radius = np.sqrt( (circParams[0, 0]/2)**2 + (circParams[0, 1]/2)**2 - circParams[0, 2]  )
        self.calc_cx_cy_ra()


    def calc_po_po_ra(self, name = None, angle = 2*np.pi):
        x0, y0, x1, y1, r = self.po_po()

        gamma = -(x0 - x1)/(y0 - y1)
        delta = -(x0**2-x1**2+y0**2-y1**2)/(y0-y1)
        ar = 1 + gamma**2
        br = x0 + x1 + gamma*(y0 + y1 + delta)
        cr = 2*x0**2 + 2*x1**2 + 2*y0**2 + 2*y1**2 + 2*delta*(y0 + y1) - 4*self._radius**2 + delta**2
        
        DeltaR =  br**2 - ar*cr#Reduced Delta in second square equation
        solutions = [ (-br+DeltaR**.5)/ar, (-br-DeltaR**.5)/ar ] #two solutions of squared equation

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
    def calc_c_cx_cy(self, name = None, angle = 2*np.pi):
        x0, y0 = self._centre.coords[0], self._centre.coords[1]
        self._a, self._b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c )**.5
        self.calc_cx_cy_ra()

    def calc_c_po(self, name = None, angle = 2*np.pi):
        point = self.getPoint()
        x0, y0 = self._centre.coords[0], self._centre.coords[1] = point.coords[0], point.coords[1]
        a, b = -2*x0, -2*y0
        self._radius = ( x0**2 + y0**2 - self._c)**.5
        self.calc_cx_cy_ra()


    def calc_cx_cy_ra(self, name = None, angle = 2*np.pi):

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
    def calc_cx_cy_po(self, name = None, angle = 2*np.pi):
        print("ce_po is working!")
        u = self.getPoint()
        point0 = next(u)
        x0 = point0.coords[0]
        y0 = point0.coords[1]
        
        xc = self._centre.coords[0]
        yc = self._centre.coords[1]
        self._radius = np.sqrt( ( x0 - xc  )**2 + ( y0 - yc  )**2  )

        self._a = -2*xc
        self._b = -2*yc
        self._radius = ( (x0 - xc)**2 + (y0 - yc)**2 )**.5
        self._c = xc**2 + yc**2 - self._radius**2
        
        self.calc_cx_cy_ra()
