# segment.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth, seed

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class segment(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, seed = seed):
        
        super().__init__(xmin, xmax, steps)
        
        self.seed = seed

        #.xMin and .xMax indexes to cut off the straight line into a segment
        self.idxMin = None
        self.idxMax = None

        self.color = random.choice(self.colors)
        #self.xMin and self.xMax cut off the straight line into a segment
        self.xMin = self.xmin
        self.xMax = self.xmax

        #according with matplotlib self.lines.remove() removes the plot
        self.lines = None
        self.data = None #[None, None]

        #random points from which the straight line is identified
        point1 = point(xmin = xmin, xmax = xmax)
        point2 = point(xmin = xmin, xmax = xmax, seed = seed + 1)
        self.point = [point1, point2]
        
        #point choosen for labeling
        self.pointLabel = point()
        self.pointLabel.coords = [None, None]
        self.pointLabel.color = 'white'

        #values to calculate straight line data (self.data[1])
        self.angCoeff = None #np.tan(angle)
        self.intercept = None
        self.name = None

    def calc1(self): #calculate equation from angCoeff and intercept

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        
        #labeling
        if self.pointLabel.coords == [None, None]:
            indices = (self.data[1] > xmin ) & (self.data[0] < xmax)
            data0 = self.data[0][indices]
            data1 = self.data[1][indices]
            idx = int(len(data[0])/2)
            self.pointLabel.coords = [data0[idx], data1[idx + 10] ]

    def calc2(self): #calculate equation from two points

        x0, y0 = self.point[0].coords[0], self.point[0].coords[1]
        x1, y1 = self.point[1].coords[0], self.point[1].coords[1]

        self.angCoeff = (y1 - y0)/(x1 - x0)
        self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
        
        self.calc1()

    def calc3(self): #calculate equation from 1 point and angCoeff
        j = 0
        
        for j in range(2):
            try:
                x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
                self.intercept = -self.angCoeff*x0 + y0
            except:
                pass
        
        self.calc1()

    def calc4(self): #calculate equation from 1 point and intercept

        for j in range(2):
            try:
                x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
                self.angCoeff = (y0 - self.intercept)/x0
            except:
                pass
        
        self.calc1()

    def chooseCalc(self):
        self.__del__()
        try:
            self.calc1()#intercept, angCoeff
        except:
            try:
                self.calc2() #two points
            except:
                try:
                    self.calc3() # 1point, angCoeff
                except:
                    try:
                        self.calc4()# 1point, intercept
                    except:
                        pass


    def draw(self, name = None ):
        #self.pointLabel.set_text("")
        self.chooseCalc()
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color)

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

    def erase(self):
        self.__del__()
        
        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]

        for j in range(2):
            self.point[j].coords = [None, None]
        #for u in self.point:
        #    u.coords = [None, None]

        self.angCoeff = None
        self.intercept = None

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m Segment\n"
            f"\033[93m.angCoeff = \033[0m {self.angCoeff}\n"
            f"\033[93m.intercept = \033[0m {self.intercept}\n"
            f"\033[93m.xMin = \033[0m {self.xMin}\n"
            f"\033[93m.xMax = \033[0m {self.xMax}\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewdith =\033[0m {self.linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.draw()\033[0m\n"
            f"\033[93m.erase()\033\n"
            f"\033[93m.point[0].coords = [{self.point[0].coords[0]}, {self.point[0].coords[1]}]\033\n "
            f"\033[93m.point[1].coords = [{self.point[1].coords[0]}, {self.point[1].coords[1]}]\033[0m\n"
        )            
        
        return attributes + methods + self.plotSettings

