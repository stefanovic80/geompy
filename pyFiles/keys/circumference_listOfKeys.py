from ..circumferenceCalcFile import circumferenceCalc

class method(circumferenceCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc_a_b_c,
            ('a', 'b', 'ce'): self.calc_a_b_ce,
            ('a', 'b', 'po'): self.calc_a_b_po,
            ('a', 'b', 'r'): self.calc_a_b_r,
            ('a', 'c', 'ce'): self.calc_a_c_ce,
            ('a', 'c', 'po'): self.calc_a_c_po,
            ('a', 'c', 'r'): self.calc_a_c_r,
            ('a', 'ce', 'po'): self.calc_a_ce_po,
            ('a', 'ce', 'r'): self.calc_a_ce_r,
            ('a', 'po', 'po'): self.calc_a_po_po,
            ('a', 'po', 'r'): self.calc_a_po_r,
            ('b', 'c', 'ce'): self.calc_a_c_ce,
            ('b', 'c', 'po'): self.calc_b_c_po,
            ('b', 'c', 'r'): self.calc_b_c_r,
            ('b', 'ce', 'po'): self.calc_b_ce_po,
            ('b', 'ce', 'r'): self.calc_b_ce_r,
            ('b', 'po', 'po'): self.calc_b_po_po,
            ('b', 'po', 'r'): self.calc_b_po_r,
            ('c', 'ce', 'po'): self.calc_c_ce_po,
            ('c', 'ce', 'r'): self.calc_c_ce_r,
            ('c', 'po', 'po'): self.calc_c_po_po,
            ('c', 'po', 'r'): self.calc_c_po_r,
            ('ce', 'po', 'po'): self.calc_ce_po_po,
            ('ce', 'po', 'r'): self.calc_ce_po_r,
            ('po', 'po', 'po'): self.calc_po_po_po,
            ('po', 'po', 'r'): self.calc_po_po_r
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
