from .. import plt, np, random
from ..Settings import settings
from ..pointFile import point
from ..dataExploreFile import dataExplore
from .. import seed # may be not really necessary
from ..segment.segmentFile import segment


class triangleCalc(dataExplore):
    
    def __init__(self):

        super().__init__()

        u = self.getVertex()
        #to be fixed!
        u = self.getVertex()
        u = self.getVertex()
        """
        A = next(u)
        B = next(u)
        C = next(u)
        """

    def calc_ve_ve_ve(self):
        
        A.name, B.name, C.name = "A", "B", "C"
        s1, s1.points, s1.points = segment(), A, B
        s2, s2.points, s2.points = segment(), B, C
        s3, s3.points, s3.points = segment(), C, A

        self.data = [ np.array( A.x, B.x, C.x), np.array( A.y, B.y, C.y ) ]

    def calc1(self):
        for l in range(2):
            self.data[l] = np.array([])

        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
