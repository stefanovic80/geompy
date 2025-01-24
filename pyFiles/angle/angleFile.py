from ..line.lineFile import line
from ..pointFile import point
from .._plotSettFile import plotSett
from ..circumference.circumferenceFile import circumference
from .. import seed
from ..Settings import settings
from .. import plt, np, random
from ..keys.angle_listOfKeys import method

class angle(method):
    def __init__(self, line0 = line(draw = False) , line1 = line(draw = False), seed = seed, draw = False):

        super().__init__()
        
        self.line = [line0, line1]
        self.angle = circumference(draw = False)
        
        self.rotate = False
        self._color = random.choice(self.colors)
        self._name = None
        self.data = None

        self.j = 0
        
        if draw: self.drawSetts()




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
