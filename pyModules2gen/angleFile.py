from pyFiles.segmentFile import segment
from pyFiles.pointFile import point
from pyFiles._plotSettFile import plotSett
from pyFiles.circumferenceFile import circumference

from pyFiles import xmin, xmax, steps, linewidth, seed

from . import plt, np, random

class angle(plotSett):
    def __init__(self, xmin = xmin, xmax = xmax, steps = steps, seed = seed):
        super().__init__(xmin, xmax, steps)
        
        self.segment = [segment(), segment()]
        self.arc = circumference()
        
        self.rotate = False
        self.color = random.choice(self.colors)
        self.name = None
        self.data = None

        self.j = 0

    def calc(self):
        self.__del__()


        m = [None, None]
        q = [None, None]
        
        #for segment in self.segment:
        self.segment[0].color = self.color
        self.segment[0].calc2()
        
        self.segment[1].color = self.color
        self.segment[1].erase()
        self.segment[1].point[0] = self.segment[0].point[0]
        self.segment[1].intercept = np.random.uniform(self.xmin, self.xmax)
        self.segment[1].calc4()
        
        m[0] = self.segment[0].angCoeff
        q[0] = self.segment[0].intercept
        
        m[1] = self.segment[1].angCoeff
        q[1] = self.segment[1].intercept


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        self.arc.center = point( x, y  )
        
        radius = (self.xmax - self.xmin)/20
        self.arc.radius = radius
        
        self.arc.color = self.color

        arcSize = np.arctan( m[1] ) - np.arctan( m[0] )
        self.arc.calc(angle = arcSize)
        
        self.arc.center.rotation( locus = self.arc, angle = np.arctan( m[0] ) )

        self.data = self.arc.data
        
        self.size = None

    def calc2(self):
        #for segment in self.segment:
        #    segment.chooseCalc()
        m = [None, None]
        q = [None, None]

        m[0] = self.segment[0].angCoeff
        q[0] = self.segment[0].intercept

        m[1] = self.segment[1].angCoeff
        q[1] = self.segment[1].intercept
        
        #------------- from chatGPT
        # Get the indices that would sort 'm'
        sorted_indices = np.argsort(m)
        
        # Sort 'm' and 'q' based on the sorted indices
        m = [m[i] for i in sorted_indices]
        q = [q[i] for i in sorted_indices]
        #------------- from chatGPT


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        
        self.arc.center = point( x, y  )

        radius = (self.xmax - self.xmin)/20
        self.arc.radius = radius

        self.arc.color = self.color

        self.size = abs( self.j%2*np.pi - np.arctan( m[1] ) + np.arctan( m[0] )  )
        self.arc.calc(angle = self.size)
        #to be modified!

        
        #self.arc.center.rotation( locus = self.arc, angle = (self.j%2)*np.arctan( m[1] ) + ((self.j+1)%2)*np.arctan( m[0])  )# + np.arctan( m[0] )  )
        
        formula = (self.j + 1)%2*np.arctan(m[0]) + self.j%2*np.arctan(m[1]) +int(self.j/2)*np.pi
        self.arc.center.rotation( locus = self.arc, angle = formula)


        self.data = self.arc.data

        self.j+=1


    def chooseCalc(self):
        self.__del__()

        calculation_functions = [self.calc2]
        
        #for segment in self.segment:
        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()
                    break
                except:
                    pass



    def draw(self, name = None):
        #self.__del__()
        self.name = name
        #if self.rotate == False:
        #    self.calc()

        self.chooseCalc()

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color)
        
        #self.segment[0].draw()
        #self.segment[1].draw()
        #self.segment[0].point[0].color = 'r'
        #self.segment[0].point[0].draw()

        self.lines = []
        self.lines.append(line)

        
    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.segment = [None, None]
        #self.arc.erase()
        #self.center = None
