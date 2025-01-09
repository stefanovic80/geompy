from ..parabola.parabolaCalcFile import parabolaCalc

class method(parabolaCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('a', 'b', 'c'): self.calc_a_b_c,
            ('a', 'b', 'po'): self.calc_a_b_po,
            ('a', 'b', 'vx'): self.noMethod,
            ('a', 'b', 'vy'): self.noMethod,
            ('a', 'c', 'po'): self.calc_a_c_po,
            ('a', 'c', 'vx'): self.noMethod,
            ('a', 'c', 'vy'): self.noMethod,
            ('a', 'po', 'po'): self.calc_a_po_po,
            ('a', 'po', 'vx'): self.noMethod,
            ('a', 'po', 'vy'): self.noMethod,
            ('a', 'vx', 'vy'): self.calc_a_vx_vy,
            ('b', 'c', 'po'): self.calc_b_c_po,
            ('b', 'c', 'vx'): self.noMethod,
            ('b', 'c', 'vy'): self.noMethod,
            ('b', 'po', 'po'): self.calc_b_po_po,
            ('b', 'po', 'vx'): self.noMethod,
            ('b', 'po', 'vy'): self.noMethod,
            ('b', 'vx', 'vy'): self.calc_b_vx_vy,
            ('c', 'po', 'po'): self.calc_c_po_po,
            ('c', 'po', 'vx'): self.noMethod,
            ('c', 'po', 'vy'): self.noMethod,
            ('c', 'vx', 'vy'): self.calc_c_vx_vy,
            ('po', 'po', 'po'): self.calc_po_po_po,
            ('po', 'po', 'vx'): self.noMethod,
            ('po', 'po', 'vy'): self.noMethod,
            ('po', 'vx', 'vy'): self.calc_po_vx_vy
        }

            #('a', 'b', 've'): self.calc_a_b_ve,
            #('a', 'c', 've'): self.calc_a_c_ve,
            #('a', 'po', 've'): self.calc_a_po_ve,
            #('b', 'c', 've'): self.calc_b_c_ve,
            #('b', 'po', 've'): self.calc_b_po_ve,
            #('c', 'po', 've'): self.calc_c_po_ve,
            #('po', 'po', 've'): self.calc_po_po_ve

