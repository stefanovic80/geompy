from ..lineCalcFile import lineCalc

class method(lineCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'p'): self.calc_m_p,
            ('m', 'q'): self.calc_m_q,
            ('p', 'p'): self.calc_p_p,
            ('p', 'q'): self.calc_p_q
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
