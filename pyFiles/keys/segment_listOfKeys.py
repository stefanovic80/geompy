from ..segment.segmentCalcFile import segmentCalc
from weakref import WeakMethod

class method(segmentCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('an', 'le', 'po'): WeakMethod(self.calc_an_le_po),
            ('an', 'po', 'po'): WeakMethod(self.calc_po_po),
            ('le', 'po', 'po'): WeakMethod(self.calc_po_po)
        }

