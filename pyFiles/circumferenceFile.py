# circumference.py
from . import plt, np, random
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point
from .lineFile import line
from .dataExploreFile import dataExplore
from .circumferenceCalcFile import circumferenceCalc

class circumference(dataExplore, circumferenceCalc):
    
    dof = 3

    def __init__(self, draw = True):
        
        super().__init__()
        #plotSett.__init__(self)

        self._radius = random.uniform(0, (settings.ymax-settings.ymin)/2)
        self._centre = point(draw = False)
        
        self.angles = None
        self._angle = 2*np.pi
        self._color = random.choice(self.colors)

        self._centre._color = self._color 
        self.j = 0
        self.k = 0
        

        self.draws = {
                ('a', 'b', 'c'): self.calc_a_b_c,
                ('C', 'a', 'b'): self.calc_a_b_C,
                ('a', 'b', 'p'): self.calc_a_b_p,
                ('a', 'b', 'r'): self.calc_a_b_r,
                ('a', 'c', 'r'): self.calc_a_c_r,
                ('C', 'b', 'c'): self.calc_b_c_C,
                ('b', 'c', 'p'): self.calc_b_c_p,
                ('b', 'c', 'r'): self.calc_b_c_r,

                ('C', 'c'): self.calc_c_C,
                ('c', 'p'): self.calc_c_p,
                ('C', 'r'): self.calc_C_r,
                
                ('p', 'p', 'p'): self.calc_p_p_p,
                ('a', 'p', 'p'): self.calc_a_p_p,
                ('b', 'p', 'p'): self.calc_b_p_p,
                ('c', 'p', 'p'): self.calc_c_p_p,
                }



        self.dof = 3

        self._a = None
        self._b = None
        self._c = None

        if draw == True:
            self.addParams('radius', self._radius)
            self.addParams('Centre', self._centre)
            self.draw_C()


    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self.__del__()
        if angle > 0:
            self._angle = angle
        elif angle < 0:
            self._angle = 2*np.pi + angle
        self.chooseCalc( angle = self._angle )
        
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self._color)

        self.lines = []
        self.lines.append(line)
        self.label(self._name)

   
    @property
    def centre(self):
        return self._centre

    @centre.setter
    def centre(self, point):
        self.addParams('Centre', point)
        self._centre = point
        self.drawSetts()
       

    @property
    def center(self):
        return self._centre

    @centre.setter
    def center(self, point):
        self.addParams('Centre', point)
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
        self.drawSetts()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self.addParams('b', value)
        self._b = value
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

    
    def pointsSelect(self, angle = 2*np.pi):
        
        try:
            condition = self.angles < angle
            idxs = np.where(self.angles[condition])
            idxs = np.where(self.data[0][condition])
            self.data[0] = self.data[0][idxs]
            self.data[1] = self.data[1][idxs]
        except:
            pass

    def draw_C(self):
        self.__del__()
        
        lok = list( self.params.keys()) #List Of Keys
        if 'radius' in self.params.keys():
            self.calc_C_r()
            self.onlyDraw()
        elif any( 'point' in key for key in lok):
            self.calc_C_p()


    def draw_r(self):
        self.__del__()

        if 'Centre' in self.params.keys():
            self.calc_C_r()
            self.onlyDraw()
        elif any('point' in key for key in lok):
            self.calc_C_p()
            self.onlyDraw()
        
    def draw(self):
        self.__del__()
        prefix = 'point'

        #1) centre and radius
        if 'Centre' in self.params.keys() and 'radius' in self.params.keys():
            self.calc_C_r()
            self.onlyDraw()

        #2) centre, 1 point
        elif 'Centre' in self.params.keys() and any(isinstance(key, str) and key.startswith("point") for key in self.params.keys() ):
            self.calc_C_p()
            self.onlyDraw()

        #3) all points
        elif all(isinstance(key, str) and key.startswith("point") for key in self.params.keys() ):
            self.calc_p_p_p()
            self.onlyDraw()
        else:
            pass
    
    def draw_a(self):
        self.__del__()
        lok = list( self.params.keys() )
        if 'b' in lok and 'c' in lok:
            self.calc_a_b_c()
            self.onlyDraw()
    
    def draw_b(self):
        self.__del__()
        lok = list( self.params.keys() )
        if 'a' in lok and 'c' in lok:
            self.calc_a_b_c()
            self.onlyDraw()


    def draw_c(self):
        self.__del__()
        lok = list( self.params.keys() )
        if 'a' in lok and 'b' in lok:
            self.calc_a_b_c()
            self.onlyDraw()


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
    
