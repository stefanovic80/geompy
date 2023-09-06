# triangle.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .segmentFile import segment

class triangle(plotSett):


    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth):
        
        super().__init__(xmin, xmax, steps, linewidth)

        self.segment = [segment(), segment(), segment()]
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        #x.sort(reverse = True)
        #y.sort(reverse = True)
        #angCoeff calculation

    def draw(self):
        self.__del__()
        
        self.data = [None, None, None]
        
        for j in range(3):
            self.segment[j].calc()
            self.data = self.segment[j].data
            #self.segment[j].draw()

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mType:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93mradius:\033[0m {self.radius}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93mcenter\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
