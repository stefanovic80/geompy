# segmentFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings
from ..pointFile import point
from ..keys.segment_listOfKeys import method


class segment(method):

    def __init__(self, point0 = None, point1 = None, seed = seed, draw = True):

        super().__init__()

        if draw: self.drawSetts()
    
    
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self.__del__()
        self._length = value
        self.addParams('length', abs(value) )
        self.drawSetts()

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self.addParams('angle', value)
        self.drawSetts()

    
    #to be deprecated
    #-------------------------------------
    @property
    def dataGroup(self):
        return self.data + self.labCoords

    @dataGroup.setter
    def dataGroup(self, value):
        self.data = value[0:2]
        #self.labCoords = value[2:4]
        #to be implemented!
    #-------------------------------------


    def erase(self):
        self.__del__()

        self.data = [None, None]


    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m line\n"
            f"\033[93m.m = \033[0m {self.angCoeff}\n"
            f"\033[93m.q = \033[0m {self.intercept}\n"
            f"\033[93m.color = \033[0m {self._color}\n"
            f"\033[93m.linewdith =\033[0m {self._linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

