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
        self._params['m'] = np.tan(angle)
        
        self.intercept = np.random.uniform(settings.ymin, settings.ymax)
        self._params['q'] = self.intercept

        self.degreesOfFreedom = 2
        if draw == True:
            self.draw()
            #self._params_generator()


    


    @property
    def m(self):
        return self.angCoeff


    @m.setter
    def m(self, value):
        idx = list(self._params.keys())[0]
        del self._params[idx]
        
        self._params['m'] = value
        self.angCoeff = value
        self.draw()


    @property
    def q(self):
        return self.intercept

    @q.setter
    def q(self, value):

        idx = list(self._params.keys())
        if idx[0] == 'q':
            del self._params[idx[0]]
        else:
            del self._params[idx[1]]

        self._params['q'] = value
        self.intercept = value
        self.draw()


    def system(self, line):
        x = -(self.intercept - line.intercept)/(self.angCoeff - line.angCoeff)
        y = self.angCoeff*x + self.intercept
        return point(x, y)


    def m_q(self): #calculate equation from angCoeff and intercept
        self.data = [self._x]
        self.data = self.data + [ self.angCoeff*self.data[0] + self.intercept ]
        self.angle = np.arctan(self.angCoeff)
        

    def point_point(self): #calculate equation from two points

        x0, y0 = self._params[0].coords[0], self._params[0].coords[1]
        x1, y1 = self._params[1].coords[0], self._params[1].coords[1]
        
        self.length = ( ( x0 - x1  )**2 + ( y0 -y1  )**2  )**.5

        if x1 != x0:
            self.angCoeff = (y1 - y0)/(x1 - x0)
            self.intercept = y0 - (y1 - y0)*x0/(x1 - x0)
            j = 0 
            
            lims = [ self._params[0].coords[j], self._params[1].coords[j] ]
            lims.sort()
            settings.xmin = lims[0]
            settings.xmax = lims[1]
            
            self.m_q()
        else:
            L = len(self._y)
            self.data = [np.zeros(L) + x1]
            self.data = self.data + [ self._y ]


    def point_m(self): #calculate equation from 1 point and angCoeff
        j = 0
        x0, y0 = self._params[self.pp].coords[0], self._params[self.pp].coords[1]
        self.intercept = -self.angCoeff*x0 + y0
        
        self.m_q()
    
    
    def point_q(self): #calculate equation from 1 point and intercept
        j = 0
        x0, y0 = self._params[self.pp].coords[0], self._params[self.pp].coords[1]
        self.angCoeff = (y0 - self.intercept)/x0
        
        self.m_q()
    

    def chooseCalc(self):
        self.__del__()

        if 'm' in self._params.keys() and 'q' in self._params.keys():
            self.m_q()
        elif 'm' in self._params.keys() and any(isinstance(k, int) for k in self._params.keys()):# in self._params.keys():
            self.point_m()
        elif 'q' in self._params.keys() and any(isinstance(k, int) for k in self._params.keys()):#'point' in self._params.keys():
            self.point_q()
        else:# 'point' in sel._params.keys() and 'm' not in self._params.keys() and 'q' not in self._params.keys():
            self.point_point()
        
        
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

