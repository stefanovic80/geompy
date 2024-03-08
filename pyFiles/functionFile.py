# function.py
from . import plt, np, random
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point
from .lineFile import line
from .dataExploreFile import dataExplore

#to be fixed according with real values of xlim and ylim
x = np.arange(-10, 10, 0.01)

class function(dataExplore):

    def __init__(self, draw = False):
        
        super().__init__()
        #plotSett.__init__(self)

        self._color = random.choice(self.colors)

        self.j = 0
        self.k = 0
        if draw == True:
            self.draw()

    @property
    def points(self):
        pass

    @points.setter
    def points(self, array):
        self.data[0] = x
        self.data[1] = array
        self.onlyDraw()
    
    
    
    def chooseCalc(self, angle = 2*np.pi):
        self.__del__()

        calculation_functions = [self.calc]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    self.lims()
                    #calc_function(angle = angle)
                    break
                except:
                    pass
    

    #to be partially inherited
    def erase(self):
        self.__del__()

        #self._points = []
        self.data = [None, None]
        self._center.coords = [None, None]
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
    
