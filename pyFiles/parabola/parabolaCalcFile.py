from .. import plt, np, random
from ..Settings import settings
from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

#from itertools import combinations
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
    #a, b and c (to be modified!)
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

    #abpo, point0, a (self._a) and b (self._b)
    def calc_a_b_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._c = y0 - self._a*x0**2 - self._b*x0

        self.calc_a_b_c()


    #acpo
    def calc_a_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._b = (y0 - self._a*x0**2 - self._c)/x0

        self.calc_a_b_c()


    #apopo, point0, point1 and a (self._a)
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

    #ave, vertex, concavity a (self._a)
    def calc_a_vx_vy(self, name = None):
        self.data = [ self._x ]
        #self.data = self.data + [self._a*(self._x - self._vertex.coords[0])**2 + self._vertex.coords[1] ]
        self.data = self.data + [self._a*(self._x - self.params['vx'])**2 + self.params['vy'] ]
        
        
    #B----------------------------------------------------------------
    #bcpo, point0, b (self._b) and c (self._c)
    def calc_b_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._a = (y0 - self._b*x0 - self._c)/x0**2

        self.calc_a_b_c()                


    #bpopo, point0, point1 and b (self._b)
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

    #bve, vertex, b (self._b)
    def calc_b_vx_vy(self, name = None):
        
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = - self._b/(2*self._a)
        self._c = yv + self._b**2/(4*self._a)

        self.calc_a_b_c()

    #C----------------------------------------------------------------
    #cpopo, point0, point1 and c (self._c)
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



    #cve, vertex, c (self._c)
    def calc_c_vx_vy(self, name = None):
        print("c_ve is running!")
        xv, yv = self._vertex.coords[0], self._vertex.coords[1]

        self._a = (self._c - yv)/xv**2
        self._b = -2*xv*self._a

        self.calc_a_b_c()
        
                
    #P----------------------------------------------------------------
    #popopo calculate from three points passing through (to be fixed!)
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


    #one point and vertex
    #pove
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
        self._b = -2*self._a*xv

        self.calc_a_b_c()
