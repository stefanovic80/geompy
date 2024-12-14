from . import plt, np, random
from .Settings import settings

class parabolaCalc():
    #def __init__(): 
    #    self.methods = [calc00, calc01, calc02, calc03, calc04, calc05, calc06, calc07,\
    #        calc08, calc09, calc10, calc11, calc12, calc13, calc14, calc15]
    #A----------------------------------------------------------------
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

        self.calc_a_b_c()

    #abv
    def calc02(self, Name = None):
        self.params['c'] = self.params.pop('vertex')
        self.params['c'] = self._c = np.random.uniform(settings.ymin, settings.ymax)
        self.calc_a_b_c()


    #acp
    def calc03(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._b = (y0 - self._a*x0**2 - self._c)/x0

        self.calc_a_b_c()
        
    #acv, point0, a (self._a) and c (self._c)
    def calc04(self, name = None):
        self.params['b'] = self.params.pop('vertex')
        self.params['b'] = self._b = np.random.uniform(settings.ymin, settings.ymax)
        self.calc_a_b_c()

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

        self.calc_a_b_c()

    #apv
    def calc06(self, name = None):
        self.params['b'] = self.params.pop('vertex')
        self.params['b'] = self._b = np.random.uniform(settings.ymin, settings.ymax)
        self.calc_a_b_p()


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

        self.calc_a_b_c()                

    #bcv
    def calc09(self, name = None):
        self.calc_b_v
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

        self.calc_a_b_c()

    #bv, vertex, b (self._b)
    def calc11(self, name = None):
        
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = - self._b/(2*self._a)
        self._c = yv + self._b**2/(4*self._a)

        self.calc_a_b_c()

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

        self.calc_a_b_c()



    #cv, vertex, c (self._c)
    def calc13(self, name = None):
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = (self._c - yv)/xv
        self._b = -2*xv*(self._c - yv)

        self.calc_a_b_c()
        
                
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
        
        self.calc_a_b_c() 
    
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

        self.calc_a_b_c()
