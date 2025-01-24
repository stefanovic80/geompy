from ..line.lineFile import line
from ..pointFile import point
#from ..dataExploreFile import dataExplore
from ..circumference.circumferenceFile import circumference
from .. import seed
from ..Settings import settings
from .. import plt, np, random


class angleCalc(circumference):
    def __init__(self, line0 = line(draw = False) , line1 = line(draw = False), seed = seed, draw = True):

        super().__init__()
        
        dof = 4
        
        #self._centre = point(draw = False)

        
        #self.line = [line0, line1]
        #self.angle = circumference(draw = False)
        
        #self.rotate = False
        #self._color = random.choice(self.colors)
        #self._name = None
        #self.data = None

        #self.j = 0
        
    #may be deprecated
    def calc(self):
        self.__del__()


        m = [None, None]
        q = [None, None]
        
        self.line[0]._color = self._color
        self.line[0].calc2()
        
        self.line[1]._color = self._color
        self.line[1].erase()
        self.line[1]._points[0] = self.line[0]._points[0]
        self.line[1].intercept = np.random.uniform(settings.xmin, settings.xmax)
        self.line[1].calc4()
        
        m[0] = self.line[0].angCoeff
        q[0] = self.line[0].intercept
        
        m[1] = self.line[1].angCoeff
        q[1] = self.line[1].intercept


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        self.angle._center = point( x, y, draw = False  )
        
        radius = (settings.xmax - settings.xmin)/20
        self.angle._radius = radius
        
        self.angle._color = self._color

        arcSize = np.arctan( m[1] ) - np.arctan( m[0] )
        self.angle.calc(arc = arcSize)
        
        self.angle._center.rotation( locus = self.angle, arc = np.arctan( m[0] ) )

        self.data = self.angle.data
        
        self.size = None

    
    
    def calc2(self):
        m = [None, None]
        q = [None, None]

        m[0] = self.line[0].angCoeff#[0]
        q[0] = self.line[0].intercept#[0]

        m[1] = self.line[1].angCoeff#[0]
        q[1] = self.line[1].intercept#[0]
        
        #------------- from chatGPT
        # Get the indices that would sort 'm'
        sorted_indices = np.argsort(m)
        
        # Sort 'm' and 'q' based on the sorted indices
        m = [m[i] for i in sorted_indices]
        q = [q[i] for i in sorted_indices]
        #------------- from chatGPT


        x = (q[1] - q[0])/(m[0] - m[1])
        y = m[0]*x + q[0]
        
        self.angle._center = point( x, y, draw = False )

        radius = (settings.xmax - settings.xmin)/20
        self.angle._radius = radius

        self.angle._color = self._color

        self.size = abs( self.j%2*np.pi - np.arctan( m[1] ) + np.arctan( m[0] )  )
        self.angle.calc(arc = self.size)
        #to be modified!
        
        formula = (self.j + 1)%2*np.arctan(m[0]) + self.j%2*np.arctan(m[1]) +int(self.j/2)*np.pi
        self.angle._center.rotation( locus = self.angle, arc = formula)

        #to be checked out!
        self.data = self.angle.data

        self.j+=1


    #def chooseCalc(self):
    def draw(self):
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

    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
