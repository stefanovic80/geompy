# _plotSett.py
from . import plt, np, random
from . import steps, linewidth
#from . import steps, linewidth

#xmin = [-10]
#xmax = [10]

from .config import xmin, xmax

#global xmin, xmax

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'lines.linewidth' ] = 2
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 10
plt.rcParams [ 'font.weight'] = 'bold'


class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()
    #ax.set_xlim(self.xmin, self.xmax)
    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth):
        self.xmin = xmin#[0]
        self.xmax = xmax#[0]
        self.steps = steps
        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'c', 'cyan', 'm', 'magenta', 'k', 'black']
        self.linewidth = linewidth
        self.plotSettings = None

        self.data = [None, None]
        self.tex = [None, None]  # label text
        #density of grid
        self.N = 1
        
        self.hline = None
        self.vline = None

        plt.rcParams [ 'lines.linewidth' ] = self.linewidth
        
        self.lims()

        self.rotate = False
        self._name = None

    @property
    def left(self):
        return self.xmin

    @left.setter
    def left(self, value):
        self.xmin = value
        majorStep = (self.xmax - self.xmin)/20
        self.grid(majorStep = majorStep)
        self.lims()

    @property
    def right(self):
        return self.xmax

    @right.setter
    def right(self, value):
        self.xmax = value
        majorStep = (self.xmax - self.xmin)/20
        self.grid(majorStep = majorStep)
        self.lims()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        if c in self.colors:
            self._color = c
            self.draw()
            self.label(self._name)
        else:
            pass


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        self.draw()
        self.label( n )




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
        shift = (self.xmax - self.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        
        #labelx, labely may necessitte to be attributes
        self.tex = self.ax.text(labelx, labely, self._name, fontsize = 12, color = self._color, ha="center", va="center")



    def draw(self):#, cut = False):#, angle = 2*np.pi ):

        self.lims()
        #self._cut = cut
        self.chooseCalc()#angle = 2*np.pi)
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self._color)

        self.lines = []
        self.lines.append(line)

       
    def condition_mask(self):

        condition_mask0 = ( self.data[0] > self.xmin) & (self.data[0] < self.xmax)
        condition_mask1 = ( self.data[1] > self.xmin) & (self.data[1] < self.xmax)
        condition_mask = condition_mask0 & condition_mask1
        return np.where(condition_mask)
        


    def lims(self):
        self._x = np.linspace(self.xmin, self.xmax, steps)
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.xmin, self.xmax)


    def grid(self, N = 1, majorStep = None, minorSteps = 10):#roteate x numbers to make them better fit in
        
        #max( abs(self.min), abs(self.max) )

        #grid density 
        self.N = self.N - 0.1*N
        
        #raw grid step
        #gridSteps = round(gridSteps, 2)
        if majorStep == None:
            majorStep = (self.xmax - self.xmin) / self.steps*self.N*100
        else:
            pass
        #fine grid step
        minorStep = majorStep/minorSteps
        #minorStep = (self.xmax - self.xmin) / self.steps*self.N*10
        #GridSteps = round(GridSteps, 1)
        
        #x grid---------------------------------------
        if (self.xmin < 0) and (self.xmax > 0):
            #------------ minor ticks
            Xminor_ticksPos = np.arange(0, self.xmax, minorStep)
            Xminor_ticksNeg = np.arange(0, self.xmin, -minorStep)[::-1]

            Xminor_ticks = np.append(Xminor_ticksNeg, Xminor_ticksPos)
            
            #----------- major ticks
            Xmajor_ticksPos = np.arange(0, self.xmax, majorStep)

            Xmajor_ticksNeg = np.arange(0, self.xmin, -majorStep)[::-1]

            Xmajor_ticks = np.append(Xmajor_ticksNeg, Xmajor_ticksPos)

            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')


        else:
            Xminor_ticks = np.arange(self.xmin, self.xmax, minorStep)
        
            Xmajor_ticks = np.arange(self.xmin, self.xmax, majorStep)

        #self.ax.set_xlim(self.xmin, self.xmax)

        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.vline = self.ax.axvline(0, color = 'k', linewidth = self.linewidth)

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
        self.hline = self.ax.axhline(0, color = 'k', linewidth = self.linewidth)    

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
    

    """
    def gridOff(self):
        plt.minorticks_off()
        self.ax.grid(False)
        
        # Hide the x and y axes and their associated elements
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        
        # Hide the x and y tick values and labels
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xlabel('')
        self.ax.set_ylabel('')
        
        self.hline.set_visible(False)
        self.vline.set_visible(False)
        self.ax.figure.canvas.draw()
    """



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
            f"\033[93m.xmin = \033[0m {self.xmin}\n"
            f"\033[93m.xmax = \033[0m {self.xmax}\n"
            f"\033[93m.steps = \033[0m {self.steps}\n"
            f"\033[93m.x = \033[0m {self._x[:10]}...\n"
            f"\033[93m.grid(N = {self.N})\033[0m\n"
        )
