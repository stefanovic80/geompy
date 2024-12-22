from ..parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('m', 'p'): self.noMethod,
            ('m', 'q'): self.noMethod,
            ('p', 'p'): self.noMethod,
            ('p', 'q'): self.noMethod
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
