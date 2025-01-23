from ..triangle.triangleCalcFile import triangleCalc
from weakref import WeakMethod

class method(triangleCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('an', 'an', 'an'): WeakMethod(self.noMethod),
            ('an', 'an', 'si'): WeakMethod(self.noMethod),
            ('an', 'an', 've'): WeakMethod(self.noMethod),
            ('an', 'si', 'si'): WeakMethod(self.noMethod),
            ('an', 've', 'si'): WeakMethod(self.noMethod),
            ('an', 've', 've'): WeakMethod(self.noMethod),
            ('si', 'si', 'si'): WeakMethod(self.noMethod),
            ('ve', 'si', 'si'): WeakMethod(self.noMethod),
            ('ve', 've', 'si'): WeakMethod(self.noMethod),
            ('ve', 've', 've'): WeakMethod(self.noMethod)
        }

