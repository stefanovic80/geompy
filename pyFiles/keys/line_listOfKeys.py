from ..lineCalcFile import lineCalc

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'po'): self.calc_m_po,
            ('m', 'q'): self.calc_m_q,
            ('po', 'po'): self.calc_po_po,
            ('po', 'q'): self.calc_po_q
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
