from ..parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'p', 'p'): self.noMethod,
            ('m', 'p', 'q'): self.noMethod,
            ('p', 'p', 'q'): self.noMethod
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
