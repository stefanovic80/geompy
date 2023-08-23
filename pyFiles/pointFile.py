# pointFile.py
from . import plt, np, random
#matplotlib.plot has to be imported in all pyFiles modules

plt.ion()

from ._plotSettFile import plotSett



class point(plotSett):
    
    def __init__(self, xmin = -20, xmax = 20, steps = 500, linewidth = 2):
        super().__init__( xmin, xmax, steps, linewidth )
        #a = plt.ginput()
        #self.coords = [ a[0][0], a[0][1] ]
        self.coords = [random.randint(-20, 20), random.randint(-20, 20) ]

        self.lines = []
        self.color = random.choice(self.colors)
        self.name = None

    def draw(self):
        line = self.ax.scatter( self.coords[0], self.coords[1], color = self.color, linewidth = self.linewidth)
        self.lines = []
        self.lines.append(line)

    def click(self):
        self.remove()
        a = plt.ginput()
        self.coords = [ a[0][0], a[0][1] ]
        self.draw()

    def __str__(self):

        super().__str__()
        
        
        attributes = (
            f"\033[93mType:\033[0m point\n"
            f"\nAttributes:\n"
            f"\033[93mdata:\033[0m {self.coords[0]}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )

        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mclick()\033[0m\n"
            f"\033[93mremove()\033[0m\n"
        )

        return attributes + methods + self.plotSettings

