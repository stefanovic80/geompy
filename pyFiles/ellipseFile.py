# circumference.py
from . import plt, np, random

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class ellipse(plotSett):
#class circumference(point):

    def __init__(self, xmin= -20, xmax = 20, steps = 500, linewidth = 2):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.center = point()
        self.focus1 = random.uniform(0, (self.xmax-self.xmin)/4)
        self.focus2 = random.uniform(0, (self.xmax-self.xmin)/4)
        #self.center = point(xmin = self.xmin + self.radius, xmax = self.xmax -self.radius)
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        self.center.color = self.color

    def draw(self):
        self.remove()

        ellip = self.focus2*np.sqrt( 1 - ( ( self.x - self.center.coords[0]  )/( self.focus1  )  )**2  )#ellipse equation      

        #it removes not a number terms due to root of negative values
        #idx1 = np.argmax(~np.isnan(circ))
        #idx2 = len(circ) - np.argmax(np.flip(~np.isnan(circ)))
        #x values for the graph upper side
        #self.data = [self.x[idx1:idx2]]
        #circ = circ[idx1:idx2]
        
        #y values as second column of self.data matrix
        self.data = [self.x]
        self.data = self.data + [ np.append( self.center.coords[1] + ellip, self.center.coords[1] - ellip[::-1] ) ]

        #x values for the graph of the lower side
        self.data[0] = np.append( self.data[0], self.data[0][::-1])

        self.data[0] = np.append( self.data[0], self.data[0][0] )
        self.data[1] = np.append( self.data[1], self.data[1][0] )

        line1, = self.ax.plot(self.data[0], self.data[1], color = self.color, label = self.name, linewidth = self.linewidth)


        self.ax.legend()
        
        self.lines = []
        self.lines.append(line1)

        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.xmin, self.xmax)
    
    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93mradius:\033[0m {self.radius}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93mcenter\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
