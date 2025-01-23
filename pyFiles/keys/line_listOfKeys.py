from ..line.lineCalcFile import lineCalc
from weakref import WeakMethod

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'po'): WeakMethod(self.calc_m_po),
            ('m', 'q'): WeakMethod(self.calc_m_q),
            ('po', 'po'): WeakMethod(self.calc_po_po),
            ('po', 'q'): WeakMethod(self.calc_po_q)
        }

