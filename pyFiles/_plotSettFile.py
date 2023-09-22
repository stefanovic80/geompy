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
        
        #max( abs(self.min), abs(self.max) )

        #grid density 
        self.N = self.N - 0.1*N
        #fine grid step
        minorStep = (self.xmax - self.xmin) / self.steps*self.N*10
        #raw grid step
        #gridSteps = round(gridSteps, 2)
        majorStep = (self.xmax - self.xmin) / self.steps*self.N*100
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

        self.ax.set_xlim(self.xmin, self.xmax)

        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.ax.axvline(0, color = 'k', linewidth = self.linewidth)

        #y grid---------------------------------------
        Ymajor_ticks = Xmajor_ticks
        Yminor_ticks = Xminor_ticks
        
        self.ax.set_ylim(self.xmin, self.xmax)
        self.ax.set_yticks(Yminor_ticks, minor=True)
        self.ax.set_yticks(Ymajor_ticks)
        
        #self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.6)
        #self.ax.grid(switch)

        # alpha stands for transparency: 0 transparent, 1 opaque
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
