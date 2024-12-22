from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore

# to be removed
from itertools import combinations


class parabolaCalc(dataExplore):
    def __init__(self):
        super().__init__()

        self._vertex = point( random.uniform(settings.xmin, settings.xmax), random.uniform(settings.ymin, settings.ymax), draw = False  )

        #TO BE FIXED!
        from .keys import parabola_listOfKeys

        self._a = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        self.addParams('a', self._a)
        self._b = random.uniform(settings.xmin, settings.xmax)#None 
        self.addParams('b', self._b)
        self._c = random.uniform(settings.xmin, settings.xmax)#None
        self.addParams('c', self._c)

        self.j = 0
        self._color = random.choice(self.colors)



    #A-----------------------------------------
    #a, b and c (to be modified!)
    def calc00(self, name = None):

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

    #abp, point0, a (self._a) and b (self._b)
    def calc01(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._c = y0 - self._a*x0**2 - self._b*x0

        self.calc00()

    #abv
    def calc02(self, Name = None):
        self.params['c'] = self.params.pop('vertex')
        self.params['c'] = self._c = np.random.uniform(settings.ymin, settings.ymax)
        self.calc00()


    #acp
    def calc03(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._b = (y0 - self._a*x0**2 - self._c)/x0

        self.calc00()
        
    #acv, point0, a (self._a) and c (self._c)
    def calc04(self, name = None):
        self.params['b'] = self.params.pop('vertex')
        self.params['b'] = self._b = np.random.uniform(settings.ymin, settings.ymax)
        self.calc00()

    #app, point0, point1 and a (self._a)
    def calc05(self, name = None):
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

        self.calc00()

    #apv
    def calc06(self, name = None):
        self.params['b'] = self.params.pop('vertex')
        self.params['b'] = self._b = np.random.uniform(settings.ymin, settings.ymax)
        self.calc01()


    #av, vertex, concavity a (self._a)
    def calc07(self, name = None):
        self.data = [ self._x ]
        #self.data = self.data + [self._a*(self._x - self._vertex.coords[0])**2 + self._vertex.coords[1] ]
        self.data = self.data + [self._a*(self._x - self.params['vertex'].coords[0])**2 + self.params['vertex'].coords[1] ]
        
        
    #B----------------------------------------------------------------
    #bcp, point0, b (self._b) and c (self._c)
    def calc08(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._a = (y0 - self._b*x0 - self._c)/x0**2

        self.calc00()                

    #bcv
    def calc09(self, name = None):
        self.calc11()
        #to be better implemented

    #bpp, point0, point1 and b (self._b)
    def calc10(self, name = None):
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

        self.calc00()

    #bv, vertex, b (self._b)
    def calc11(self, name = None):
        
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = - self._b/(2*self._a)
        self._c = yv + self._b**2/(4*self._a)

        self.calc00()

    #C----------------------------------------------------------------
    #cpp, point0, point1 and c (self._c)
    def calc12(self, name = None):
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

        self.calc00()



    #cv, vertex, c (self._c)
    def calc13(self, name = None):
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = (self._c - yv)/xv
        self._b = -2*xv*(self._c - yv)

        self.calc00()
        
                
    #P----------------------------------------------------------------
    #ppp calculate from three points passing through (to be fixed!)
    def calc14(self, name = None):

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
        
        self.calc00() 
    
    #one point and vertex
    #pv
    def calc15(self, name = None):
        #self.dof = 2
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

        self.calc00()
