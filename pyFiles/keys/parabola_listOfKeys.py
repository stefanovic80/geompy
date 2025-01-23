from ..parabola.parabolaCalcFile import parabolaCalc
from weakref import WeakMethod

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): WeakMethod(self.calc_a_b_c),
            ('a', 'b', 'po'): WeakMethod(self.calc_a_b_po),
            ('a', 'b', 'vx'): WeakMethod(self.noMethod),
            ('a', 'b', 'vy'): WeakMethod(self.noMethod),
            ('a', 'c', 'po'): WeakMethod(self.calc_a_c_po),
            ('a', 'c', 'vx'): WeakMethod(self.noMethod),
            ('a', 'c', 'vy'): WeakMethod(self.noMethod),
            ('a', 'po', 'po'): WeakMethod(self.calc_a_po_po),
            ('a', 'po', 'vx'): WeakMethod(self.noMethod),
            ('a', 'po', 'vy'): WeakMethod(self.noMethod),
            ('a', 'vx', 'vy'): WeakMethod(self.calc_a_vx_vy),
            ('b', 'c', 'po'): WeakMethod(self.calc_b_c_po),
            ('b', 'c', 'vx'): WeakMethod(self.noMethod),
            ('b', 'c', 'vy'): WeakMethod(self.noMethod),
            ('b', 'po', 'po'): WeakMethod(self.calc_b_po_po),
            ('b', 'po', 'vx'): WeakMethod(self.noMethod),
            ('b', 'po', 'vy'): WeakMethod(self.noMethod),
            ('b', 'vx', 'vy'): WeakMethod(self.calc_b_vx_vy),
            ('c', 'po', 'po'): WeakMethod(self.calc_c_po_po),
            ('c', 'po', 'vx'): WeakMethod(self.noMethod),
            ('c', 'po', 'vy'): WeakMethod(self.noMethod),
            ('c', 'vx', 'vy'): WeakMethod(self.calc_c_vx_vy),
            ('po', 'po', 'po'): WeakMethod(self.calc_po_po_po),
            ('po', 'po', 'vx'): WeakMethod(self.noMethod),
            ('po', 'po', 'vy'): WeakMethod(self.noMethod),
            ('po', 'vx', 'vy'): WeakMethod(self.calc_po_vx_vy)
        }

