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




    #abve
    def calc_a_b_ve(self, Name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if firstKey == 'a':
            self._a = - self._b/(2*self._vertex.coords[0])
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            self.calc_a_b_c()
            
            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        elif firstKey == 'b':
            self._b = -2*self._a*self._vertex.coords[0]
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            
            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        else:
            self._c = np.random.uniform(settings.ymin, settings.ymax)
            self.addParams('c', self._c)
            self.calc_a_b_c()


    #acpo
    def calc_a_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._b = (y0 - self._a*x0**2 - self._c)/x0

        self.calc_a_b_c()
        
    #acve, point0, a (self._a) and c (self._c)
    def calc_a_c_ve(self, name = None):
        print("to be debugged!")
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if firstKey == 'a':
            self._a = - self._b/(2*self._vertex.coords[0])
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            self.calc_a_b_c()

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        elif firstKey == 'b':
            self._b = -2*self._a*self._vertex.coords[0]
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        else:
            self._c = np.random.uniform(settings.ymin, settings.ymax)
            self.addParams('c', self._c)
            self.calc_a_b_c()
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if firstKey == 'a':
            self._a = ( self._c - self._vertex.coords[1] )/( 4*self._vertex.coords[0] )
            self._b = -2*self._a*self._vertex.coords[0]
            self.calc_a_b_c()

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        elif firstKey == 'c':
            self._b = -2*self._a*self._vertex.coords[0]
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            
            self.calc_a_b_c()
            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        else:
            self._b = np.random.uniform(settings.ymin, settings.ymax)
            self.addParams('b', self._b)
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

    #apove
    def calc_a_po_ve(self, name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        #possible bug: u is not necessarely a point
        u = self.getPoint()
        point = next(u)
        x0, y0 = point.coords[0], point.coords[1]
        xv, yv = self._vertex.coords[0], self._vertex.coords[1]
        if firstKey == 'a':
            self._a = ( y0 - yv)/(x0 - yv)**2
            self._b = - 2*self._a*xv
            self._c = y0 - self._a*x0**2 - self._b*x0
            self.calc_a_b_c()

        elif firstKey == 'po':
            self._b = -2*self._a*self._vertex.coords[0]
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            self.calc_a_b_c()

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        else:
            self._b = np.random.uniform(settings.ymin, settings.ymax)
            self.addParams('b', self._b)
            self.calc_a_b_c()

    #ave, vertex, concavity a (self._a)
    def calc_a_ve(self, name = None):
        self.data = [ self._x ]
        #self.data = self.data + [self._a*(self._x - self._vertex.coords[0])**2 + self._vertex.coords[1] ]
        self.data = self.data + [self._a*(self._x - self.params['vertex'].coords[0])**2 + self.params['vertex'].coords[1] ]
        
        
    #B----------------------------------------------------------------
    #bcpo, point0, b (self._b) and c (self._c)
    def calc_b_c_po(self, name = None):
        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        self._a = (y0 - self._b*x0 - self._c)/x0**2

        self.calc_a_b_c()                

    #bcve
    def calc_b_c_ve(self, name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        if firstKey == 'c':
            self._a = - self._b/(2*self._vertex.coords[0])
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)
            self.calc_a_b_c()

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        elif firstKey == 'b':
            self._a = ( self._c - self._vertex.coords[1] )/(self._vertex.coords[0]**2)
            self._b = -2*self._a*self._vertex.coords[0]
            self.calc_a_b_c()

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        else:
            self.noMethod()

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
    def calc_b_ve(self, name = None):
        
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
    def calc_c_ve(self, name = None):
        xv, yv = self.vertex.coords[0], self.vertex.coords[1]

        self._a = (self._c - yv)/xv
        self._b = -2*xv*(self._c - yv)

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
    def calc_po_ve(self, name = None):
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

    def rmParam(self):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)

        if len( self.params ) > 2:
            self.keys.popleft()
            del self.params[firstKey]


    #bpove
    def calc_b_po_ve(self, name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        #pove
        if firstKey == 'b':
            self.calc_po_ve()

        #bve
        elif firstKey == 'po':
            self._a = -self._b/(2*self._vertex.coords[0])
            self._c = self._vertex.coords[1] + self._b**2/(4*self._a)

            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        #bpo
        else:
            self._c = np.random.uniform(settings.ymin, settings.ymax)
            #self.addParams('c', self._c)
            self._a = np.random.uniform(settings.ymin, settings.ymax)
            #self.addParams('a', self._a)
            self.calc_a_b_c()

    #cpove
    def calc_c_po_ve(self, name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        #pove
        if firstKey == 'c':
            self.calc_po_ve()
            #self.rmParam()
        #cve
        elif firstKey == 'po':
            self._a = ( self._c - self._vertex.coords[1])/(self._vertex.coords[0])**2
            self._b = -2*self._a*self._vertex.coords[0]
            self.calc_a_b_c()
            #if len( self.params ) > 2:
            #    self.keys.popleft()
            #    del self.params[firstKey]
        #cpo
        else:
            self._a = np.random.uniform(settings.ymin, settings.ymax)
            #self.addParams('a', self._a)
            self._a = np.random.uniform(settings.ymin, settings.ymax)
            #self.addParams('b', self._b)
            self.calc_a_b_c()




    #popove
    def calc_po_po_ve(self, name = None):
        firstKey = iter( self.params.keys() )
        firstKey = next(firstKey)
        #pove. It's not working yet
        if firstKey[:2] == 'po':
            self.calc_po_ve()
        #popo
        elif firstKey[:2] == 've': 
            self._c = np.random.uniform(settings.ymin, settings.ymax)
            u = self.getPoint()
            point0 = next(u)
            point1 = next(u)
            
            x0, y0 = point0.coords[0], point0.coords[1]
            x1, y1 = point1.coords[0], point1.coords[1]
            
            A = np.matrix([ [ x1**2, x1  ], [ x0**2, x0]  ])
            Ainv = np.linalg.inv(A)
            y = np.array( [ y1 - self._c, y0 - self._c ])
            parabParams = np.dot(Ainv, y)

            self._a = parabParams[0, 0]
            self._b = parabParams[0, 1]
            self.calc_a_b_c()

