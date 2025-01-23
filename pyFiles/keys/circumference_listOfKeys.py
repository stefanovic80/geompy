from ..circumference.circumferenceCalcFile import circumferenceCalc
from weakref import WeakMethod

class method(circumferenceCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): WeakMethod(self.calc_a_b_c),
            ('a', 'b', 'cx'): WeakMethod(self.noMethod),
            ('a', 'b', 'cy'): WeakMethod(self.noMethod),
            ('a', 'b', 'po'): WeakMethod(self.calc_a_b_po),
            ('a', 'b', 'ra'): WeakMethod(self.calc_a_b_ra),
            ('a', 'c', 'cx'): WeakMethod(self.noMethod),
            ('a', 'c', 'cy'): WeakMethod(self.noMethod),
            ('a', 'c', 'po'): WeakMethod(self.calc_a_c_po),
            ('a', 'c', 'ra'): WeakMethod(self.calc_a_c_ra),
            ('a', 'cx', 'cy'): WeakMethod(self.noMethod),
            ('a', 'cx', 'po'): WeakMethod(self.noMethod),
            ('a', 'cx', 'ra'): WeakMethod(self.noMethod),
            ('a', 'cy', 'po'): WeakMethod(self.noMethod),
            ('a', 'cy', 'ra'): WeakMethod(self.noMethod),
            ('a', 'po', 'po'): WeakMethod(self.calc_a_po_po),
            ('a', 'po', 'ra'): WeakMethod(self.calc_a_po_ra),
            ('b', 'c', 'cx'): WeakMethod(self.calc_b_c_cx),
            ('b', 'c', 'cy'): WeakMethod(self.noMethod),
            ('b', 'c', 'po'): WeakMethod(self.calc_b_c_po),
            ('b', 'c', 'ra'): WeakMethod(self.calc_b_c_po),
            ('b', 'cx', 'cy'): WeakMethod(self.noMethod),
            ('b', 'cx', 'po'): WeakMethod(self.noMethod),
            ('b', 'cx', 'ra'): WeakMethod(self.noMethod),
            ('b', 'cy', 'po'): WeakMethod(self.noMethod),
            ('b', 'cy', 'ra'): WeakMethod(self.noMethod),
            ('b', 'po', 'po'): WeakMethod(self.calc_b_po_po),
            ('b', 'po', 'ra'): WeakMethod(self.calc_b_po_ra),
            ('c', 'cx', 'cy'): WeakMethod(self.calc_c_cx_cy),
            ('c', 'cx', 'po'): WeakMethod(self.noMethod),
            ('c', 'cx', 'ra'): WeakMethod(self.noMethod),
            ('c', 'cy', 'po'): WeakMethod(self.noMethod),
            ('c', 'cy', 'ra'): WeakMethod(self.noMethod),
            ('c', 'po', 'po'): WeakMethod(self.calc_c_po_po),
            ('c', 'po', 'ra'): WeakMethod(self.calc_c_po_ra),
            ('cx', 'cy', 'po'): WeakMethod(self.calc_cx_cy_po),
            ('cx', 'cy', 'ra'): WeakMethod(self.calc_cx_cy_ra),
            ('cx', 'po', 'po'): WeakMethod(self.noMethod),
            ('cx', 'po', 'ra'): WeakMethod(self.noMethod),
            ('cy', 'po', 'po'): WeakMethod(self.noMethod),
            ('cy', 'po', 'ra'): WeakMethod(self.noMethod),
            ('po', 'po', 'po'): WeakMethod(self.calc_po_po_po),
            ('po', 'po', 'ra'): WeakMethod(self.calc_po_po_po)
        }

