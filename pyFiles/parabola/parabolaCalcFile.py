from .. import plt, np, random
from ..Settings import settings
from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

from ..keys import parabola_listOfKeys

#gc.collect()

import weakref

class parabolaCalc(dataExplore):
    def __init__(self):
        super().__init__()

        self._vertex = point( random.uniform(settings.xmin, settings.xmax), random.uniform(settings.ymin, settings.ymax), draw = False  )

        self._a = random.uniform(settings.xmin/5, settings.xmax/5)**-1#to be checked out!
        self.addParams('a', self._a)
        self._b = random.uniform(settings.xmin, settings.xmax)#None 
        self.addParams('b', self._b)
        self._c = random.uniform(settings.xmin, settings.xmax)#None
        self.addParams('c', self._c)

        self.j = 0
        self._color = random.choice(self.colors)



    #A-----------------------------------------
    #calculate y = ax^2 + bx + c from a, b and c parameters (to be modified!)
    def calc_a_b_c(self, name = None):

        self.data = [ self._x ]
        self.data = self.data + [self._a*self._x**2 + self._b*self._x + self._c ]
        
        #------------ vertex coords
        xv = -self._b/(2*self._a)
        yv = (- self._b**2 + 4*self._a*self._c)/(4*self._a)

        self._vertex.coords[0] = xv
        self._vertex.coords[1] = yv 
        
        self._vertex.data[0] = np.array([xv])
        self._vertex.data[1] = np.array([yv])
        #------------ vertex coords


    #calculate y = ax^2 + bx + c from a, b parameters and one point
    def calc_a_b_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._c = y0 - self._a*x0**2 - self._b*x0

        self.calc_a_b_c()


    #calculate y = ax^2 + bx + c from a and c parameters and one point
    def calc_a_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._b = (y0 - self._a*x0**2 - self._c)/x0

        self.calc_a_b_c()


    #calculate y = ax^2 + bx + c from a parameters and two points
    def calc_a_po_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]

        A = np.matrix( [ [ x0, 1 ], [ x1, 1  ] ] )
        Ainv = np.linalg.inv(A)
        y = np.array( [y0 - self._a*x0**2, y1 - self._a*x1**2 ] )
        parabParams = np.dot(Ainv, y)

        self._b = parabParams[0, 0]
        self._c = parabParams[0, 1]

        self.calc_a_b_c()


    #calculate y = ax^2 + bx + c from parameter a, and vertex coordinates (vx, vy)
    def calc_a_vx_vy(self, name = None):
        self.data = [ self._x ]
        self.data = self.data + [self._a*(self._x - self.params['vx'])**2 + self.params['vy'] ]
        
        
    #B----------------------------------------------------------------
    #calculate y = ax^2 + bx + c from b and c parameters and one point
    def calc_b_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._a = (y0 - self._b*x0 - self._c)/x0**2

        self.calc_a_b_c()                


    #calculate y = ax^2 + bx + c from b parameter and two points
    def calc_b_po_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]

        A = np.matrix( [ [ x0**2, 1 ], [ x1**2, 1  ] ] )
        Ainv = np.linalg.inv(A)
        y = np.array( [y0 - self._b*x0, y1 - self._b*x1 ] )
        parabParams = np.dot(Ainv, y)

        self._a = parabParams[0, 0]
        self._c = parabParams[0, 1]

        self.calc_a_b_c()


    #calculate y = ax^2 + bx + c from paramter b and vertex coordinate vx and vy
    def calc_b_vx_vy(self, name = None):
        
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = - self._b/(2*self._a)
        self._c = yv + self._b**2/(4*self._a)

        self.calc_a_b_c()

    #C----------------------------------------------------------------
    #calculate y = ax^2 + bx + c from parameter c and two points
    def calc_c_po_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]

        A = np.matrix( [ [ x0**2, x0 ], [ x1**2, x1  ] ] )
        Ainv = np.linalg.inv(A)
        y = np.array( [y0 - self._c, y1 - self._c ] )
        parabParams = np.dot(Ainv, y)

        self._a = parabParams[0, 0]
        self._b = parabParams[0, 1]

        self.calc_a_b_c()


    #calculate y = ax^2 + bx + c from parameter c and vertex coordinatex vx and vy
    def calc_c_vx_vy(self, name = None):
        print("c_ve is running!")
        xv, yv = self._vertex.coords[0], self._vertex.coords[1]

        self._a = (self._c - yv)/xv**2
        self._b = -2*xv*self._a

        self.calc_a_b_c()
        
                
    #P----------------------------------------------------------------
    #calculate y = ax^2 + bx + c from three points
    def calc_po_po_po(self, name = None):

        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        point2 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        
        A = np.matrix([ [ x0**2, x0, 1  ], [ x1**2, x1, 1  ], [ x2**2, x2, 1  ] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ y0  , y1  , y2 ] )#.reshape(-1, 1)
        parabParams = np.dot(Ainv, y)
        
        self._a = parabParams[0, 0]
        self._b = parabParams[0, 1]
        self._c = parabParams[0, 2]
        
        self.calc_a_b_c() 


    #calculate y = ax^2 + bx + c from one point and vertex coordinates
    def calc_po_vx_vy(self, name = None):
        print("po_ve is working!")
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        xv, yv = self._vertex.coords[0], self._vertex.coords[1]

        A = np.matrix([ [ -xv**2, 1  ], [ x0*(x0 - 2*xv), 1]  ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ yv, y0 ])
        parabParams = np.dot(Ainv, y)

        self._a = parabParams[0, 0]
        self._c = parabParams[0, 1]
        self._b = -2*self.a*xv
        self.calc_a_b_c()
