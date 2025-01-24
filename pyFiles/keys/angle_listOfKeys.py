from ..angle.angleCalcFile import angleCalc
from weakref import WeakMethod

class method(angleCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('am', 'li', 'li'): WeakMethod(self.noMethod),
            ('am', 'li', 'po'): WeakMethod(self.noMethod),
            ('am', 'li', 'si'): WeakMethod(self.noMethod),
            ('am', 'po', 'po'): WeakMethod(self.noMethod),
            ('am', 'po', 'si'): WeakMethod(self.noMethod),
            ('am', 'si', 'si'): WeakMethod(self.noMethod),
            ('li', 'li', 'po'): WeakMethod(self.noMethod),
            ('li', 'li', 'si'): WeakMethod(self.noMethod),
            ('li', 'po', 'po'): WeakMethod(self.noMethod),
            ('li', 'po', 'si'): WeakMethod(self.noMethod),
            ('li', 'si', 'si'): WeakMethod(self.noMethod),
            ('po', 'po', 'po'): WeakMethod(self.noMethod),
            ('po', 'po', 'si'): WeakMethod(self.noMethod),
            ('po', 'si', 'si'): WeakMethod(self.noMethod)
        }

