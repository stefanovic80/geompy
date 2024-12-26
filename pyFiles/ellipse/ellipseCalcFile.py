from .. import plt, np, random
from ..Settings import settings
from .._plotSettFile import plotSett
from ..pointFile import point
from ..dataExploreFile import dataExplore

# to be removed
from itertools import combinations
from ..keys import ellipse_listOfKeys

from collections import deque

class ellipseCalc(dataExplore):
    def __init__(self):
        super().__init__()


        dof = 5
        self.keys = deque(maxlen = dof)
        #self.sflk = deque(maxlen = dof)
        self.values = deque(maxlen = dof)

        self._center = point(draw = False)
        self.focus1 = random.uniform(0, (settings.xmax-settings.xmin)/4)
        self.focus2 = random.uniform(0, (settings.xmax-settings.xmin)/4)
        
        self._color = random.choice(self.colors)

        self._center._color = self._color


        self._a = random.uniform(settings.xmin, settings.xmax)**-1
        self.addParams('a', self._a)
        self._b = random.uniform(settings.xmin, settings.xmax) 
        self.addParams('b', self._b)
        self._c = random.uniform(settings.xmin, settings.xmax)
        self.addParams('c', self._c)
        self._d = random.uniform(settings.xmin, settings.xmax)
        self.addParams('d', self._d)
        self._e = random.uniform(settings.xmin, settings.xmax)
        self.addParams('e', self._e)
