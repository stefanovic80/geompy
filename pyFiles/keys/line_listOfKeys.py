from ..lineCalcFile import lineCalc

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'po'): self.calc_m_p,
            ('m', 'q'): self.calc_m_q,
            ('po', 'po'): self.calc_p_p,
            ('po', 'q'): self.calc_p_q
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
