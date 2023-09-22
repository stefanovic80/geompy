# _plotSett.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'lines.linewidth' ] = 2
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 10
plt.rcParams [ 'font.weight'] = 'bold'

class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_xlim(self.xmin, self.xmax)
    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, linewidth = linewidth):
        self.xmin = xmin
        self.xmax = xmax
        self.steps = steps
        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'c', 'cyan', 'm', 'magenta', 'k', 'black']
        self.linewidth = linewidth
        self.plotSettings = None

        #density of grid
        self.N = 1

        plt.rcParams [ 'lines.linewidth' ] = self.linewidth

        self.x = np.linspace(self.xmin, self.xmax, steps)

    def grid(self, N = 1):#roteate x numbers to make them better fit in
        
        self.N = N
        #gridSteps = int(self.steps / 10)
        #GridSteps = int(self.steps / 100)
        gridSteps = (self.xmax - self.xmin) / self.steps*self.N*100
        #gridSteps = round(gridSteps, 2)
        GridSteps = (self.xmax - self.xmin) / self.steps*self.N*10
        #GridSteps = round(GridSteps, 1)
        #Xmajor_ticks = np.linspace(self.xmin, self.xmax, GridSteps)
        Xmajor_ticks = np.arange(self.xmin, self.xmax, GridSteps)
        Ymajor_ticks = Xmajor_ticks

        #Xminor_ticks = np.linspace(self.xmin, self.xmax, gridSteps)

        Xminor_ticks = np.arange(self.xmin, self.xmax, gridSteps)
        Xmajor_ticks = np.arange(self.xmin, self.xmax, GridSteps)

        Yminor_ticks = Xminor_ticks

        #Ymajor_ticks = np.linspace(self.xmin, self.xmax, GridSteps)
        #Yminor_ticks = np.linspace(self.xmin, self.xmax, gridSteps)
        
        try:
            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')
        except:
            pass

        self.ax.set_xlim(self.xmin, self.xmax)
        #self.ax.set_xticks(Xmajor_ticks)
        #this is not number labelling
        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        self.ax.set_ylim(self.xmin, self.xmax)
        #self.ax.set_yticks(Ymajor_ticks)
        self.ax.set_yticks(Yminor_ticks, minor=True)

        # And a corresponding grid
        #self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.2)
        # alpha stands for transparency: 0 transparent, 1 opaque
        self.ax.axvline(0, color = 'k', linewidth = self.linewidth)
        #linewidth = self.linewidth
        self.ax.axhline(0, color = 'k', linewidth = self.linewidth)
        

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

        try:#removes point texts (.remove() doesn't work!)
            self.pointLabel.remove()
        except:
            pass

    def __str__(self):
        self.plotSettings = (
            f"\nSettings:\n"
            f"\033[93m.xmin = \033[0m {self.xmin}\n"
            f"\033[93m.xmax = \033[0m {self.xmax}\n"
            f"\033[93m.steps = \033[0m {self.steps}\n"
            f"\033[93m.x = \033[0m {self.x[:10]}...\n"
            f"\033[93m.grid(N = {self.N})\033[0m\n"
        )
