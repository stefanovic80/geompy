from ..line.lineCalcFile import lineCalc
from ..line.lineCalcFile import m_po, m_q, po_po, po_q

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'po'): m_po,
            ('m', 'q'): m_q,
            ('po', 'po'): po_po,
            ('po', 'q'): po_q
        }
