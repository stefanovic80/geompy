# lineFile.py
from . import plt, np, random
from . import seed
from .Settings import settings

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore

class line(dataExplore):
    def __init__(self, seed = seed, draw = True):
        
        super().__init__()
        
        self.seed = seed
        self._color = random.choice(self.colors)

        #values to calculate straight line data (self.data[1])
        angle = random.uniform(0, np.pi)
        self.angle = angle
        self.angCoeff =  np.tan(angle)
        self.intercept = np.random.uniform(settings.xmin, settings.xmax)

        if draw == True:
            self.draw()


    @property
    def m(self):
        return self.angCoeff


    @m.setter
    def m(self, value):
        self.angCoeff = value
        try:
            self.draw()
        except:
            pass


    @property
    def q(self):
        return self.intercept

    @q.setter
    def q(self, value):
        self.intercept = value
        try:
            self.draw()
        except:
            pass


    def system(self, line):
        x = -(self.intercept - line.intercept)/(self.angCoeff - line.angCoeff)
        y = self.angCoeff*x + self.intercept
        return point(x, y)


    def calc1(self): #calculate equation from angCoeff and intercept
        self.data = [self._x]
        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        self.angle = np.arctan(self.angCoeff)
        

    def calc2(self): #calculate equation from two points

        x0, y0 = self._points[0].coords[0], self._points[0].coords[1]
        x1, y1 = self._points[1].coords[0], self._points[1].coords[1]
        
        self.length = ( ( x0 - x1  )**2 + ( y0 -y1  )**2  )**.5

        if x1 != x0:
            self.angCoeff = (y1 - y0)/(x1 - x0)
            self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
            j = 0 
            
            lims = [ self._points[0].coords[j], self._points[1].coords[j] ]
            lims.sort()
            settings.xmin = lims[0]
            settings.xmax = lims[1]
            
            self.calc1()
        else:
            L = len(self._y)
            self.data = [np.zeros(L) + x1]
            self.data = self.data + [ self._y ]


    def calc3(self): #calculate equation from 1 point and angCoeff
        j = 0
        x0, y0 = self._points[j].coords[0], self._points[j].coords[1]
        self.intercept = -self.angCoeff*x0 + y0
        
        self.calc1()
    
    
    def calc4(self): #calculate equation from 1 point and intercept
        j = 0
        x0, y0 = self._points[j].coords[0], self._points[j].coords[1]
        self.angCoeff = (y0 - self.intercept)/x0
        
        self.calc1()
    

    def chooseCalc(self):
        self.__del__()
        calculation_functions = [self.calc2, self.calc1, self.calc3, self.calc4]
        
        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    self.lims()
                    calc_function()
                    break
                except:
                    pass
    
    @property
    def dataGroup(self):
        return self.data + self.labCoords

    @dataGroup.setter
    def dataGroup(self, value):
        self.data = value[0:2]
        #self.labCoords = value[2:4]
        #to be implemented!



    def erase(self):
        self.__del__()

        self.data = [None, None]
        self.angCoeff = None
        self.intercept = None


    @property
    def equation(self):

        #to be (properly) inherited
        try:
            self.tex.remove()
        except:
            pass

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]
        random_index = np.random.randint(len(data[0]))
        shift = (settings.xmax - settings.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        #--------------------

        if self.intercept > 0:
            sign = '+'
        elif self.intercept <0:
            sign = '-'

        q = str(round(abs( self.q), 2))
        m = str(round(self.m, 2))
        eq = "y = " + m + "x" + sign + q
        try:
            eq = self._name + ": " + eq
        except:
            pass
        #labelx, labely may necessitte to be attributes
        if self.j%2 == 0:
            self.tex = self.ax.text(labelx, labely, eq, fontsize = 12, color = self._color, ha="center", va="center")
        self.j += 1


    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m line\n"
            f"\033[93m.m = \033[0m {self.angCoeff}\n"
            f"\033[93m.q = \033[0m {self.intercept}\n"
            f"\033[93m.color = \033[0m {self._color}\n"
            f"\033[93m.linewdith =\033[0m {self._linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

