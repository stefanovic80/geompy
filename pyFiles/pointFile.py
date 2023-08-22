# pointFile.py
from . import plt, np, random
#matplotlib.plot has to be imported in all pyFiles modules

plt.ion()

from ._plotSettFile import plotSett



class point(plotSett):
    
    def __init__(self, xmin = -20, xmax = 20, steps = 500, linewidth = 2):
        super().__init__( xmin, xmax, steps, linewidth )
        a = plt.ginput()
        self.coords = [ a[0][0], a[0][1] ]
        self.line = None

        colors = ['b', 'blue', 'g', 'green', 'r', 'red',\
                'c', 'cyan', 'm', 'magenta', 'k', 'black']
        self.color = random.choice(colors)

    def draw(self):
        self.line = self.ax.scatter( self.coords[0], self.coords[1], color = self.color, linewidth = self.linewidth)
