from .pyFiles.parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        self.labels = {
            ('a', 'b', 'c'): self.noMethod,
            ('a', 'b', 'p'): self.noMethod,
            ('a', 'b', 'v'): self.noMethod,
            ('a', 'c', 'p'): self.noMethod,
            ('a', 'c', 'v'): self.noMethod,
            ('a', 'p', 'p'): self.noMethod,
            ('a', 'p', 'v'): self.noMethod,
            ('b', 'c', 'p'): self.noMethod,
            ('b', 'c', 'v'): self.noMethod,
            ('b', 'p', 'p'): self.noMethod,
            ('b', 'p', 'v'): self.noMethod,
            ('c', 'p', 'p'): self.noMethod,
            ('c', 'p', 'v'): self.noMethod,
            ('p', 'p', 'p'): self.noMethod,
            ('p', 'p', 'v'): self.noMethod
        }

    def noMethod(self):
         print('Method still not implemented!')
