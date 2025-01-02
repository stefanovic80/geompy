from ..line.lineCalcFile import lineCalc
#from ..line.lineCalcFile import m_po, m_q, po_po, po_q

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'po'): self.calc_m_po,
            ('m', 'q'): self.calc_m_q,
            ('po', 'po'): self.calc_po_po,
            ('po', 'q'): self.calc_po_q
        }
