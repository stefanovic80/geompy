#pointFile.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth


plt.ion()

from ._plotSettFile import plotSett
from . import xmin, xmax, steps, linewidth
from . import seed
#from .randomGenFile import randomGen

#seed = 1
#random.seed(seed) #seed automatically imported from main.py

#a = randomGen(seed)
#seed = a.seed

class point(plotSett):
    def __init__(self, pickFrom = None, x = None, y = None, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth, seed = seed):
        super().__init__( xmin, xmax, steps, linewidth)
        
        
        #self.pickFrom = pickFrom
        self.seed = seed
        
        self.coords = [None, None]
        if isinstance(pickFrom, int) or isinstance(pickFrom, float):# coords as point instance arguments
            self.coords[0] = pickFrom
            self.coords[1] = x
            #y = x
        elif pickFrom is None and x is None and y is None:
            pass
            self.randomCoords(self.seed)
        else:#chooce from a geometrical locus
            self.pickFrom = pickFrom.data
            #self.pickFrom = pickFrom
            self.randomPoint()
            #self.draw()
        
        
        #if x is None and y is None:
        #    self.randomCoords(self.seed)

        self.color = random.choice(self.colors)
        self.j = 0

        self.lines = None
        self.text = None
        self.name = None
        
        print(seed)

    def draw(self, name = None):
        self.__del__()

        line = self.ax.scatter( self.coords[0], self.coords[1], color = self.color, linewidth = self.linewidth)
        self.lines = []
        self.lines.append(line)

        if self.j%2 != 0:
            hline = self.ax.axhline(y = self.coords[1], linestyle = '--', color = 'k', linewidth = 1)#, xmax = 4)
            vline = self.ax.axvline(x = self.coords[0], linestyle = '--', color = 'k', linewidth = 1)
            self.lines.append(hline)
            self.lines.append(vline)
            print("\nrun .draw one more time to erase coordinates\n")
        else:
            print("\nrun .draw one more time to highlight coordinates\n")
        
        

        try:
            self.name = name
            self.label()
        except:
            pass

        self.j += 1

    def randomCoords(self, seed):
        #seed = input("chooce a random integer\n")
        self.coords[0] = random.uniform(xmin, xmax)
        self.coords[1] = random.uniform(xmin, xmax)
        self.seed += 1
        seed = self.seed

    
    #random Point from a geometrical locus
    def randomPoint(self):
        idx = np.random.randint(0, len(self.pickFrom[0]) )
        self.coords = [ self.pickFrom[0][idx]  , self.pickFrom[1][idx]  ]



    def click(self):
        self.__del__()

        a = plt.ginput()
        self.coords = [ a[0][0], a[0][1] ]
        self.draw()

    def label(self):
        shift = (self.xmax - self.xmin)/40
        self.text = self.ax.text(self.coords[0] + shift, self.coords[1] + shift, self.name, fontsize = 12, color = self.color, ha="center", va="center")




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
            f"\033[93merase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings

