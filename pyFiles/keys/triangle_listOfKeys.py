from ..triangle.triangleCalcFile import triangleCalc
from weakref import WeakMethod

class method(triangleCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('an', 'an', 'an'): WeakMethod(self.noMethod),
            ('an', 'an', 'po'): WeakMethod(self.noMethod),
            ('an', 'an', 'si'): WeakMethod(self.noMethod),
            ('an', 'po', 'po'): WeakMethod(self.noMethod),
            ('an', 'po', 'si'): WeakMethod(self.noMethod),
            ('an', 'si', 'si'): WeakMethod(self.noMethod),
            ('po', 'po', 'po'): WeakMethod(self.calc_po_po_po),
            ('po', 'po', 'si'): WeakMethod(self.noMethod),
            ('po', 'si', 'si'): WeakMethod(self.noMethod),
            ('si', 'si', 'si'): WeakMethod(self.noMethod)
        }

