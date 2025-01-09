from ..circumference.circumferenceCalcFile import circumferenceCalc

class method(circumferenceCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc_a_b_c,
            ('a', 'b', 'cx'): self.noMethod,
            ('a', 'b', 'cy'): self.noMethod,
            ('a', 'b', 'po'): self.calc_a_b_po,
            ('a', 'b', 'ra'): self.calc_a_b_ra,
            ('a', 'c', 'cx'): self.noMethod,
            ('a', 'c', 'cy'): self.noMethod,
            ('a', 'c', 'po'): self.calc_a_c_po,
            ('a', 'c', 'ra'): self.calc_a_c_ra,
            ('a', 'cx', 'cy'): self.noMethod,
            ('a', 'cx', 'po'): self.noMethod,
            ('a', 'cx', 'ra'): self.noMethod,
            ('a', 'cy', 'po'): self.noMethod,
            ('a', 'cy', 'ra'): self.noMethod,
            ('a', 'po', 'po'): self.calc_a_po_po,
            ('a', 'po', 'ra'): self.calc_a_po_ra,
            ('b', 'c', 'cx'): self.noMethod,
            ('b', 'c', 'cy'): self.noMethod,
            ('b', 'c', 'po'): self.calc_b_c_po,
            ('b', 'c', 'ra'): self.calc_b_c_ra,
            ('b', 'cx', 'cy'): self.noMethod,
            ('b', 'cx', 'po'): self.noMethod,
            ('b', 'cx', 'ra'): self.noMethod,
            ('b', 'cy', 'po'): self.noMethod,
            ('b', 'cy', 'ra'): self.noMethod,
            ('b', 'po', 'po'): self.calc_b_po_po,
            ('b', 'po', 'ra'): self.calc_b_po_ra,
            ('c', 'cx', 'cy'): self.calc_c_cx_cy,
            ('c', 'cx', 'po'): self.noMethod,
            ('c', 'cx', 'ra'): self.noMethod,
            ('c', 'cy', 'po'): self.noMethod,
            ('c', 'cy', 'ra'): self.noMethod,
            ('c', 'po', 'po'): self.calc_c_po_po,
            ('c', 'po', 'ra'): self.calc_c_po_ra,
            ('cx', 'cy', 'po'): self.calc_cx_cy_po,
            ('cx', 'cy', 'ra'): self.calc_cx_cy_ra,
            ('cx', 'po', 'po'): self.noMethod,
            ('cx', 'po', 'ra'): self.noMethod,
            ('cy', 'po', 'po'): self.noMethod,
            ('cy', 'po', 'ra'): self.noMethod,
            ('po', 'po', 'po'): self.calc_po_po_po,
            ('po', 'po', 'ra'): self.calc_po_po_ra 
        }


            
            #('a', 'b', 'ce'): self.calc_a_b_ce,
            #('a', 'c', 'ce'): self.calc_a_c_ce,
            #('b', 'c', 'ce'): self.calc_b_c_ce,
            #('c', 'ce', 'po'): self.calc_c_ce_po,
            #('c', 'ce', 'ra'): self.calc_c_ce_ra,
            #('ce', 'po', 'po'): self.calc_ce_po_po,
            #('ce', 'po', 'ra'): self.calc_ce_po_ra,
            
