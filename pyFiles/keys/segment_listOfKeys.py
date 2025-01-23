from ..segment.segmentCalcFile import segmentCalc
from weakref import WeakMethod

class method(segmentCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('po', 'po'): WeakMethod(self.noMethod)
        }

