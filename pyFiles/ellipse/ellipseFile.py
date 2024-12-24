# circumference.py
from .. import plt, np, random
from ..Settings import settings

from .._plotSettFile import plotSett
from ..pointFile import point

#to be removed
from ..dataExploreFile import dataExplore

#class ellipse(method):
class ellipse(dataExplore):

    def __init__(self, draw = True):
        
        super().__init__()
        #plotSett.__init__(self)

        self._center = point(draw = False)
        self.focus1 = random.uniform(0, (settings.xmax-settings.xmin)/4)
        self.focus2 = random.uniform(0, (settings.xmax-settings.xmin)/4)
        
        self._color = random.choice(self.colors)

        self._center._color = self._color

        self.a = None
        self.b = None
        self.c = None


        if draw == True:
            self.draw()

    

    #to be revisited: y = f(x) for derivative > 1, x = f(y) for derivative < 1
    def calc(self):
        self.__del__()

        ellip = self.focus2*np.sqrt( 1 - ( ( self._x - self._center.data[0]  )/( self.focus1  )  )**2  )#ellipse equation      

        self.data = [self._x]
        self.data = self.data + [ np.append( self._center.data[1] + ellip, self._center.data[1] - ellip[::-1] ) ]

        #x values for the graph of the lower side
        self.data[0] = np.append( self.data[0], self.data[0][::-1])

        self.data[0] = np.append( self.data[0], self.data[0][0] )
        self.data[1] = np.append( self.data[1], self.data[1][0] )

        #line1, = self.ax.plot(self.data[0], self.data[1], color = self.color, label = self.name, linewidth = self.linewidth)


        #self.ax.legend()
        
        self.lines = []
        self.lines.append(line1)

        #self.ax.set_xlim(settings.xmin, settings.xmax)
        #self.ax.set_ylim(settings.xmin, settings.xmax)





    def chooseCalc(self):#, angle = 2*np.pi):
        self.__del__()

        #self._angle = angle
        calculation_functions = [self.calc]#, self.calc2, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    calc_function()#angle = angle)
                    break
                except:
                    pass



    #to be partially inherited
    def erase(self):
        self.__del__()

        self.data = [None, None]
        self._center.data = [None, None]
        self.focus1 = None
        self.focus2 = None



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
    
