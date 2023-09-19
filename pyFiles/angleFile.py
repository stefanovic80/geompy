# circumference.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .segmentFile import segment
from .circumferenceFile import circumference

class angle(circumference):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps):
        
        #super().__init__(xmin, xmax, steps, linewidth)
        super().__init__(radius)

        self.cross00 = None
        self.cross01 = None
        self.cross10 = None
        self.cross11 = None

        self.xx = None

