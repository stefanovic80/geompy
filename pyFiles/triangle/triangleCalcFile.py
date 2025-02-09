from .. import plt, np, random
from ..Settings import settings
from ..pointFile import point
from ..dataExploreFile import dataExplore
from .. import seed # may be not really necessary
from ..segment.segmentFile import segment


class triangleCalc(dataExplore):
    
    def __init__(self):#, seed = seed, draw = True):

        super().__init__()

    

    def calc_ve_ve_ve(self):
        pass

    def calc1(self):
        for l in range(2):
            self.data[l] = np.array([])

        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
