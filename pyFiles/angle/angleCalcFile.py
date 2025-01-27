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
        xc = self._centre.coords[0] = self._centre.data[0] = np.random.uniform(settings.xmin, settings.xmax)
        yc = self._centre.coords[1] = self._centre.data[1] = np.random.uniform(settings.ymin, settings.ymax)
        
        dof = 4
        self.keys = deque(maxlen = dof)
        self.values = deque(maxlen = dof)    
        
        self.endpoints = [None, None]

        self.addParams('cx', self._centre.coords[0] )
        self.addParams('cy', self._centre.coords[1] )
        self.centre.draw
        self._size = np.random.uniform(0, 2*np.pi)
        self.addParams('am', self._size)
        self._point = point()
        self.points = self._point
        

    def calc_am_cx_cy_po(self):
        xc, yc = self._centre.coords[0], self._centre.coords[1]

        m = [None, None]

        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        
        
        m[0] = ( y0 - yc ) / ( x0 - xc)
        rotateAngle = np.arctan(m[0]) + np.pi*np.heaviside(xc - x0, 0) 
        m[1] = np.sign( y0 - yc  )*np.arctan( self._size )

        radius = (settings.xmax - settings.xmin)/20
        self._radius = radius

        self.calc_cx_cy_ra(arc = self._size)
        self._centre.rotation( locus = self, angle = rotateAngle )

    def calc_am_cx_po_po(self):
        self._calc_cx_po_po(arc = np.pi/2 )
        print("Work in progress!")

    def calc_am_cy_po_po(self):
        self.calc_cy_po_po(arc = np.pi/2)
        print("Work in progress!")


    def calc_cx_cy_po_po(self):
        print("cx_cy_po_po .calc method is working!")

        xc, yc = self._centre.coords[0], self._centre.coords[1]

        m = [None, None]

        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        point1 = next(u)
        x1, y1 = point1.coords[0], point1.coords[1]
        
        m[0] = ( y0 - yc ) / ( x0 - xc)
        rotateAngle0 = np.arctan(m[0]) + np.pi*np.heaviside(xc - x0, 0) 
        m[1] = ( y1 - yc ) / ( x1 - xc)
        rotateAngle1 = np.arctan(m[1]) + np.pi*np.heaviside(xc - x1, 0)

        rotateAngle = sorted([rotateAngle0, rotateAngle1])

        radius = (settings.xmax - settings.xmin)/20
        self._radius = radius
        
        self._size = rotateAngle[1] - rotateAngle[0]
        print( str(rotateAngle[0]) + "\n" + str(rotateAngle[1])+ "\n")
        self.calc_cx_cy_ra(arc = self._size)
        self._centre.rotation( locus = self, angle = rotateAngle[0] )



        """
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
        """
    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
