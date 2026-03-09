# segmentFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings
from ..pointFile import point
from ..keys.segment_listOfKeys import method
from .segmentFile import segment

class vector(segment):

    def onlyDraw(self):
        self.__del__()
        X, Y, U, V = self.data[0][0], self.data[1][0], -self.data[0][0] + self.data[0][1], -self.data[1][0] + self.data[1][1]
        line = self.ax.quiver(X, Y, U, V, angles= 'xy', scale_units='xy', scale=1, width = 0.003, headwidth=10, headlength=10, headaxislength=9)
        self.lines = []
        self.lines.append(line)

    @property
    def flip(self):
        self.data[0] = self.data[0][::-1]
        self.data[1] = self.data[1][::-1]
        self.onlyDraw()
