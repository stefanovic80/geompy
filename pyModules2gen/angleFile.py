from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett
from ..pyFiles.circumferenceFile import circumference

from ..pyFiles import seed

from ..pyFiles.Settings import settings

from ..pyFiles import plt, np, random

class angle(plotSett):
    def __init__(self, line0 = line(draw = False) , line1 = line(draw = False), seed = seed, draw = True):
        super().__init__()
        
        self.line = [line0, line1]
        self.arc = circumference(draw = False)
        
        self.rotate = False
        self._color = random.choice(self.colors)
        self._name = None
        self.data = None

        self.j = 0
        
        if draw == True:
            self.name = r"$\alpha$"

    def calc(self):
        self.__del__()


        m = [None, None]
        q = [None, None]
        
        #for line in self.line:
        self.line[0]._color = self._color
        self.line[0].calc2()
        
        self.line[1]._color = self._color
        self.line[1].erase()
        self.line[1].point[0] = self.line[0].point[0]
        self.line[1].intercept = np.random.uniform(settings.xmin, settings.xmax)
        self.line[1].calc4()
        
        m[0] = self.line[0].angCoeff
        q[0] = self.line[0].intercept
        
        m[1] = self.line[1].angCoeff
        q[1] = self.line[1].intercept


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        self.arc.center = point( x, y, draw = False  )
        
        radius = (settings.xmax - settings.xmin)/20
        self.arc._radius = radius
        
        self.arc._color = self._color

        arcSize = np.arctan( m[1] ) - np.arctan( m[0] )
        self.arc.calc(angle = arcSize)
        
        self.arc.center.rotation( locus = self.arc, angle = np.arctan( m[0] ) )

        self.data = self.arc.data
        
        self.size = None

    def calc2(self):
        #for line in self.line:
        #    line.chooseCalc()
        m = [None, None]
        q = [None, None]

        m[0] = self.line[0].angCoeff
        q[0] = self.line[0].intercept

        m[1] = self.line[1].angCoeff
        q[1] = self.line[1].intercept
        
        #------------- from chatGPT
        # Get the indices that would sort 'm'
        sorted_indices = np.argsort(m)
        
        # Sort 'm' and 'q' based on the sorted indices
        m = [m[i] for i in sorted_indices]
        q = [q[i] for i in sorted_indices]
        #------------- from chatGPT


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        
        self.arc.center = point( x, y, draw = False )

        radius = (settings.xmax - settings.xmin)/20
        self.arc._radius = radius

        self.arc._color = self._color

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
        
        #for line in self.line:
        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()
                    break
                except:
                    pass


    """
    def draw(self, name = None):
        #self.__del__()
        self._name = name
        #if self.rotate == False:
        #    self.calc()

        self.chooseCalc()

        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        

        self.lines = []
        self.lines.append(line)
    """
        
    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
        #self.arc.erase()
        #self.center = None
