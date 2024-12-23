from ..parabola.parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc00,
            ('a', 'b', 'po'): self.calc01,
            ('a', 'b', 've'): self.calc02,
            ('a', 'c', 'po'): self.calc03,
            ('a', 'c', 've'): self.calc04,
            ('a', 'po', 'po'): self.calc05,
            ('a', 'po', 've'): self.calc06,
            ('b', 'c', 'po'): self.calc08,
            ('b', 'c', 've'): self.calc09,
            ('b', 'po', 'po'): self.calc10,
            ('b', 'po', 've'): self.calc16,
            ('c', 'po', 'po'): self.calc12,
            ('c', 'po', 've'): self.calc17,
            ('po', 'po', 'po'): self.calc14,
            ('po', 'po', 've'): self.calc18
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
