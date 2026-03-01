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
        line = self.ax.text(self.data[0], self.data[1], self.bodyAttr, color = self._color)
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
        self.__del__()
        fontsize = self._labelsize + 1
        line = self.ax.text(self.data[0], self.data[1], self.bodyAttr, color = self._color, fontsize = fontsize)


    @property
    def drop(self):
        self.__del__()
        fontsize = self._labelsize - 1
        line = self.ax.text(self.data[0], self.data[1], self.bodyAttr, color = self._color, fontsize = fontsize)
    #to be checked out
    #--------------------------------------------------
