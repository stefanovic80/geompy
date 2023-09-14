# _plotSett.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'lines.linewidth' ] = 2
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 9

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

        plt.rcParams [ 'lines.linewidth' ] = self.linewidth

        #x = [t/abs(self.steps) for t in range(self.xmin*self.steps, self.xmax*self.steps + 1, 1)]
        #self.x = np.array(x)
        step = (self.xmax - self.xmin)/self.steps
        self.x = np.arange(self.xmin, self.xmax + step, step)

    def grid(self, sizeMinor = 0.2, sizeMajor = 1, N = 1):#roteate x numbers to make them better fit in

        #gridSteps = int(self.steps / 10)
        #GridSteps = int(self.steps / 100)
        gridSteps = (self.xmax - self.xmin) / self.steps*N*10
        GridSteps = (self.xmax - self.xmin) / self.steps*N*100

        #Xmajor_ticks = np.linspace(self.xmin, self.xmax, GridSteps)
        Xmajor_ticks = np.arange(self.xmin, self.xmax, GridSteps)
        Ymajor_ticks = Xmajor_ticks

        #Xminor_ticks = np.linspace(self.xmin, self.xmax, gridSteps)

        Xminor_ticks = np.arange(self.xmin, self.xmax, gridSteps)

        Yminor_ticks = Xminor_ticks

        #Ymajor_ticks = np.linspace(self.xmin, self.xmax, GridSteps)
        #Yminor_ticks = np.linspace(self.xmin, self.xmax, gridSteps)
        
        try:
            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')
        except:
            pass

        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_xticks(Xmajor_ticks)
        self.ax.set_xticks(Xminor_ticks, minor=True)
    
        self.ax.set_ylim(self.xmin, self.xmax)
        self.ax.set_yticks(Ymajor_ticks)
        self.ax.set_yticks(Yminor_ticks, minor=True)

        # And a corresponding grid
        #self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.2)
        # alpha stands for transparency: 0 transparent, 1 opaque
        self.ax.axvline(0, color = 'k', linewidth = self.linewidth)
        #linewidth = self.linewidth
        self.ax.axhline(0, color = 'k', linewidth = self.linewidth)
        
    #to be deprecated
    #def remove(self):
    #    try:
    #        for line in self.lines:
    #            line.remove()
    #    except:
    #        pass	


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
            f"\033[93m.grid(N = 1)\033[0m\n"
        )
