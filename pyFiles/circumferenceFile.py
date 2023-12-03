# circumference.py
from . import plt, np, random
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point

class circumference(plotSett):

    def __init__(self, draw = True):
        
        super().__init__()
        #plotSett.__init__(self)

        self._radius = random.uniform(0, (settings.xmax-settings.xmin)/2)
        self.center = point(draw = False)

        #three points passing through the circumference
        self.point = [None, None, None]
        
        self.angles = None
        self._angle = 2*np.pi
        self._color = random.choice(self.colors)

        self.center._color = self._color 
        self.j = 0

        if draw == True:
            self.draw()
       
        self.a = None
        self.b = None
        self.c = None


    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self.__del__()
        self._angle = angle
        self.chooseCalc(angle = self._angle )
        
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self._color)

        self.lines = []
        self.lines.append(line)
        self.label(self._name)

    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.chooseCalc()
        self.name = self._name


    """
    @property
    def equation(self):
        #to be inherited
        try:
            self.tex.remove()
        except:
            pass

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]
        random_index = np.random.randint(len(data[0]))
        shift = (self.xmax - self.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        #--------------------

        if self.a > 0:
            siga = '+'
        elif self.b <0:
            signb = '-'

        a = str(round(abs( self.a), 2))
        b = str(round(abs( self.b), 2))
        b = str(round(abs( self.c), 2))
        eq = r"$y^2$ = " + m + "x" + sign + q
        #labelx, labely may necessitte to be attributes
        self.tex = self.ax.text(labelx, labely, eq, fontsize = 12, color = self._color, ha="center", va="center")
    """

    
    #circumference equation calculation from center coordinates and radius
    def calc(self, name = None, angle = 2*np.pi):
         
        data = [None, None]

        #1) (pi/2 pi/4)
        data[0] = self._x[ (self._x >= 0 ) & (self._x <= self._radius/2**.5)]
        data[1] = list( np.sqrt( ( self._radius  )**2 - ( data[0]  )**2  ) )
        
        data[0] = list(data[0])
        idx = len(data[0])
        
        #2) extended from (pi/2 pi/4) to (pi/2 0)
        data[0] = data[1] + data[0][::-1]
        data[1] = data[0][idx:][::-1] + data[1][::-1]

        angles = [ np.arctan(y/x) for (y, x) in zip(data[1], data[0]) ]

        #3) extended from (pi/2 0) to (pi 0)
        data[0] = data[0] + [ -x for x in data[0][::-1] ]
        data[1] = data[1] + data[1][::-1]
        
        angles = angles + [ np.pi/2 + ang for ang in angles] 
        
        #4) extended from (pi 0) to (2pi 0)
        data[0] = data[0] + data[0][::-1]
        data[1] = data[1] + [ -x for x in data[1][::-1] ]
        
        angles = angles + [ np.pi + ang for ang in angles]

        #5) connect at the end of the circle
        #data[0] = data[0] + data[0][0]
        #data[1] = data[1] + data[1][1]

        self.angles = np.array(angles)

        self.data = [np.array(data[0]) + self.center.data[0], np.array(data[1]) + self.center.data[1] ]
       
        self.pointsSelect(angle = angle)
        
        self.a = -2*self.center.data[0]
        self.b = -2*self.center.data[1]
        self.c = self.center.data[0]**2 + self.center.data[1]**2 - self._radius**2

    
    def pointsSelect(self, angle = 2*np.pi):
        
        for point in self.point:
            try:
                condition = self.angles < angle
                idxs = np.where(self.angles[condition])
                idxs = np.where(self.data[0][condition])
                self.data[0] = self.data[0][idxs]
                self.data[1] = self.data[1][idxs]
                break
            except:
                pass



        
    # calculate from three points the circumference passing through (to be fixed!)
    def calc2(self, name = None, angle = 2*np.pi):
        x0 = self.point[0].data[0]
        x1 = self.point[1].data[0]
        x2 = self.point[2].data[0]
        
        y0 = self.point[0].data[1]
        y1 = self.point[1].data[1]
        y2 = self.point[2].data[1]
        
        A = np.matrix([ [ x0, y0, 1  ], [ x1, y1, 1  ], [ x2, y2, 1  ] ]) 
        Ainv = np.linalg.inv(A)
        squares = np.array( [ -x0**2 - y0**2  , -x1**2 - y1**2  , -x2**2 - y2**2 ] )
        #circParams = np.dot(Ainv, squares)
        circParams = np.dot(Ainv, squares)

        self.a, self.b, self.c = circParams[0, 0], circParams[0, 1], circParams[0, 2]

        self.center = point(-circParams[0, 0]/2, -circParams[0, 1]/2, draw = False)
        
        self._radius = np.sqrt( (circParams[0, 0]/2)**2 + (circParams[0, 1]/2)**2 - circParams[0, 2]  )
        self.calc()

    # calculate from center coordinates and a point passing through
    def calc3(self, name = None, angle = 2*np.pi):
        
        for point in self.point:
            try:
                        
                x0 = point.data[0]
                y0 = point.data[1]
                x1 = self.center.data[0]
                y1 = self.center.data[1]
                self._radius = np.sqrt( ( x0 - x1  )**2 + ( y0 - y1  )**2  )
                
                self.a = -2*x1
                self.b = -2*y1
                self.c = x1**2 + y1**2 - x0**2 - y0**2

                break
            except:
                pass

        self.calc()


    def chooseCalc(self, angle = 2*np.pi):
        self.__del__()

        self._angle = angle
        calculation_functions = [self.calc, self.calc2, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function(angle = angle)
                    break
                except:
                    pass

    #to be partially inherited
    def erase(self):
        self.__del__()

        self.data = [None, None]
        self.center.data = [None, None]
        self._radius = None

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93m.radius = \033[0m {self._radius}\n"
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewidth = \033[0m {self.linewidth}  \n"
            f"\033[93m.name = \033[0m {self._name}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93m.center\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
