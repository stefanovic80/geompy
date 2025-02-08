from ..line.lineFile import line
from ..pointFile import point
from ..segment.segmentFile import segment
from .._plotSettFile import plotSett
from ..dataExploreFile import dataExplore
from ..circumference.circumferenceFile import circumference

from .. import seed 

from ..Settings import settings

from .. import plt, np, random


#from ..keys.triangle_listOfKeys import method

class triangleCalc(dataExplore):
    
    def __init__(self, seed = seed, draw = True):

        super().__init__()
        s = False
        self.vertices = [point(draw = s ), point(draw = s), point(draw = s)]
        #self.sides = [line(draw = s), line(draw = s), line(draw = s)]
        
        self._color = random.choice(self.colors)
        self._colorV = random.choice(self.colors)
        
        #to set up "labels" decorated method
        self.j = 0

        #to set up setter decorated labels
        self.k = 0
        
        #to set up setter decorated vertex
        self.l = 0
        
        self._side = 0

        for v in self.vertices:
            v.color = self._colorV
    

    def calc_ve_ve_ve(self):
        pass

    def calc1(self):
        for l in range(2):
            self.data[l] = np.array([])

        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
