from .. import plt, np, random
from ..Settings import settings
from ..pointFile import point
from ..dataExploreFile import dataExplore
from .. import seed # may be not really necessary


class triangleCalc(dataExplore):
    
    def __init__(self):

        super().__init__()
        #to be fixed
        self.addParams('point0', point() )
        self.addParams('point1', point() )
        self.addParams('point2', point() )

    def calc_po_po_po(self):
        u = self.getPoint()
        
        A = next(u)
        B = next(u)
        C = next(u)
        
        self.data = [ np.array( [ A.x[0], B.x[0], C.x[0], A.x[0] ]), np.array( [ A.y[0], B.y[0], C.y[0], A.y[0] ]  ) ]

    def calc1(self):
        for l in range(2):
            self.data[l] = np.array([])

        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
