from ..parabola.parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc_a_b_c,
            ('a', 'b', 'po'): self.calc_a_b_po,
            ('a', 'b', 've'): self.calc_a_b_ve,
            ('a', 'c', 'po'): self.calc_a_c_po,
            ('a', 'c', 've'): self.calc_a_c_ve,
            ('a', 'po', 'po'): self.calc_a_po_po,
            ('a', 'po', 've'): self.calc_a_po_ve,
            ('b', 'c', 'po'): self.calc_b_c_po,
            ('b', 'c', 've'): self.calc_b_c_ve,
            ('b', 'po', 'po'): self.calc_b_po_po,
            ('b', 'po', 've'): self.calc_b_po_ve,
            ('c', 'po', 'po'): self.calc_c_po_po,
            ('c', 'po', 've'): self.calc_c_po_ve,
            ('po', 'po', 'po'): self.calc_po_po_po,
            ('po', 'po', 've'): self.calc_po_po_ve
        }

