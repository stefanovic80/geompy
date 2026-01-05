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

        self._radius = (settings.xmax - settings.xmin)/20

        self.addParams('cx', self._centre.coords[0] )
        self.addParams('cy', self._centre.coords[1] )
        self.centre.draw
        self._size = np.random.uniform(0, 2*np.pi)
        self.addParams('am', self._size)
        self._point = point(draw = False)
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

        self.calc_cx_cy_ra(arc = self._size)
        self.rotate = self._centre, rotateAngle

    def calc_am_cx_po_po(self):
        self.calc_cx_po_po()#arc = np.pi/2 )
        self.calc_cx_cy_po_po()
        print("Work in progress!")

    def calc_am_cy_po_po(self):
        self.calc_cy_po_po(arc = np.pi/2)
        print("Work in progress!")


    def calc_cx_cy_po_po(self):
        """
        Calculates the angle between two points ('po' and 'po') relative to a center (cx, cy),
        and rotates the arc accordingly.
        
        - Computes the slopes (m) between the center and the two points.
        - Uses the arctangent function to determine the angles of the points relative to the center.
        - Correctly handles division by zero cases.
        - Calculates the total angle (arc) between the two points.
        - Rotates the arc based on the calculated angles, similar to how angles are defined and rotated in GeoGebra.

        Note: Angles are calculated relative to the horizontal axis, and the arc is rotated 
        based on the relative position of the points to the center.
        """

        xc, yc = self._centre.coords[0], self._centre.coords[1]

        m = [None, None]

        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        point1 = next(u)
        x1, y1 = point1.coords[0], point1.coords[1]
        
        m[0] = ( y0 - yc ) / ( x0 - xc) if x0 != xc else float('inf')
        rotateAngle0 = np.arctan(m[0]) + np.pi*np.heaviside(xc - x0, 0) 
        m[1] = ( y1 - yc ) / ( x1 - xc) if x1 != xc else float('inf')
        rotateAngle1 = np.arctan(m[1]) + np.pi*np.heaviside(xc - x1, 0)

        #rotateAngle = sorted([rotateAngle0, rotateAngle1])
        rotateAngle = [rotateAngle0, rotateAngle1]
        
        _size = rotateAngle[1] - rotateAngle[0]
        self._size = np.pi*( 1 - np.sign( _size ) ) + _size
        self.calc_cx_cy_ra(arc = self._size)
        

        self.rotate = self.centre, rotateAngle[0]


    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
