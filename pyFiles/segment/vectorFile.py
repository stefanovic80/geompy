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
        #line = self.ax.quiver(X, Y, U, V, angles= 'xy', scale_units='xy', scale=1, width = 0.003, headwidth=6, headlength=6, headaxislength=9)
        
        line = self.ax.quiver(
            X, Y, U, V, 
            angles='xy', 
            scale_units='xy', 
            scale=1, 
            width=0.003, 
            headwidth=6,      # Larghezza della base della punta
            headlength=9,     # Lunghezza totale della punta
            headaxislength=9  # <--- Impostalo UGUALE a headlength per base piatta
        )

        self.lines = []
        self.lines.append(line)

    @property
    def flip(self):
        self.data[0] = self.data[0][::-1]
        self.data[1] = self.data[1][::-1]
        self.onlyDraw()
