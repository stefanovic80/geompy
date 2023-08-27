# modulo.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class segment(plotSett):

    def __init__(self, xmin= -20, xmax = 20, steps = 500):
        
        super().__init__(xmin, xmax, steps)

        self.angCoeff = np.random.randint(self.xmin, self.xmax)
        self.intercept = np.random.randint(self.xmin, self.xmax)
        self.idxMin = None
        self.idxMax = None
        self.lines = []
        self.data = None
        self.color = random.choice(self.colors)
    
    def draw(self):
        
        self.remove()
        try:
            idxMin = np.where( self.x >= self.xMin)[0][0]
            idxMax = np.where( self.x >= self.xMax)[0][0]
            self.x = self.x[idxMin: idxMax] # a local copy of x values
        except:
            self.xMin, self.xMax = self.xmin, self.xmax

        
        self.data = self.angCoeff*self.x + self.intercept
        line, = self.ax.plot(self.x, self.data, linewidth=self.linewidth, color = self.color)

        self.lines = []
        self.lines.append(line)

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"
            f"\033[93mType:\033[0m Segment\n"
            f"\033[93mangCoeff:\033[0m {self.angCoeff}\n"
            f"\033[93mintercept:\033[0m {self.intercept}\n"
            f"\033[93mxMin:\033[0m {self.xMin}\n"
            f"\033[93mxMax:\033[0m {self.xMax}\n"
            f"\033[93mx:\033[0m {self.x}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            #f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
            f"\033[93mlinewdith:\033[0m {self.linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mremove()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

