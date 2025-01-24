from ..angle.angleCalcFile import angleCalc
from weakref import WeakMethod

class method(angleCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('am', 'cx', 'cy', 'po'): WeakMethod(self.noMethod),
            ('am', 'cx', 'po', 'po'): WeakMethod(self.noMethod),
            ('am', 'cy', 'po', 'po'): WeakMethod(self.noMethod),
            ('cx', 'cy', 'po', 'po'): WeakMethod(self.noMethod)
        }

