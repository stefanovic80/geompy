from ..parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc00,
            ('a', 'b', 'po'): self.calc01,
            ('a', 'b', 'v'): self.calc02,
            ('a', 'c', 'po'): self.calc03,
            ('a', 'c', 'v'): self.calc04,
            ('a', 'po', 'po'): self.calc05,
            ('a', 'po', 'v'): self.calc06,
            ('b', 'c', 'po'): self.calc08,
            ('b', 'c', 'v'): self.calc09,
            ('b', 'po', 'po'): self.calc10,
            ('b', 'po', 'v'): self.noMethod,
            ('c', 'po', 'po'): self.calc12,
            ('c', 'po', 'v'): self.noMethod,
            ('po', 'po', 'po'): self.calc14,
            ('po', 'po', 'v'): self.noMethod
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
