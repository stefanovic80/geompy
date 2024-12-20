from ..parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc00,
            ('a', 'b', 'p'): self.calc01,
            ('a', 'b', 'v'): self.calc02,
            ('a', 'c', 'p'): self.calc03,
            ('a', 'c', 'v'): self.calc04,
            ('a', 'p', 'p'): self.calc05,
            ('a', 'p', 'v'): self.calc06,
            ('b', 'c', 'p'): self.calc08,
            ('b', 'c', 'v'): self.calc09,
            ('b', 'p', 'p'): self.calc10,
            ('b', 'p', 'v'): self.noMethod,
            ('c', 'p', 'p'): self.calc12,
            ('c', 'p', 'v'): self.noMethod,
            ('p', 'p', 'p'): self.calc14,
            ('p', 'p', 'v'): self.noMethod
        }

    def noMethod(self):
         print('Method still not implemented!')
