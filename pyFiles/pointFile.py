#pointFile.py
from . import plt, np, random#, ctypes

plt.ion()

from ._plotSettFile import plotSett
from . import xmin, xmax, steps, linewidth
from . import seed


class point(plotSett):
    def __init__(self, pickFrom = None, x = None, y = None, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth, seed = seed):
        super().__init__( xmin, xmax, steps, linewidth)
        
        self.seed = seed
        
        self.coords = [None, None]

        #return True if var is a  number
        pf_isnumber = isinstance(pickFrom, (int, float) )

        #check if x and y are numbers
        xy_arenumber =  ( isinstance(x, (int, float) ) ) and ( isinstance(y, (int, float) ) )

        #shift of variables:pickFrom become x, x become y
        if pf_isnumber == True:
            self.coords[0] = pickFrom
            self.coords[1] = x

        #no arguments return random coords
        elif pickFrom is None and x is None and y is None:
            self.randomCoords(self.seed)

        #chooce point coords from a geometrical locus
        elif pf_isnumber == False and xy_arenumber == False:
            self.pickFrom = pickFrom.data
            self.randomPoint()
        
        elif xy_arenumber == True:
            self.coords[0] = x
            self.coords[1] = y
            
        """
        @property
        def y(self):
            return self._coords[1]

        @y.setter
        def y(self, value):
            self._coords[1] = value
        """

        self.color = random.choice(self.colors)
        self.j = 0 #for drawing
        self.k = 0 #for clicking

        self.lines = None
        self.tex = None
        self.name = None
        
    def draw(self, name = None):
        self.__del__()

        line = self.ax.scatter( self.coords[0], self.coords[1], color = self.color, linewidth = self.linewidth)
        self.lines = []
        self.lines.append(line)



        if self.j%2 != 0: 
            """
            xvals = [ 0, self.coords[0] ]
            xvals.sort()
            yvals = [ 0, self.coords[1] ]
            yvals.sort()
            """

            hline = self.ax.axhline(y = self.coords[1], linestyle = '--', color = 'k', linewidth = 1)#, xmin = xvals[0], xmax = xvals[1] )

            vline = self.ax.axvline(x = self.coords[0], linestyle = '--', color = 'k', linewidth = 1)#, ymin = yvals[0], ymax = yvals[1] )
            self.lines.append(hline)
            self.lines.append(vline)
            print("\nrun .draw one more time to erase coordinates\n")

        self.label(name)
        self.j += 1 
        # used by .draw() method to make it working in 1 maner fist and in another once it's called again


    def label(self, name):
        try:
            self.tex.remove()
        except:
            pass

        if isinstance(name, str):
            self.name = name

        shift = (self.xmax - self.xmin)/40
        self.tex = self.ax.text(self.coords[0] + shift, self.coords[1] + shift, self.name, fontsize = 12, color = self.color, ha="center", va="center")
        

    #-----------------------------------------------
    def randomCoords(self, seed):
        self.coords[0] = random.uniform(self.xmin, self.xmax)
        self.coords[1] = random.uniform(self.xmin, self.xmax)
        self.seed += 1
        seed = self.seed

    
    #random Point from a geometrical locus
    def randomPoint(self):
        condition_mask = ( self.pickFrom[1] > self.xmin) & (self.pickFrom[1] < self.xmax)
        indices = np.where(condition_mask)
        idx = random.choice(indices[0])
        self.coords = [self.pickFrom[0][idx], self.pickFrom[1][idx] ]
    #-------------------------------------------------------------

    def click(self, name = None):
        self.__del__()
         
                
        if self.k%2 != 0: 
            b = plt.ginput()
            self.coords = [ b[0][0], b[0][1] ]
            self.draw(name)
            
            self.ax.set_xlim( self.xmin, self.xmax  )
            self.ax.set_ylim( self.xmin, self.xmax  )
        else: 
            a = plt.ginput()
            
            deltaZoom = (self.xmax - self.xmin)/10
            
            self.ax.set_xlim( a[0][0] - deltaZoom, a[0][0] + deltaZoom)
            self.ax.set_ylim( a[0][1] - deltaZoom, a[0][1] + deltaZoom)
            print("\nrun .click('label') one more time to select point coordinates\n")
        self.k += 1

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

    def __del__(self):
        super().__del__()
        try:
            self.tex.remove()
        except:
            pass
