# circumference.py
from .. import plt, np, random
from ..Settings import settings
#from .._plotSettFile import plotSett
from ..pointFile import point
from ..line.lineFile import line
#from ..dataExploreFile import dataExplore

from ..keys.circumference_listOfKeys import method

"""
class custom_point(point):  # Estendi la classe point
    @property
    def x(self):
        print("it's working!")
        return super().x()

    @x.setter
    def x(self, value):
        print(f"Setting x to {value}")
        super(custom_point, self.__class__).x.__set__(self, value)
"""

class circumference(method):
    
    dof = 3

    def __init__(self, draw = True):
        
        super().__init__()
        #plotSett.__init__(self)

        self._radius = random.uniform(0, (settings.ymax-settings.ymin)/2)
        self.addParams('radius', self._radius)
        
        self._centre = point(draw = False)
        #self._centre = custom_point(draw=False)

        self.addParams('cx', self._centre.coords[0])
        self.addParams('cy', self._centre.coords[1])

        self.angles = None
        self._arc = 2*np.pi
        self._color = random.choice(self.colors)

        self._centre._color = self._color 
        self.j = 0
        self.k = 0
        
        if draw: self.drawSetts()
        
        """
        #decorazione dinamica
        def new_x():
            print("it's working!")

        self._centre.x = new_x.__get__(self._centre, point)
        """
    @property
    def arc(self):
        return self._arc

    @arc.setter
    def arc(self, arc):
        self.__del__()
        if arc > 0:
            self._arc = arc
        elif arc < 0:
            self._arc = 2*np.pi + arc
        
        self.calc_cx_cy_ra( name = None, arc = self._arc )
        #self.chooseCalc( angle = self._angle )
        
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self._color)

        self.lines = []
        self.lines.append(line)
        self.label(self._name)

   
    @property
    def centre(self):
        return self._centre

    @centre.setter
    def centre(self, point):
        self.addParams('cx', point.coords[0])
        self.addParams('cy', point.coords[1])
        self._centre = point 
        self.drawSetts()
    
    @property
    def centre_x(self):
        return self._centre.coords[0]

    @centre_x.setter
    def centre_x(self, value):
        self.centre.coords[0] = self.centre.data[0] = value
        self.addParams('cx', value)
        self.drawSetts()

    @property
    def centre_y(self):
        return self._centre.coords[1]
    
    @centre_x.setter
    def centre_y(self, value):
        self.centre.coords[1] = self.centre.data[1] = value
        self.addParams('cy', value)
        self.drawSetts()



    @property
    def center(self):
        return self._centre

    @centre.setter
    def center(self, point):
        self.addParams('centre', point)
        self._centre = point
        self.drawSetts()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self.addParams('radius', r)
        self._radius = r
        self.drawSetts()

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self.addParams('a', value)
        self._a = value
        self._centre.coords[0] = self._centre.data[0] = - value/2
        self.drawSetts()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self.addParams('b', value)
        self._b = value
        self._centre.coords[1] = self._centre.data[1] = - value/2
        self.drawSetts()


    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self.addParams('c', value)
        self._c = value
        self.drawSetts()


    def tangent(self, point):
        xc = self._centre.data[0]
        yc = self._centre.data[1]
        x0 = point.data[0]
        y0 = point.data[1]
        R = self.radius
        dist = ( (xc - x0)**2 + (yc - y0)**2)**.5
        angle1 = np.arcsin( (yc - y0)/dist )
        angle2 = np.arcsin( R/dist)
        if xc >= x0:
            m0 = np.tan( angle1 + angle2 )
            m1 = np.tan( angle1 - angle2 )
        elif xc < x0:
            m0 = np.tan( np.pi - angle1 - angle2 )
            m1 = np.tan( np.pi - angle1 + angle2 )
        l = line()
        l.points = point
        if self.k%2 == 0:
            l.m = m0[0]
            self.k += 1
        else:
            l.m = m1[0]
            self.k += 1
        return l

    
    def pointsSelect(self, arc = 2*np.pi):
        
        try:
            condition = self.angles < arc
            idxs = np.where(self.angles[condition])
            idxs = np.where(self.data[0][condition])
            self.data[0] = self.data[0][idxs]
            self.data[1] = self.data[1][idxs]
        except:
            pass

    #to be partially inherited
    def erase(self):
        self.__del__()
        self.data = [None, None]
        self._centre.coords = [None, None]
        self._radius = None

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93m.radius = \033[0m {self._radius}\n"
            #f"\033[93m.x = \033[0m {self.data[0][:10]}...\n"
            #f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewidth = \033[0m {self.linewidth}  \n"
            f"\033[93m.name = \033[0m {self._name}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93m.centre\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
