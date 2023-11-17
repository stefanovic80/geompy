#pointFile.py

#global xmin, xmax

from . import plt, np, random#, ctypes

plt.ion()

from ._plotSettFile import plotSett
#from . import xmin, xmax, steps, linewidth
from . import steps, linewidth
from . import seed
from .config import xmin, xmax


class point(plotSett):
    def __init__(self, pickFrom = None, x = None, y = None, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth, seed = seed, draw = True):
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
        #------------------------------------------------------------
        # Get local variables as a dictionary
        local_vars = locals()

        # Convert the dictionary values to a list
        args_list = list(local_vars.values())
        #------------------------------------------------------------
        """


        self._color = random.choice(self.colors)
        self.lines = None
        self.tex = None 

        if draw == True:
            self.draw()
            #self.label(name = None)

    
    @property
    def x(self):
        return self.coords[0]

    @x.setter
    def x(self, value):
        self.coords[0] = value
        self.lims()
        self.draw()
        self.label(self._name)

    @property
    def y(self):
        return self.coords[1]

    @y.setter
    def y(self, value):
        self.coords[1] = value
        self.lims()
        self.draw()
        self.label(self._name)

    #coords as a list of two numpy arrays of one element each
    def calc(self):
        self.data = [ None, None  ]
        for j in range(2):
            self.data[j] = np.array([ self.coords[j] ] )

    #it overwrites the .draw method in _plotSett
    def draw(self):
        self.__del__()
        self.lims()
        if self.rotate == False:
            self.calc()

        line = self.ax.scatter( self.coords[0], self.coords[1], color = self._color, linewidth = self.linewidth)
        self.lines = []
        self.lines.append(line)
    
    
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
    def zoom(self):

        a = plt.ginput()
        
        m = self.xmin
        M = self.xmax

        deltaZoom = (M - m)/10

        self.ax.set_xlim( a[0][0] - deltaZoom, a[0][0] + deltaZoom)
        self.ax.set_ylim( a[0][1] - deltaZoom, a[0][1] + deltaZoom)


    def click(self):
        self.__del__()
          
        b = plt.ginput()
        self.coords = [ b[0][0], b[0][1] ]
        self.draw()
        self.label(self._name)
            
        self.lims()
    
    
    def rotation(self, locus = None, angle = 0):
        locus.rotate = True
        a1 = (locus.data[0] - self.coords[0])*np.sin(angle)
        locus.data[0] = (locus.data[0] - self.coords[0]  )*np.cos(angle) - (locus.data[1] - self.coords[1]  )*np.sin(angle) + self.coords[0]

        locus.data[1] = a1 + ( locus.data[1] - self.coords[1])*np.cos(angle) + self.coords[1]
        
        locus.draw()#, draw = False)
    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m point\n"
            f"\nAttributes:\n"
            f"\033[93mcoords:\033[0m [{self.coords[0]}, {self.coords[1]}] \n"
            f"\033[93mname:\033[0m {self._name}\n"
            f"\033[93mcolor:\033[0m {self._color}\n"
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
