from ..circumference.circumferenceCalcFile import circumferenceCalc

class method(circumferenceCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc_a_b_c,
            ('a', 'b', 'ce'): self.calc_a_b_ce,
            ('a', 'b', 'po'): self.calc_a_b_po,
            ('a', 'b', 'ra'): self.calc_a_b_ra,
            ('a', 'c', 'ce'): self.calc_a_c_ce,
            ('a', 'c', 'po'): self.calc_a_c_po,
            ('a', 'c', 'ra'): self.calc_a_c_ra,
            ('a', 'ce', 'po'): self.calc_a_ce_po,
            ('a', 'ce', 'ra'): self.calc_a_ce_ra,
            ('a', 'po', 'po'): self.calc_a_po_po,
            ('a', 'po', 'ra'): self.calc_a_po_ra,
            ('b', 'c', 'ce'): self.calc_a_c_ce,
            ('b', 'c', 'po'): self.calc_b_c_po,
            ('b', 'c', 'ra'): self.calc_b_c_ra,
            ('b', 'ce', 'po'): self.calc_b_ce_po,
            ('b', 'ce', 'ra'): self.calc_b_ce_ra,
            ('b', 'po', 'po'): self.calc_b_po_po,
            ('b', 'po', 'ra'): self.calc_b_po_ra,
            ('c', 'ce', 'po'): self.calc_c_ce_po,
            ('c', 'ce', 'ra'): self.calc_c_ce_ra,
            ('c', 'po', 'po'): self.calc_c_po_po,
            ('c', 'po', 'ra'): self.calc_c_po_ra,
            ('ce', 'po', 'po'): self.calc_ce_po_po,
            ('ce', 'po', 'ra'): self.calc_ce_po_ra,
            ('po', 'po', 'po'): self.calc_po_po_po,
            ('po', 'po', 'ra'): self.calc_po_po_ra
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
