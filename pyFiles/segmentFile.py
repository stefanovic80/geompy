# modulo.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class segment(plotSett):

    def __init__(self, xmin= -20, xmax = 20, steps = 500):
        
        super().__init__(xmin, xmax, steps)

        self.idxMin = None
        self.idxMax = None

        self.color = random.choice(self.colors)
        self.xMin = self.xmin
        self.xMax = self.xmax

        self.lines = None
        self.data = None
        self.point = [point(), point()]
        self.angCoeff = None #np.tan(angle)
        self.intercept = None

    def calc1(self): #calculate equation from angCoeff and intercept
        #self.__del__()

        self.idxMin = np.where( self.x >= self.xMin)[0][0]
        self.idxMax = np.where( self.x >= self.xMax)[0][0]
        self.data = [ self.x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]


    def calc2(self): #calculate equation from two points

        x0, y0 = self.point[0].coords[0], self.point[0].coords[1]
        x1, y1 = self.point[1].coords[0], self.point[1].coords[1]

        self.angCoeff = (y1 - y0)/(x1 - x0)
        self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
        
        self.calc1()
        
    
    def calc3(self): #calculate equation from 1 point and angCoeff
        j = 0
        #try:
        #    x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
        
        for j in range(2):
            try:
                x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
                self.intercept = -self.angCoeff*x0 + y0
        
        #[u for u in self.point if u not in [x0, y0] ]
        
                if j == 0:
                    self.point[j+1].coords = [None, None]
                else:
                    self.point[j-1].coords = [None, None]
            except:
                pass
        
        self.calc1()



    def calc4(self): #calculate equation from 1 point and intercept
        #self.__del__()

        for j in range(2):
            try:
                x0, y0 = self.point[j].coords[0], self.point[j].coords[1]
                self.angCoeff = (y0 - self.intercept)/x0
                if j == 0:
                    self.point[j+1].coords = [None, None]
                else:
                    self.point[j-1].coords = [None, None]
            except:
                pass
        

        self.calc1()
        


    def erase(self):#add self.remove()
        self.__del__()

        self.data = [None, None]
        for j in range(2):
            self.point[j].coords = [None, None]
            #self.point[j].lines.remove()
        self.angCoeff = None
        self.intercept = None
        print(self.__str__() )

    def draw(self):
        self.__del__()
        try:
            self.calc1()#intercept, angCoeff
            for j in range(2):
                 self.point[j].coords = [None, None]
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

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color)

        self.lines = []
        self.lines.append(line)
        print(self.__str__())

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m Segment\n"
            f"\033[93m.angCoeff = \033[0m {self.angCoeff}\n"
            f"\033[93m.intercept = \033[0m {self.intercept}\n"
            f"\033[93m.xMin = \033[0m {self.xMin}\n"
            f"\033[93m.xMax = \033[0m {self.xMax}\n"
            f"\033[93m.data[0] = \033[0m {self.data[0]}\n"
            #f"\033[93mname = \033[0m {self.name}\n"
            f"\033[93m.data[1] = \033[0m {self.data[1]}\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewdith =\033[0m {self.linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.draw()\033[0m\n"
            f"\033[93m.erase()\033\n"
            f"\033[93m.point[0].coords = [{self.point[0].coords[0]}, {self.point[0].coords[1]}]\033\n "
            f"\033[93m.point[1].coords = [{self.point[1].coords[0]}, {self.point[1].coords[1]}]\033\n"
        )            
        
        return attributes + methods + self.plotSettings

