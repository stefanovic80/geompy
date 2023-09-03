# pointFile.py
from . import plt, np, random
#matplotlib.plot has to be imported in all pyFiles modules

plt.ion()

from ._plotSettFile import plotSett



class point(plotSett):
    
    def __init__(self, xmin = -20, xmax = 20, steps = 500, linewidth = 2, bip = 0):
        super().__init__( xmin, xmax, steps, linewidth )
        
        self.coords = [random.randint(self.xmin + bip, self.xmax - bip), random.randint(self.xmin, self.xmax) ]

        self.lines = None
        self.color = random.choice(self.colors)
        self.name = None
        self.j = 0

    def draw(self):
        self.remove()

        line = self.ax.scatter( self.coords[0], self.coords[1], color = self.color, linewidth = self.linewidth)

        self.lines = []
        self.lines.append(line)

        if self.j%2 != 0:
            hline = self.ax.axhline(y = self.coords[1], linestyle = '--', color = 'k', linewidth = 1)
            vline = self.ax.axvline(x = self.coords[0], linestyle = '--', color = 'k', linewidth = 1)
            self.lines.append(hline)
            self.lines.append(vline)
            print("\nrun .draw one more time to erase coordinates\n")
        else:
            print("\nrun .draw one more time to highlight coordinates\n")
        
        self.j+=1


    def click(self):
        self.remove()
        a = plt.ginput()
        self.coords = [ a[0][0], a[0][1] ]
        self.draw()

    def __str__(self):

        super().__str__()
        
        
        attributes = (
            f"\033[93mClass type:\033[0m point\n"
            f"\nAttributes:\n"
            f"\033[93mcoords:\033[0m [{self.coords[0]}, {self.coords[1]}] \n"
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

