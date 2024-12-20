from ..parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        self.labels = {
            ('m', 'p', 'p'): self.noMethod,
            ('m', 'p', 'q'): self.noMethod,
            ('p', 'p', 'q'): self.noMethod
        }

    def noMethod(self):
         print('Method still not implemented!')
