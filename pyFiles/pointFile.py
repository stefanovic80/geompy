# pointFile.py
from . import plt, np, random, time
from . import xmin, xmax, steps, linewidth

#matplotlib.plot has to be imported in all pyFiles modules

plt.ion()

from ._plotSettFile import plotSett
from . import xmin, xmax, steps, linewidth

x = random.uniform(xmin, xmax)
y = random.uniform(xmin, xmax)


class point(plotSett):
    
    def __init__(self, pickFrom = None, x = x, y = y, xmin = -20, xmax = 20, steps = 500, linewidth = 2):
        super().__init__( xmin, xmax, steps, linewidth )

        
        p = (isinstance(pickFrom, int) or isinstance(pickFrom, float) or pickFrom == None)
        print(p)
        #if p == True:
        #    x = pickFrom
        #    y = x
        self.coords = [x, y]
        #else: 
        try:
            self.pickFrom = pickFrom.data
        except:
            self.pickFrom = pickFrom
        
        self.lines = None
        self.color = random.choice(self.colors)
        self.name = None


        self.j = 0
        self.text = None

        #it works in case a geometrical locus is selected (.pickFrom) 
        try:
            self.randomPoint()
        except:
            pass


    """
    @property
    def _name(self):
        return self.name

    @_name.setter
    def _name(self, new_name):
        if new_name != self.name:
            self.label()
        self.name = new_name

    #def _on_name_change(self, new_name):
    #    self.label()
    """


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


        self.j+=1
    
    #it works in case a geometrical locus is selected (.pickFrom)
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
    
    #a = globals().keys(), b = list(a)
