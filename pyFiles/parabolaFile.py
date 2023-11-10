# parabolaFile.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth


plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class parabola(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, draw = True):

        super().__init__(xmin, xmax, steps)
        #self.xShift = np.random.randint(xmin, xmax)
        #self.yShift = np.random.randint(xmin, xmax)
        self.vertex = point( np.random.randint(xmin, xmax), np.random.randint(xmin, xmax), draw = False  )
        self.concavity = np.random.randint(-10, 10)/5#to be checked out!
        
        
        self.a = None
        self.b = None
        self.c = None
        
        self.lines = []
        self.point = [None, None, None]
        self.data = None
        self.name =  None
        self.color = random.choice(self.colors)

        #------------------------------------------------------------
        #point choosen for labeling
        self.pointLabel = point( draw = False )
        self.pointLabel.coords = [None, None]
        self.pointLabel.color = 'white'
        #------------------------------------------------------------

        self.rotate = False


        if draw == True:
            self.draw(name = None)

    def erase(self):
        self.__del__()
        
        self.vertex = None
        self.concavity = None
        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = None #[None, None]





    def calc(self, name = None):
        #self.__del__()
        self.data = [ self._x ]
        self.data = self.data + [self.concavity*(self._x - self.vertex.coords[0])**2 + self.vertex.coords[1] ]


    def calc1(self, name = None):

        
        self.calc()


    # calculate from three points the circumference passing through (to be fixed!)
    def calc2(self, name = None):
        x0 = self.point[0].coords[0]
        x1 = self.point[1].coords[0]
        x2 = self.point[2].coords[0]

        y0 = self.point[0].coords[1]
        y1 = self.point[1].coords[1]
        y2 = self.point[2].coords[1]

        A = np.matrix([ [ x0**2, x0, 1  ], [ x1**2, x1, 1  ], [ x2**2, x2, 1  ] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ y0  , y1  , y2 ] )#.reshape(-1, 1)
        parabParams = np.dot(Ainv, y)
        
        self.a = parabParams[0, 0]
        self.b = parabParams[0, 1]
        self.c = parabParams[0, 2]
        
        self.calc1() 
    
    def calc1(self, name = None):

        Delta = self.b**2 - 4*self.a*self.c
        self.vertex = point( -self.b/(2*self.a)  , -Delta/(4*self.a)  )
        self.concavity = self.a
        self.calc()



    def chooseCalc(self):
        self.__del__()

        calculation_functions = [self.calc, self.calc1, self.calc2]#, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()
                    break
                except:
                    pass



    def draw(self, name = None):
        
        self.chooseCalc()

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color, label = self.name) # can be optimized for ALL pictures vi rmParams
        
        self.lines = []
        self.lines.append(line)

        if isinstance(name, str):
            self.name = name

        condition_mask = ( self.data[1] > self.xmin) & (self.data[1] < self.xmax)
        indices = np.where(condition_mask)
        idx = random.choice(indices[0])
        self.pointLabel.coords = [self.data[0][idx], self.data[1][idx] ]

        self.pointLabel.color = self.color
        self.pointLabel.label(name)



    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93m.xShift = \033[0m {self.vertex.coords[0]}\n"
            f"\033[93m.yShift = \033[0m {self.vertex.coords[1]}\n"
            f"\033[93m.concavity = \033[0m {self.concavity}\n"
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            #f"\033[93m.data[0] =\033[0m {self.data[0]}\n"
            #f"\033[93m.data[1] =\033[0m {self.data[1]}\n"
            f"\033[93m.name:\033[0m {self.name}\n"
            f"\033[93m.color:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.draw()\033[0m\n"
            f"\033[93m.erase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings
