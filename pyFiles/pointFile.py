#pointFile.py

from . import plt, np, random
from ._plotSettFile import plotSett
from . import seed
from .Settings import settings


class point(plotSett):
    def __init__(self, pickFrom = None, x = None, y = None, seed = seed, draw = True):
        super().__init__()
        

        self.seed = seed
        self.data = [None, None]

        #return True if var is a  number
        pf_isnumber = isinstance(pickFrom, (int, float) )

        
        #check if x and y are numbers
        xy_arenumber =  ( isinstance(x, (int, float) ) ) and ( isinstance(y, (int, float) ) )

        #shift of variables:pickFrom become x, x become y
        if pf_isnumber == True:
            self.data[0] = pickFrom
            self.data[1] = x

        #no arguments return random coords
        elif pickFrom is None and x is None and y is None:
            self.randomCoords(self.seed)

        #chooce point coords from a geometrical locus
        elif pf_isnumber == False and xy_arenumber == False:
            self.pickFrom = pickFrom.data
            self.randomPoint()
        
        elif xy_arenumber == True:
            self.data[0] = x
            self.data[1] = y 
        
        """
        #------------------------------------------------------------
        # Get local variables as a dictionary
        local_vars = locals()

        # Convert the dictionary values to a list
        args_list = list(local_vars.values())
        #------------------------------------------------------------
        """

        self.j = 0
        self._color = random.choice(self.colors)
        self.lines = None
        self.tex = None 
        
        self.coords = self.data
        self.data = [ np.array([u]) for u in self.data  ]
        
        if draw == True:
            self.draw()

    @property
    def x(self):
        return self.data[0]


    @x.setter
    def x(self, value):
        self.data[0] = np.array( [ value ] )
        self.lims()
        self.draw()
        self.label(self._name)


    @property
    def y(self):
        return self.data[1]


    @y.setter
    def y(self, value):
        self.data[1] = np.array( [ value ] )
        self.lims()
        self.draw()
        self.label(self._name)


    @property
    def equation(self):
        
        try:
            self.tex.remove()
        except:
            pass

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]
        random_index = np.random.randint(len(data[0]))
        shift = (settings.xmax - settings.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        #--------------------

        
        x = str(round(self.data[0], 2))
        y = str(round(self.data[1], 2))
        eq = "(" + x + ";" + y + ")"
        try:
            eq = self._name + eq
        except:
            pass
        
        if self.j%2 == 0:
            self.tex = self.ax.text(labelx, labely, eq, fontsize = 12, color = self._color, ha="center", va="center")
        self.j += 1



    #coords as a list of two numpy arrays of one element each
    def calc(self):
        pass
        #self.data = [ np.array([u]) for u in self.data  ]

    #it overwrites the .draw method in _plotSett
    def draw(self):
        self.__del__()
        self.lims()
        if self.rotate == False:
            self.calc()

        line = self.ax.scatter( self.data[0], self.data[1], color = self._color, linewidth = self._linewidth)
        self.lines = []
        self.lines.append(line)
    
    
    #-----------------------------------------------
    def randomCoords(self, seed):
        self.data[0] = random.uniform(settings.xmin, settings.xmax)
        self.data[1] = random.uniform(settings.xmin, settings.xmax)
        self.seed += 1
        seed = self.seed

    
    #random Point from a geometrical locus
    def randomPoint(self):
        condition_mask = ( self.pickFrom[1] > settings.xmin) & (self.pickFrom[1] < settings.xmax)
        indices = np.where(condition_mask)
        idx = random.choice(indices[0])
        self.data = [self.pickFrom[0][idx], self.pickFrom[1][idx] ]
    #-------------------------------------------------------------
    def zoom(self):

        a = plt.ginput()
        
        m = settings.xmin
        M = settings.xmax

        deltaZoom = (M - m)/10

        self.ax.set_xlim( a[0][0] - deltaZoom, a[0][0] + deltaZoom)
        self.ax.set_ylim( a[0][1] - deltaZoom, a[0][1] + deltaZoom)


    def click(self):
        self.__del__()
          
        b = plt.ginput()
        self.data = [ b[0][0], b[0][1] ]
        self.draw()
        self.label(self._name)
            
        self.lims()
    
    
    def rotation(self, locus = None, angle = 0):
        locus.rotate = True
        a1 = (locus.data[0] - self.data[0])*np.sin(angle)
        locus.data[0] = (locus.data[0] - self.data[0]  )*np.cos(angle) - (locus.data[1] - self.data[1]  )*np.sin(angle) + self.data[0]

        locus.data[1] = a1 + ( locus.data[1] - self.data[1])*np.cos(angle) + self.data[1]
        
        locus.draw()#, draw = False)
    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m point\n"
            f"\nAttributes:\n"
            f"\033[93mcoords:\033[0m [{self.data[0]}, {self.data[1]}] \n"
            f"\033[93mname:\033[0m {self._name}\n"
            f"\033[93mcolor:\033[0m {self._color}\n"
        )

        methods = (
            f"\nMethods:\n"
            f"\033[93mclick()\033[0m\n"
            f"\033[93mrotation(locus, angle = radiants)\033[0m\n"
            f"\033[93merase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings

    def __del__(self):
        super().__del__()
        try:
            self.tex.remove()
        except:
            pass
