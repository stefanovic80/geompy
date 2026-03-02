#pointFile.py

from . import plt, np, random
from ._plotSettFile import plotSett
from . import seed
from .Settings import settings
from .pointFile import point

class text(point):
    
    """
    def __init__(self, body="text"):
        super().__init__(self, body="text")#, **kwargs)#(x=x, y=y, **kwargs)
        
        self.bodyAttr = body
    """
    def onlyDraw(self):
        self.__del__()
        #line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        line = self.ax.text(self.data[0], self.data[1], self.bodyAttr, color = self._color, fontsize = self._labelsize)
        self.lines = []
        self.lines.append(line)

    @property
    def name(self):
        return self.bodyAttr

    @name.setter
    def name(self, value):
        self.bodyAttr = value
        self.onlyDraw()


    #------------------------------------------------
    #to be checked out
    @property
    def rise(self):
        self._labelsize = self._labelsize + 1
        self.onlyDraw()

    @rise.setter
    def rise(self, value):
        self._labelsize = self._labelsize + value
        self.onlyDraw()

    @property
    def drop(self):
        self._labesize = self._labelsize - 1
        self.onlyDraw()
    
    @drop.setter
    def drop(self, value):
        self._labelsize = self._labelsize - value
        self.onlyDraw()
    #--------------------------------------------------
