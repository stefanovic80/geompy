# circumference.py
from . import plt, np, random

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point

class circumference(plotSett):
#class circumference(point):

    def __init__(self, xmin= -20, xmax = 20, steps = 500, linewidth = 2):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2)
        self.center = point()
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        self.center.color = self.color

    def draw(self):
        self.remove()

        #np.where(self.radius - self.x ) < 0
	# [ a for a in self.data[0] ]
        circ = np.sqrt( self.radius**2 - (self.x- self.center.coords[0])**2)#circumference equation
        
        #a bug when circumference is going to be moved from the border
        idx1 = np.argmax(~np.isnan(circ))
        idx2 = len(circ) - np.argmax(np.flip(~np.isnan(circ)))
        self.x = self.x[idx1:idx2]
        circ = circ[idx1:idx2]
        
        self.data = [ self.center.coords[1] + circ ] #a one data list with upper side data of circ

        self.data = self.data + [ self.center.coords[1] - circ ] #append one element of list with dw side of circ
        
        #self.data[0] = [a for a in self.data[0] if np.isnan(a) != True]
        #self.data[1] = [a for a in self.data[1] if np.isnan(a) != True]
        #self.x = [a for a in self.x if np.isnan(a) != True]
        
        line1, = self.ax.plot(self.x, self.data[1], color = self.color, label = self.name, linewidth = self.linewidth)

        self.ax.legend()

        line2, = self.ax.plot(self.x, self.data[0], color = self.color, linewidth = self.linewidth)#, markersize=12)
        
        
        line3, = self.ax.plot( [ self.x[-1], self.x[-1] ], [ self.data[0][-1], self.data[1][-1] ], color = self.color, linewidth = self.linewidth)
        
        line4, = self.ax.plot( [ self.x[0], self.x[0] ], [ self.data[0][0], self.data[1][0] ], color = self.color, linewidth = self.linewidth)

        self.lines = []
        self.lines.append(line1)
        self.lines.append(line2)
        
        self.lines.append(line3)
        self.lines.append(line4)

        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.xmin, self.xmax)
    
    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mType:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93mcenter.coords:\033[0m {self.center.coords[0]} {self.center.coords[1]}\n"
            f"\033[93mradius:\033[0m {self.radius}\n"
            f"\033[93mx:\033[0m {self.x}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93mcenter\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
