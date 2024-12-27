from ..segment.segmentCalcFile import segmentCalc

class method(segmentCalc):
    def __init__(self):
        super().__init__()
        self.draws = {
            ('po', 'po'): self.calc_po_po
        }
