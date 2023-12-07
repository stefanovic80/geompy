# _plotSett.py
from . import plt, np, random
from .Settings import settings

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 10
plt.rcParams [ 'font.weight'] = 'bold'


class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()
    
    def __init__(self):

        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'm', 'magenta', 'k', 'black', settings.azure]
        self._linewidth = settings.linewidth
        self.plotSettings = None

        self.data = [None, None]
        self.tex = [None, None]  # label text
        #density of grid
        
        self.hline = None
        self.vline = None

        plt.rcParams [ 'lines.linewidth' ] = self._linewidth
        
        self.lims()

        self.rotate = False
        self._name = None
        self._points = []

        self._majorStep = None

    @property
    def left(self):
        return settings.xmin

    @left.setter
    def left(self, value):
        settings.xmin = value
        self.majorStep = self._majorStep
        self.lims()
        self.draw()

    @property
    def right(self):
        return settings.xmax

    @right.setter
    def right(self, value):
        settings.xmax = value
        self.majorStep = self._majorStep
        self.minorSteps = 10
        self.lims()
        self.draw()



    @property
    def color(self):
        return self._color
        #if self.j %2 == 0:
        #    self.j += 1
        #    self.color = self._color[self.j]

    @color.setter
    def color(self, c):
        if c in self.colors:
            self._color = c
            self.draw()
            self.label(self._name)
        elif c == "azure":
            self.color = settings.azure
        else:
            pass



    @property
    def x(self):
        return self.data[0]

    """ 
    @x.setter
    def x(self, value):
        self.data[0] = np.array( [ value ] )
        self.lims()
        #self.draw()
        #self.label(self._name)
    """

    @property
    def y(self):
        return self.data[1]

    """
    @y.setter
    def y(self, value):
        self.data[1] = np.array( [ value ] )
        self.lims()
        #self.draw()
        #self.label(self._name)
    """


    """
    #@property
    def nameX(self):
        for name, obj in globals().items():
            if obj is self:
                self._name = name
                break
                #self.label(name )
                #return name
    """
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        self.draw()
        self.label( n )
    
    @property
    def linewidth(self):
        return self._linewidth

    @linewidth.setter
    def linewidth(self, n):
        self._linewidth = n
        self.draw()


    @property
    def majorStep(self):
        return self.majorStep

    @majorStep.setter
    def majorStep(self, value):
        self._majorStep = value
        self.grid(majorStep = self._majorStep)

    @property
    def minorSteps(self):
            return self._minorSteps

    @minorSteps.setter
    def minorSteps(self, value):
        self._minorSteps = value
        self.grid(majorStep = self._majorStep, minorSteps = value)

    @property
    def points(self):
        j = 0
        for u in zip(self.data[0], self.data[1]):
            print(str(j) + ' ' + str(u))
            j+=1

    @points.setter
    def points(self, value):
        #self.erase()
        self._points = self._points + [ value ]
        try:
            self.draw()
        except:
            pass

    def label(self, name):
        try:
            self.tex.remove()
        except:
            pass

        if isinstance(name, str):
            self._name = name

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]

        random_index = np.random.randint(len(data[0]))
        shift = (settings.xmax - settings.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        
        #labelx, labely may necessitte to be attributes
        self.tex = self.ax.text(labelx, labely, self._name, fontsize = 12, color = self._color, ha="center", va="center")



    def draw(self):

        self.lims()

        self.chooseCalc()
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        
        #to check!
        self.lines = []
        self.lines.append(line)

       
    def condition_mask(self):

        condition_mask0 = ( self.data[0] > settings.xmin) & (self.data[0] < settings.xmax)
        condition_mask1 = ( self.data[1] > settings.xmin) & (self.data[1] < settings.xmax)
        condition_mask = condition_mask0 & condition_mask1
        return np.where(condition_mask)
        


    def lims(self):
        self._x = np.linspace(settings.xmin, settings.xmax, settings.steps)
        self.ax.set_xlim(settings.xmin, settings.xmax)
        self.ax.set_ylim(settings.xmin, settings.xmax)

    def grid(self, majorStep = None, minorSteps = 10):

        #grid density 
        #self.N = self.N - 0.1*N
        
        #raw grid step
        #gridSteps = round(gridSteps, 2)
        if majorStep == None:
            majorStep = 2
        else:
            pass
        #fine grid step
        minorStep = majorStep/minorSteps
        #GridSteps = round(GridSteps, 1)
        
        #x grid---------------------------------------
        if (settings.xmin < 0) and (settings.xmax > 0):
            #------------ minor ticks
            Xminor_ticksPos = np.arange(0, settings.xmax, minorStep)
            Xminor_ticksNeg = np.arange(0, settings.xmin, -minorStep)[::-1]

            Xminor_ticks = np.append(Xminor_ticksNeg, Xminor_ticksPos)
            
            #----------- major ticks
            Xmajor_ticksPos = np.arange(0, settings.xmax, majorStep)

            Xmajor_ticksNeg = np.arange(0, settings.xmin, -majorStep)[::-1]

            Xmajor_ticks = np.append(Xmajor_ticksNeg, Xmajor_ticksPos)

            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')


        else:
            Xminor_ticks = np.arange(settings.xmin, settings.xmax, minorStep)
        
            Xmajor_ticks = np.arange(settings.xmin, settings.xmax, majorStep)

        #self.ax.set_xlim(settings.xmin, self.xmax)

        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.vline = self.ax.axvline(0, color = 'k', linewidth = self._linewidth)

        #y grid---------------------------------------
        Ymajor_ticks = Xmajor_ticks
        Yminor_ticks = Xminor_ticks
        
        #self.ax.set_ylim(self.xmin, self.xmax)
        self.ax.set_yticks(Yminor_ticks, minor=True)
        self.ax.set_yticks(Ymajor_ticks)
        
        #self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.6)
        #self.ax.grid(switch)

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.hline = self.ax.axhline(0, color = 'k', linewidth = self._linewidth)    

    def gridOff(self):
        plt.minorticks_off()
        self.ax.grid(False)
    
        # Hide the x and y axes along with their tick values
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['left'].set_color('none')

        # Hide the x and y tick values
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Hide the x and y labels
        self.ax.set_xlabel('')
        self.ax.set_ylabel('')
        
        self.hline.set_visible(False)
        self.vline.set_visible(False)
        self.ax.figure.canvas.draw()


    def __del__(self):
        try:#removes all lines
            for line in self.lines:
                line.remove()
        except:
            pass

        try:#removes all points of the geometrical locus
            for u in self.point:
                u.remove()
        except:
            pass

        try:#removes point texts
            self.tex.remove()
        except:
            pass

        #self.lims()
        

    def __str__(self):
        self.plotSettings = (
            f"\nSettings:\n"
            f"\033[93m.xmin = \033[0m {settings.xmin}\n"
            f"\033[93m.xmax = \033[0m {settings.xmax}\n"
            f"\033[93m.steps = \033[0m {settings.steps}\n"
            f"\033[93m._x = \033[0m {self._x[:10]}...\n"
        )
