# lineFile.py
from . import plt, np, random
#from . import xmin, xmax, steps, linewidth, seed

from . import seed#steps, linewidth, seed
from .Settings import settings#xmin, xmax, linewidth, steps

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point


class line(plotSett):

    def __init__(self, seed = seed, draw = True):# xmin = settings.xmin, xmax = settings.xmax, steps = settings.steps, seed = seed, draw = True):
        
        super().__init__()#xmin, xmax, steps)
        
        self.seed = seed

        #.xMin and .xMax indexes to cut off the straight line into a line
        self.idxMin = None
        self.idxMax = None

        self._color = random.choice(self.colors)
        #self.xMin and self.xMax cut off the straight line into a line
        self.xMin = settings.xmin
        self.xMax = settings.xmax

        #random points from which the straight line is identified
        point1 = point(draw = False)
        point2 = point(seed = seed + 1, draw = False)
        self.point = [point1, point2]
        
        #values to calculate straight line data (self.data[1])
        self.angCoeff = None #np.tan(angle)
        self.intercept = None
        self.length = None
        self._cut = False
        self.j = 0

        if draw == True:
            self.draw()

    @property
    def m(self):
        return self.angCoeff

    @m.setter
    def m(self, value):
        self.angCoeff = value

    @property
    def q(self):
        return self.intercept

    @q.setter
    def q(self, value):
        self.intercept = value


    @property
    def cut(self):
        self._cut = not self._cut
        self.draw()#cut = self._cut)
        self.label( self._name )





    @property
    def equation(self):
        #super().equation
        
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
        
        if self.q > 0:
            sign = '+'
        elif self.q <0:
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









    def calc1(self): #calculate equation from angCoeff and intercept
        if self._cut == False:
            self.xMin = settings.xmin
            self.xMax = settings.xmax
        
        self.idxMin = np.where( self._x >= self.xMin)[0][0]
        self.idxMax = np.where( self._x >= self.xMax)[0][0]
        self.data = [ self._x[ self.idxMin: self.idxMax] ] # a local copy of x values

        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        
        #[ [x, y] for x, y in zip(r.data[0], r.data[1])]

    def calc2(self): #calculate equation from two points

        x0, y0 = self.point[0].coords[0], self.point[0].coords[1]
        x1, y1 = self.point[1].coords[0], self.point[1].coords[1]
        
        self.length = ( ( x0 - x1  )**2 + ( y0 -y1  )**2  )**.5

        if x1 != x0:
            self.angCoeff = (y1 - y0)/(x1 - x0)
            self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
            j = 0 
            if self._cut == True:
                j = 0
                lims = [ self.point[0].coords[j], self.point[1].coords[j] ]
                lims.sort()
                self.xMin = lims[0]
                self.xMax = lims[1]
            
            self.calc1()
        else:
            L = len(self._x)
            self.data = [np.zeros(L) + x1]
            self.data = self.data + [ self._x ]

            if self._cut == True:
                j = 1
                lims = [ self.point[0].coords[j], self.point[1].coords[j] ]
                lims.sort()
                self.xMin = lims[0]
                self.xMax = lims[1]
                self.idxMin = np.where( self.data[j] >= self.xMin )[0][0]
                self.idxMax = np.where( self.data[j] >= self.xMax )[0][0]

                self.data[0] = self.data[0][self.idxMin: self.idxMax]
                self.data[1] = self.data[1][self.idxMin: self.idxMax]



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
        calculation_functions = [self.calc2, self.calc1, self.calc3, self.calc4]
        
        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()
                    break
                except:
                    pass
    
    def dist(self, length = None ):#to be fixed
        idx = round( len( self.data[0] )*length/self.length )

        return [ self.data[0][idx], self.data[1][idx] ]

    

    def erase(self):
        self.__del__()

        self.data = [None, None]
        #points to be removed or not to be removed. This is the problem!!!
        for j in range(2):
            self.point[j].coords = [None, None]
        
        self.angCoeff = None
        self.intercept = None

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m line\n"
            f"\033[93m.angCoeff = \033[0m {self.angCoeff}\n"
            f"\033[93m.intercept = \033[0m {self.intercept}\n"
            f"\033[93m.xMin = \033[0m {self.xMin}\n"
            f"\033[93m.xMax = \033[0m {self.xMax}\n"
            f"\033[93m.color = \033[0m {self._color}\n"
            f"\033[93m.linewdith =\033[0m {self._linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033\n"
            f"\033[93m.point[0].coords = [{self.point[0].coords[0]}, {self.point[0].coords[1]}]\033\n "
            f"\033[93m.point[1].coords = [{self.point[1].coords[0]}, {self.point[1].coords[1]}]\033[0m\n"
        )            
        
        return attributes + methods + self.plotSettings

