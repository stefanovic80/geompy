from .pyFiles.parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        self.labels = {
            ('a', 'b', 'c'): self.noMethod,
            ('a', 'b', 'd'): self.noMethod,
            ('a', 'b', 'r'): self.noMethod,
            ('a', 'c', 'd'): self.noMethod,
            ('a', 'c', 'r'): self.noMethod,
            ('a', 'd', 'r'): self.noMethod,
            ('b', 'c', 'd'): self.noMethod,
            ('b', 'c', 'r'): self.noMethod,
            ('b', 'd', 'r'): self.noMethod,
            ('c', 'd', 'r'): self.noMethod
        }

    def noMethod(self):
         print('Method still not implemented!')
