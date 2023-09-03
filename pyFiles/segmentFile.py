# modulo.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class segment(plotSett):

    def __init__(self, xmin= -20, xmax = 20, steps = 500):
        
        super().__init__(xmin, xmax, steps)

        #angles = np.arange(-np.pi, np.pi, 0.1)
        #angle = random.choice(angles)
        self.idxMin = None
        self.idxMax = None

        self.color = random.choice(self.colors)
        self.xMin = self.xmin
        self.xMax = self.xmax


        self.lines = None
        self.data = None
        self.point = [point(), point()]
        self.angCoeff = None #np.tan(angle)
        self.intercept = None #np.random.randint(self.xmin, self.xmax) #change to make decimal possible








    def calc1(self): #calculate equation from two points
        self.remove()

        #x0, y0 = self.point[0].coords[0], self.point[0].coords[1]
        #x1, y1 = self.point[1].coords[0], self.point[1].coords[1]

        #self.angCoeff = (y1 - y0)/(x1 - x0)
        #self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
        #self.intercept = -self.angCoeff*x0 + y0
        #to find out straight line when u know angCoeff and 1 point coords

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]










    def calc2(self): #calculate equation from two points
        self.remove()

        x0, y0 = self.point[0].coords[0], self.point[0].coords[1]
        x1, y1 = self.point[1].coords[0], self.point[1].coords[1]

        self.angCoeff = (y1 - y0)/(x1 - x0)
        self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
        #self.intercept = -self.angCoeff*x0 + y0 
        #to find out straight line when u know angCoeff and 1 point coords

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]


    
    def calc3(self): #calculate equation from 1 point and angCoeff
        self.remove()
        
        x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
        self.intercept = -self.angCoeff*x0 + y0 
        #to find out straight line when u know angCoeff and 1 point coords

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]




    def calc4(self): #calculate equation from 1 point and intercept
        self.remove()
        
        j = 0
        x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
        self.angCoeff = (y0 - self.intercept)/x0

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]






    def rm(self):
        self.lines = None
        self.data = None
        self.point[0].coords = [None, None]
        self.point[1].coords = [None, None]
        self.angCoeff = None
        self.intercept = None
        """
        for attr in self.__dict__:
            print(attr)
            setattr(self, attr, None)
        """

    def draw(self):
        try:
            self.calc1()
        except:
            try:
                self.calc2()
            except:
                try:
                    self.calc3()
                except:
                    try:
                        self.calc4()
                    except:
                        pass

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color)

        self.lines = []
        self.lines.append(line)

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"
            f"\033[93mClass type:\033[0m Segment\n"
            f"\033[93mangCoeff:\033[0m {self.angCoeff}\n"
            f"\033[93mintercept:\033[0m {self.intercept}\n"
            f"\033[93mxMin:\033[0m {self.xMin}\n"
            f"\033[93mxMax:\033[0m {self.xMax}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            #f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
            f"\033[93mlinewdith:\033[0m {self.linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mremove()\033\n"
            f"\033[93mpoint[0]\033\n"
            f"\033[93mpoint[1]\033\n"
        )            
        
        return attributes + methods + self.plotSettings

