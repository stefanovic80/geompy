# modulo.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett


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

    
    def draw(self, xMin = None, xMax = None):
        
        self.remove()
        try:
        	idxMin = np.where( self.x >= xMin)[0][0]
        	idxMax = np.where( self.x >= xMax)[0][0]
        except:
        	idxMin = np.where( self.x >= self.xmin)[0][0]
        	idxMax = np.where( self.x >= self.xmax)[0][0]
        	
        x = self.x[idxMin: idxMax] # a local copy of x values
        self.data = self.angCoeff*x + self.intercept
        line, = self.ax.plot(x, self.data, linewidth=2, color = self.color)

        self.lines = []
        self.lines.append(line)

    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"
            f"\033[93mType:\033[0m Segment\n"
            f"\033[93mangCoeff:\033[0m {self.angCoeff}\n"
            f"\033[93mintercept:\033[0m {self.intercept}\n"
            f"\033[93mxmin:\033[0m {self.xmin}\n"
            f"\033[93mxmax:\033[0m {self.xmax}\n"
            f"\033[93mx:\033[0m {self.x}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            #f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mremove()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

