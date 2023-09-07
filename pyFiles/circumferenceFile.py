# circumference.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class circumference(plotSett):
#class circumference(point):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2)
        self.center = point()
        #self.center = point(xmin = self.xmin + self.radius, xmax = self.xmax -self.radius)
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        self.center.color = self.color

    def draw(self):
        #self.remove()
        self.__del__()
        
        circ = np.sqrt( self.radius**2 - (self.x- self.center.coords[0])**2)#circumference equation      

        #it removes not a number terms due to root of negative values
        idx1 = np.argmax(~np.isnan(circ))
        idx2 = len(circ) - np.argmax(np.flip(~np.isnan(circ)))
        #x values for the graph upper side
        self.data = [self.x[idx1:idx2]]
        circ = circ[idx1:idx2]
        
        #y values as second column of self.data matrix
        self.data = self.data + [ np.append( self.center.coords[1] + circ, self.center.coords[1] - circ[::-1] ) ]

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



    def erase(self):#add self.remove()
        self.__del__()

        self.data = [None, None]
        self.center.coords = [None, None]
        self.radius = None
        #print(self.__str__() )


    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93m.radius = \033[0m {self.radius}\n"
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            f"\033[93m.color = \033[0m {self.color}\n"
            f"\033[93m.linewidth = \033[0m\n"
            f"\033[93m.name = \033[0m {self.name}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93m.center\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
