import matplotlib.pyplot as plt
import numpy as np

plt.ion()

from .plotSettFile import plotSett

#names = globals().keys()

class segment(plotSett):
    def __init__(self, xmax = 10, xmin = -10):

        super().__init__()
        self.angCoeff = np.random.randint(xmin, xmax)
        self.intercept = np.random.randint(xmin, xmax)
        self.xmin = xmin
        self.xmax = xmax
        self.idxMin = None
        self.idxMax = None
        self.segment = None
        self.data = None
        self.name = globals().keys()

    def remove(self):
        try:
            self.segment.remove()
        except:
            pass

    def plot(self, color = 'b', name = 'label'):
        
        self.remove()
        
        idxMin = np.where( self.x >= self.xmin)[0][0]
        idxMax = np.where( self.x >= self.xmax)[0][0]
        x = self.x[idxMin: idxMax] # a local copy of x values
        self.data = self.angCoeff*x + self.intercept
        self.segment, = self.ax.plot(x, self.data, linewidth=2, color = color, label = name)
        self.ax.legend()
