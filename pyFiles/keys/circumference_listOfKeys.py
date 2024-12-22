from ..circumferenceCalcFile import circumferenceCalc

class method(circumferenceCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
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
         print('This method has not been implemented yet!')
