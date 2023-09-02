# parabolaFile.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett


class parabola(plotSett):

    def __init__(self, xmin= -20, xmax = 20, steps = 500):

        super().__init__(xmin, xmax, steps)
        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-(xmax-xmin)/2, + (xmax + xmin)/2)
        self.lines = []
        self.data = None
        self.name =  None
        self.color = random.choice(self.colors)

    def draw(self ):
        self.remove()

        self.data = [ self.x ]

        self.data = self.data + [self.concavity*(self.x - self.xShift)**2 + self.yShift]
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color, label = self.name) # can be optimized for ALL pictures vi rmParams
        
        self.lines = []
        self.lines.append(line)

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93mxShift:\033[0m {self.xShift}\n"
            f"\033[93myShift:\033[0m {self.yShift}\n"
            f"\033[93mconcavity:\033[0m {self.concavity}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mremove()\033[0m\n"
        )

        return attributes + methods + self.plotSettings
