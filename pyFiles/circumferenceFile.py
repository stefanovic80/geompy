# circumference.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class circumference(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, draw = True):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2)
        self.center = point(draw = False)
        
        #self.rotate = False        
        #three points passing through the circumference
        self.point = [None, None, None]
        
        #self.center = point(xmin = self.xmin + self.radius, xmax = self.xmax -self.radius)
        self.lines = None
        #self.data = None
        self.angles = None
        #self._name = None
        self._color = random.choice(self.colors)

        self.center._color = self._color
        self.cut = False 
        #------------------------------------------------------
        #point choosen for labeling
        self.pointLabel = point(draw = False)
        self.pointLabel.coords = [None, None]
        self.pointLabel._color = 'white'
        #------------------------------------------------------

        
        if draw == True:
            self.draw()

    #circumference equation calculation from center coordinates and radius
    def calc(self, name = None, angle = 2*np.pi):
        # 
        #if self.cut == False:
        #    self.xMin = self.xmin
        
        data = [None, None]

        #1) (pi/2 pi/4)
        data[0] = self._x[ (self._x >= 0 ) & (self._x <= self.radius/2**.5)]
        data[1] = list( np.sqrt( ( self.radius  )**2 - ( data[0]  )**2  ) )
        
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

        self.data = [np.array(data[0]) + self.center.coords[0], np.array(data[1]) + self.center.coords[1] ]
       
        self.pointsSelect(angle = angle)

    def pointsSelect(self, angle = 2*np.pi):
        
        #self.angles = np.arctan( ( self.data[1] - self.center.coords[1]) / (self.data[0] - self.center.coords[0]) )

        #if angle != 2*np.pi:
        for point in self.point:
            try:
                #condition = self.data[0] > point.coords[0]
                #idxs = np.where(self.data[0][condition])
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
        x0 = self.point[0].coords[0]
        x1 = self.point[1].coords[0]
        x2 = self.point[2].coords[0]
        
        y0 = self.point[0].coords[1]
        y1 = self.point[1].coords[1]
        y2 = self.point[2].coords[1]
        
        A = np.matrix([ [ x0, y0, 1  ], [ x1, y1, 1  ], [ x2, y2, 1  ] ]) 
        Ainv = np.linalg.inv(A)
        squares = np.array( [ -x0**2 - y0**2  , -x1**2 - y1**2  , -x2**2 - y2**2 ] )
        circParams = np.dot(Ainv, squares)
        self.center = point(-circParams[0, 0]/2, -circParams[0, 1]/2, draw = False)
        self.radius = np.sqrt( (circParams[0, 0]/2)**2 + (circParams[0, 1]/2)**2 - circParams[0, 2]  )
        self.calc()

    # calculate from center coordinates and a point passing through
    def calc3(self, name = None, angle = 2*np.pi):
        
        for point in self.point:
            try:
                        
                x0 = point.coords[0]
                y0 = point.coords[1]
                x1 = self.center.coords[0]
                y1 = self.center.coords[1]
                self.radius = np.sqrt( ( x0 - x1  )**2 + ( y0 - y1  )**2  )
                break
            except:
                pass

        self.calc()


    def chooseCalc(self, angle = 2*np.pi):
        self.__del__()
        calculation_functions = [self.calc, self.calc2, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function(angle = angle)
                    break
                except:
                    pass

    """
    def draw(self, name = None, angle = 2*np.pi):
        
        #if isinstance(cut, bool):
        #    self.cut = cut
        
        self.chooseCalc(angle = angle)
    
        line1, = self.ax.plot(self.data[0], self.data[1], color = self.color, label = self._name, linewidth = self.linewidth)
        
        self.lines = []
        self.lines.append(line1)

        #self.ax.set_xlim(self.xmin, self.xmax)
        #self.ax.set_ylim(self.xmin, self.xmax)

        #-------------------------------------------
        if isinstance(name, str):
            self._name = name
        
        
        condition_mask = ( self.data[1] > self.xmin) & (self.data[1] < self.xmax)
        indices = np.where(condition_mask)
        idx = random.choice(indices[0])
        self.pointLabel.coords = [self.data[0][idx], self.data[1][idx] ]

        self.pointLabel._color = self.color
        self.pointLabel.label(self._name)

        #-------------------------------------------
    """ 


    def erase(self):
        self.__del__()

        self.data = [None, None]
        self.center.coords = [None, None]
        self.radius = None

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93m.radius = \033[0m {self.radius}\n"
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
    
