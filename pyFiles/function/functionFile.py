# function.py
from .. import plt, np, random
from ..Settings import settings

from .._plotSettFile import plotSett
from ..pointFile import point
from ..line.lineFile import line
from ..dataExploreFile import dataExplore

#to be fixed according with real values of xlim and ylim
x = np.arange(settings.xmin, settings.xmax, 1/settings.steps)

#def xSet(settings.xmin, ssettings.xmax, 1/settings.steps):
#    return np.arange(settings.xmin, settings.xmax, 1/settings.steps)
#x = xSet(settings.xmin, ssettings.xmax, 1/settings.steps)

class function(dataExplore):

    def __init__(self, draw = False):
        
        super().__init__()
        #plotSett.__init__(self)

        self._color = random.choice(self.colors)

        if draw: self.onlyDraw()

    #to be modified
    @property
    def y(self):
        return self.data[1]
        """
        try:
            return self.data[1]
        except:
            pass
        """
    @y.setter
    def y(self, array):
        self.data[0] = x#np.arange
        self.data[1] = array
        self.onlyDraw()

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewidth = \033[0m {self.linewidth}  \n"
            f"\033[93m.name = \033[0m {self._name}\n"
        )
        
        
        return attributes +  self.plotSettings
    
