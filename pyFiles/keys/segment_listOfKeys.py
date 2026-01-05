from ..segment.segmentCalcFile import segmentCalc
from weakref import WeakMethod

class method(segmentCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('an', 'le'): WeakMethod(self.calc_an_le),
            ('an', 'po'): WeakMethod(self.calc_an_po),
            ('le', 'po'): WeakMethod(self.calc_le_po),
            ('po', 'po'): WeakMethod(self.calc_po_po)
        }

