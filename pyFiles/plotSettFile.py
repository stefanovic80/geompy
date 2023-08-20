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
    def __init__(self, xmin = -10, xmax = 10, step = 500, linewidth = 2):
        self.xmin = xmin
        self.xmax = xmax
        self.step = step

        self.linewidth = linewidth
        plt.rcParams [ 'lines.linewidth' ] = self.linewidth

        x = [t/abs(self.step) for t in range(self.xmin*self.step, self.xmax*self.step + 1, 1)]
        self.x = np.array(x)

