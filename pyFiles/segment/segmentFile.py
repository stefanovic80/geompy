# lineFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings

#plt.ion()

from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

class segment(dataExplore):
    def __init__(self, point0 = None, point1 = None, seed = seed, draw = True):

        super().__init__()
         
        _color = random.choice(self.colors)
        if point0 is None:
            point0 = point()
            point0.color = _color

        if point1 is None:
            point1 = point()
            point1.color = _color

        self.seed = seed
        self._color = random.choice(self.colors)
        
        
        self.endpoint = [point0, point1]
        
        if draw == True:
            self.addParams('point0', self.endpoint[0])
            self.addParams('point1', self.endpoint[1])
            self.calc()
            self.onlyDraw()
    def calc(self):
        self.data[0] = np.array([self.endpoint[0].x[0], self.endpoint[1].x[0] ])
        self.data[1] = np.array([self.endpoint[0].y[0], self.endpoint[1].y[0] ])

    #to be deprecated
    def chooseCalc(self):
        self.__del__()
        calculation_functions = [self.calc]
        
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

