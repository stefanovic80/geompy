import matplotlib.pyplot as plt
import numpy as np

plt.ion()

from .plotSettFile import plotSett




class segment(plotSett):
    def __init__(self, xmax = 10, xmin = -10):

        super().__init__()
        self.angCoeff = np.random.randint(-20, 20)
        self.intercept = np.random.randint(xmin, xmax)
        self.idxMin = None
        self.idxMax = None
        self.segment = None
        self.data = None

    def remove(self):
        try:
            self.segment.remove()
        except:
            pass

    def plot(self, color = 'b'):
        
        self.remove()
        #try:
        #    self.segment.remove()
        #except:
        #    pass
        
        #idxMin = np.where( obj.x >= xMin)[0][0]
        #idxMax = np.where( obj.x >= xMax)[0][0]
        #x = obj.x[idxMin: idxMax] # a local copy of x values
        self.data = self.angCoeff*self.x + self.intercept
        self.segment, = self.ax.plot(self.x, self.data, linewidth=2, color = color)

