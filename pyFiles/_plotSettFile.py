# _plotSett.py
from . import plt, np, random
from .Settings import settings

# to be removed in case of coding
plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 10
plt.rcParams [ 'font.weight'] = 'bold'



#plt.gca().lines[-1].remove()

class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()
    
    def __init__(self):

        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'm', 'magenta', 'k', 'black', settings.azure]
        self._linewidth = settings.linewidth
        self.plotSettings = None

        self.data = [None, None]
        #self.tex = [None, None]  # label text
        #density of grid
        
        self.hline = None
        self.vline = None

        plt.rcParams [ 'lines.linewidth' ] = self._linewidth

        self.lims()

        self.rotate = False
        self._name = None
        self._points = []

        self._majorStep = 2
        self.j = 0
        
        self.lines = []

    @property
    def left(self):
	    return settings.xmin
		
    @left.setter
    def left(self, value):
        settings.xmin = value
        settings.ymin = value
        self.majorStep = self._majorStep
        self.lims()

    @property
    def right(self):
        return settings.xmax

    @right.setter
    def right(self, value):
        settings.xmax = value
        settings.ymax = value
        self.majorStep = self._majorStep
        self.lims()

    @property
    def bottom(self):
        return settings.ymin

    @bottom.setter
    def bottom(self, value):
        settings.ymin = value
        self.grid( bottomConcat = value, topConcat = settings.ymax )
        self.ax.set_ylim( bottom = value )
        self._y = np.linspace(settings.ymin, settings.ymax, settings.steps)



    @property
    def up(self):
        return settings.ymax

    @up.setter
    def up(self, value):
        settings.ymax = value
        self.grid(topConcat = value, bottomConcat = settings.ymin)
        self.ax.set_ylim( top = value )
        self._y = np.linspace(settings.ymin, settings.ymax, settings.steps)
    

    @property
    def color(self):
        return self._color
        

    @color.setter
    def color(self, c):
        if c in self.colors:
            self._color = c
            self.__del__()
            self.onlyDraw()
            self.label(self._name)
        elif c == "azure":
            self.color = settings.azure
        else:
            pass


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        self.__del__()
        self.onlyDraw()
        self.label(n)
    
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
        self.grid(majorStep = self._majorStep, bottomConcat = settings.ymin, topConcat = settings.ymax )

    @property
    def minorSteps(self):
            return self._minorSteps

    @minorSteps.setter
    def minorSteps(self, value):
        self._minorSteps = value
        self.grid(majorStep = self._majorStep, minorSteps = value, bottomConcat = settings.ymin, topConcat = settings.ymax)



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
        #self.tex = self.ax.text(labelx, labely, self._name, fontsize = 12, color = self._color, ha="center", va="center")
        text = self.ax.text(labelx, labely, self._name, fontsize = 12, color = self._color, ha="center", va="center")
        self.lines.append(text)



    def draw(self):
        self.chooseCalc()
        self.onlyDraw()

    def onlyDraw(self):
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        
        #to check!
        self.lines = []
        self.lines.append(line)

       
    def condition_mask(self):

        condition_mask0 = ( self.data[0] > settings.xmin) & (self.data[0] < settings.xmax)
        condition_mask1 = ( self.data[1] > settings.ymin) & (self.data[1] < settings.ymax)
        condition_mask = condition_mask0 & condition_mask1
        return np.where(condition_mask)
        


    def lims(self):
        self._x = np.linspace(settings.xmin, settings.xmax, settings.steps)
        self._y = np.linspace(settings.ymin, settings.ymax, settings.steps)
        self.ax.set_xlim(settings.xmin, settings.xmax)
        self.ax.set_ylim(settings.ymin, settings.ymax)
        
        
    def grid(self, majorStep = 2, minorSteps = 10, topConcat = settings.xmax, bottomConcat = settings.xmin):
        
        minorStep = majorStep / minorSteps
        
        
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

        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.vline = self.ax.axvline(0, color = 'k', linewidth = self._linewidth)

        #y grid---------------------------------------
        topArrayMinor = np.arange(settings.xmax, topConcat, minorStep)
        
        topArrayMajor = np.arange(settings.xmax, topConcat, majorStep)

        bottomArrayMinor = np.arange( bottomConcat, settings.xmin, minorStep)

        bottomArrayMajor = np.arange( bottomConcat, settings.xmin, majorStep)



        Yminor_ticks = np.concatenate((bottomArrayMinor, Xminor_ticks, topArrayMinor))

        Ymajor_ticks = np.concatenate((bottomArrayMajor, Xmajor_ticks, topArrayMajor))

        
        self.ax.set_yticks(Yminor_ticks, minor=True)
        self.ax.set_yticks(Ymajor_ticks)
        

        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.6)
        

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.hline = self.ax.axhline(0, color = 'k', linewidth = self._linewidth)    
    

    def __del__(self):
        try:#removes all lines
            for line in self.lines:
                line.remove()
        except:
            pass

        try:#removes all geometrical locus points
            for u in self.point:
                u.remove()
        except:
            pass

        #try:#removes point texts
        #    self.tex.remove()
        #except:
        #    pass
        

    def __str__(self):
        self.plotSettings = (
            f"\nSettings:\n"
            f"\033[93m.xmin = \033[0m {settings.xmin}\n"
            f"\033[93m.xmax = \033[0m {settings.xmax}\n"
            f"\033[93m.steps = \033[0m {settings.steps}\n"
            f"\033[93m._x = \033[0m {self._x[:10]}...\n"
        )
