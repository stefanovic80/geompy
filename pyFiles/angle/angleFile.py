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

        if draw: self.drawSetts()

    #overwritten dataExplore method
    #-----------------------------------------
    @property
    def points(self):
        j = 0
        listOfPoints = []

        for u in zip(self.data[0], self.data[1]):
            listOfPoints = listOfPoints + [ point(u[0], u[1], draw = False) ]
            j+=1

        return listOfPoints


    @points.setter
    def points(self, value):

        k = self.p%2#self.dof

        self.addParams( "point" + str(k), value )
        #self.drawSetts()
        self.p += 1
    #-----------------------------------------

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self.addParams('am', value)
        self.drawSetts()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.calc_cx_cy_ra(arc = self._size)
        #self._centre.rotation( locus = self, angle = rotateAngle )
        #self.drawSetts()



    def erase(self):
        self.__del__()

        #to remove text label
        try:
            self.pointLabel.tex.remove()
        except:
            pass

        self.data = [None, None]
        self.line = [None, None]
