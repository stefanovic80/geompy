# angle.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .segmentFile import segment

class angle(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, seg0 = segment(), seg1 = segment()):
        
        super().__init__(xmin, xmax, steps, linewidth)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2 )

        self.side = [None, None]

        self.side[0] = seg0
        self.side[1] = seg1
        for j in range(2):
            self.side[j].chooseCalc()
        

        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)
        
        #------------------------------------------------------
        #point choosen for labeling
        self.pointLabel = point()
        self.pointLabel.coords = [None, None]
        self.pointLabel.color = 'white'
        #------------------------------------------------------
        self.cross00 = None
        self.cross01 = None
        self.cross10 = None
        self.cross11 = None

        self.xx = None

    #to calculate intersection
    def intersecPoints(self):
        
        q = [None, None]
        m = [None, None]
        for j in range(2):
            q[j] = self.side[j].intercept
            m[j] = self.side[j].angCoeff
        
        xCross = (q[1] - q[0])/(m[0] -m[1])
        yCross = m[0]*xCross + q[0]

        self.center = point(xCross, yCross)
        radius = self.radius
        
        Delta = [None, None]
       
        # points of intersection btw circle and 2 diameters
        x = [ [None, None], [None, None] ]
        y = [ [None, None], [None, None] ]

        #j=0 Delta with line zero, j=1 Delta with line 1
        for j in range(2):
            Delta[j] = xCross**2 - (q[j] - yCross)**2*(2*xCross*m[j] + 1) + radius**2*( 1 + m[j]**2)
            x[j][0] = ( xCross - m[j]*(q[j] - yCross) + np.sqrt( Delta[j]  ) ) / ( 1 + m[j]**2  )
            x[j][1] = ( xCross - m[j]*(q[j] - yCross) - np.sqrt( Delta[j]  ) ) / ( 1 + m[j]**2  )

            y[j][0] = m[j]*x[j][0] + q[j]
            y[j][1] = m[j]*x[j][1] + q[j]
        

        #intersectionPoints
        self.cross00 = point( x[0][0], y[0][0] )
        self.cross01 = point( x[0][1], y[0][1] )
        self.cross10 = point( x[1][0], y[1][0] )
        self.cross11 = point( x[1][1], y[1][1] )
        
        self.xx = np.array( [ x[0][0], x[0][1], x[1][0], x[1][1] ]  )
        self.xx.sort()

    def calc(self, name = None):
        #self.__del__()
        
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
        

    def draw(self, name = None):
        #self.__del__()

        self.intersecPoints()
        self.calc()

        idx = [None, None, None, None]
        for u in range(2):
            idx[u] = np.where( self.data[0] >= self.xx[u] )[0][0]
        
        start = int( len(self.data)/2 + 1 )# +1 to be checked out

        for u in range(2, 4):
            idx[u] = np.where( self.data[start:] >= self.xx[u] )[0][0]


        line1, = self.ax.plot(self.data[0][ idx[0] : idx[1] ], self.data[1][ idx[0] : idx[1] ], color = self.color, label = self.name, linewidth = self.linewidth)
        #self.ax.legend()
        
        #self.lines = []
        #self.lines.append(line1)

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
    
