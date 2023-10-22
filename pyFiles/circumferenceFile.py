# circumference.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class circumference(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2)
        self.center = point()
        
        self.rotate = False        
        #three points passing through the circumference
        self.point = [None, None, None]
        
        #self.center = point(xmin = self.xmin + self.radius, xmax = self.xmax -self.radius)
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        self.center.color = self.color
        
        #------------------------------------------------------
        #point choosen for labeling
        self.pointLabel = point()
        self.pointLabel.coords = [None, None]
        self.pointLabel.color = 'white'
        #------------------------------------------------------


    #circumference equation calculation from center coordinates and radius
    def calc(self, name = None):
         
        data = [None, None]

        #1) (pi/2 pi/4)
        data[0] = self.x[ (self.x >= 0 ) & (self.x <= self.radius/2**.5)]
        data[1] = list( np.sqrt( ( self.radius  )**2 - ( data[0]  )**2  ) )
        
        data[0] = list(data[0])
        idx = len(data[0])
        
        #2) extended from (pi/2 pi/4) to (pi/2 0)
        data[0] = data[1] + data[0][::-1]
        data[1] = data[0][idx:][::-1] + data[1][::-1]
        
        #3) extended from (pi/2 0) to (pi 0)
        data[0] = data[0] + [ -x for x in data[0][::-1] ]
        data[1] = data[1] + data[1][::-1]

        #4) extended from (pi 0) to (2pi 0)
        data[0] = data[0] + data[0][::-1]
        data[1] = data[1] + [ -x for x in data[1][::-1] ]
        
        #5) connect at the end of the circle
        #data[0] = data[0] + data[0][0]
        #data[1] = data[1] + data[1][1]

        self.data = [np.array(data[0]) + self.center.coords[0], np.array(data[1]) + self.center.coords[1] ]

    # calculate from three points the circumference passing through (to be fixed!)
    def calc2(self, name = None):
        x0 = self.point[0].coords[0]
        x1 = self.point[1].coords[0]
        x2 = self.point[2].coords[0]
        
        y0 = self.point[0].coords[1]
        y1 = self.point[1].coords[1]
        y2 = self.point[2].coords[1]
        
        a = (x0 + x1 + x2)/3
        b = (y0 + y1 + y2)/3
        
        self.center = point(a, b)
        self.radius = np.sqrt( (x0-a)**2 + (y0 - b)**2)
        self.calc()

    # calculate from center coordinates and a point passing through
    def calc3(self, name = None):
        x1 = self.point[0].coords[0]
        y1 = self.point[0].coords[1]

        x0 = self.center.coords[0]
        y0 = self.center.coords[1]

        self.radius = np.sqrt( ( x0 - x1  )**2 + ( x0 - x1 )**2  )
        self.calc()
    
    def chooseCalc(self):
        self.__del__()
        calculation_functions = [self.calc, self.calc2, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()
                    break
                except:
                    pass


    def draw(self, name = None):
        
        self.chooseCalc()

        line1, = self.ax.plot(self.data[0], self.data[1], color = self.color, label = self.name, linewidth = self.linewidth)
        
        self.lines = []
        self.lines.append(line1)

        #self.ax.set_xlim(self.xmin, self.xmax)
        #self.ax.set_ylim(self.xmin, self.xmax)
        #-------------------------------------------
        if isinstance(name, str):
            self.name = name
        

        condition_mask = ( self.data[1] > self.xmin) & (self.data[1] < self.xmax)
        indices = np.where(condition_mask)
        idx = random.choice(indices[0])
        self.pointLabel.coords = [self.data[0][idx], self.data[1][idx] ]

        self.pointLabel.color = self.color
        self.pointLabel.label(self.name)

        #-------------------------------------------


    def erase(self):#add self.remove()
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
            f"\033[93m.name = \033[0m {self.name}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93m.center\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
