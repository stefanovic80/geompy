from ..line.lineFile import line
from ..pointFile import point
from .._plotSettFile import plotSett
from ..circumference.circumferenceFile import circumference
from .. import seed
from ..Settings import settings
from .. import plt, np, random
from ..keys.angle_listOfKeys import method

class angle(method):
    
    dof = 4

    #def __init__(self, line0 = line(draw = False) , line1 = line(draw = False), seed = seed, draw = False):
    def __init__(self, seed = seed, draw = True, dof = dof):

        super().__init__()

        #if draw: self.drawSetts()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self.addParams('am', value)

    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
