from ..line.lineFile import line
from ..pointFile import point
#from ..dataExploreFile import dataExplore
from ..circumference.circumferenceFile import circumference
from .. import seed
from ..Settings import settings
from .. import plt, np, random

from collections import deque

class angleCalc(circumference):
    #def __init__(self, line0 = line(draw = False) , line1 = line(draw = False), seed = seed, draw = True):
    def __init__(self, draw = True):

        super().__init__(draw = False)
        
        #test 
        xc = self._centre.coords[0] = self._centre.data[0] = 0
        yc = self._centre.coords[1] = self._centre.data[1] = 0
        
        dof = 4
        self.keys = deque(maxlen = dof)
        self.values = deque(maxlen = dof)    
        
        self.endpoints = [None, None]

        self.addParams('cx', self._centre.coords[0] )
        self.addParams('cy', self._centre.coords[1] )
        
        """
        x, y = np.random.randint(1, 4), np.random.randint(1, 4) 
        

        self.point = point(x, y)
        self.point.name = "P"
        
        x0, y0 = self.point.coords[0], self.point.coords[1]

        k = 0 #to be fixed
        self.addParams( "point" + str(k), self.point )
        
        self._size = np.random.uniform(0, 2*np.pi )
        self.addParams("am", self._size)
        """

    def calc_am_cx_cy_po(self):
        print("work in progress!")

        xc, yc = self._centre.coords[0], self._centre.coords[1]

        m = [None, None]

        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        
        
        m[0] = ( y0 - yc ) / ( x0 - xc)
        rotateAngle = np.arctan(m[0]) + np.pi*np.heaviside(xc - x0, 0) 
        m[1] = np.sign( y0 - yc  )*np.arctan( self._size )
        
        """
        #------------- from chatGPT
        # Get the indices that would sort 'm'
        sorted_indices = np.argsort(m)

        # Sort 'm' and 'q' based on the sorted indices
        m = [m[i] for i in sorted_indices]
        #q = [q[i] for i in sorted_indices]
        #------------- from chatGPT
        """


        radius = (settings.xmax - settings.xmin)/20
        self._radius = radius



        #self._size = abs( self.j%2*np.pi - np.arctan( m[1] ) + np.arctan( m[0] )  )
        self.calc_cx_cy_ra(arc = self.size)
        #to be modified!

        #formula = (self.j + 1)%2*np.arctan(m[0]) + self.j%2*np.arctan(m[1]) +int(self.j/2)*np.pi
        self._centre.rotation( locus = self, angle = rotateAngle )# formula)




    def calc_cx_cy_po_po(self):
        print("cx_cy_po_po .calc method is working!")
        xc, yc = self._centre.coords[0], self._centre.coords[1]
        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]
        self.calc_cx_cy_po()
        #to be fixed
        coeffAng_point0, coeffAng_point1 = ( y0 - yc ) / ( x0 - xc) ,  ( y1 - yc ) / ( x1 - xc) 
        angle = np.arctan( coeffAng_point1 ) - np.arctan( coeffAng_point0  )
        self.arc = angle
        #self.radius = 3 # to be fixed according with plot size


    #may be deprecated
    def calc(self):
        self.__del__()


        m = [None, None]
        q = [None, None]
        
        self.line[0]._color = self._color
        self.line[0].calc2()
        
        self.line[1]._color = self._color
        self.line[1].erase()
        self.line[1]._points[0] = self.line[0]._points[0]
        self.line[1].intercept = np.random.uniform(settings.xmin, settings.xmax)
        self.line[1].calc4()
        
        m[0] = self.line[0].angCoeff
        q[0] = self.line[0].intercept
        
        m[1] = self.line[1].angCoeff
        q[1] = self.line[1].intercept


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        self.angle._center = point( x, y, draw = False  )
        
        radius = (settings.xmax - settings.xmin)/20
        self.angle._radius = radius
        
        self.angle._color = self._color

        arcSize = np.arctan( m[1] ) - np.arctan( m[0] )
        self.angle.calc(arc = arcSize)
        
        self.angle._center.rotation( locus = self.angle, arc = np.arctan( m[0] ) )

        self.data = self.angle.data
        
        self.size = None

    
    
    def calc2(self):
        m = [None, None]
        q = [None, None]

        m[0] = self.line[0].angCoeff#[0]
        q[0] = self.line[0].intercept#[0]

        m[1] = self.line[1].angCoeff#[0]
        q[1] = self.line[1].intercept#[0]
        
        #------------- from chatGPT
        # Get the indices that would sort 'm'
        sorted_indices = np.argsort(m)
        
        # Sort 'm' and 'q' based on the sorted indices
        m = [m[i] for i in sorted_indices]
        q = [q[i] for i in sorted_indices]
        #------------- from chatGPT


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        
        self.angle._center = point( x, y, draw = False )










        radius = (settings.xmax - settings.xmin)/20
        self.angle._radius = radius

        self.angle._color = self._color

        self.size = abs( self.j%2*np.pi - np.arctan( m[1] ) + np.arctan( m[0] )  )
        self.angle.calc(arc = self.size)
        #to be modified!
        
        formula = (self.j + 1)%2*np.arctan(m[0]) + self.j%2*np.arctan(m[1]) +int(self.j/2)*np.pi
        self.angle._center.rotation( locus = self.angle, arc = formula)

        #to be checked out!
        self.data = self.angle.data

        self.j+=1


    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
