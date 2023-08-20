import matplotlib.pyplot as plt
import numpy as np

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'lines.linewidth' ] = 2
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 9

class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_xlim(self.xmin, self.xmax)
    def __init__(self, xmin = -10, xmax = 10, steps = 500, linewidth = 2):
        self.xmin = xmin
        self.xmax = xmax
        self.steps = steps

        self.linewidth = linewidth
        plt.rcParams [ 'lines.linewidth' ] = self.linewidth

        x = [t/abs(self.steps) for t in range(self.xmin*self.steps, self.xmax*self.steps + 1, 1)]
        self.x = np.array(x)

    def grid(self, sizeMinor = 0.2, sizeMajor = 1, N = 1):

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

        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_xticks(Xmajor_ticks)
        self.ax.set_xticks(Xminor_ticks, minor=True)
    
        self.ax.set_ylim(self.xmin, self.xmax)
        self.ax.set_yticks(Ymajor_ticks)
        self.ax.set_yticks(Yminor_ticks, minor=True)

        # And a corresponding grid
        #self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.5)
