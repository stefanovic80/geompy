# segmentFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings
from ..pointFile import point
from ..keys.segment_listOfKeys import method
from .segmentFile import segment

class vector(segment):

    def onlyDrawFlip(self):
        self.__del__()


        X, Y, U, V = self.data[0][0], self.data[1][0], -self.data[0][0] + self.data[0][1], -self.data[1][0] + self.data[1][1]

        #X, Y, U, V = self.data[0][1], self.data[1][1], -self.data[0][1] + self.data[0][0], -self.data[1][1] + self.data[1][0]
        line = self.ax.quiver(
            X, Y, U, V,
            angles='xy',
            scale_units='xy',
            scale=1,
            width=0.003,
            headwidth=6,      # Larghezza della base della punta
            headlength=9,     # Lunghezza totale della punta
            headaxislength=9,  # <--- Impostalo UGUALE a headlength per base piatta
            color = self._color
        )

        self.lines = []
        self.lines.append(line)


    def onlyDraw(self):
        self.__del__()
        

        #X, Y, U, V = self.data[0][0], self.data[1][0], -self.data[0][0] + self.data[0][1], -self.data[1][0] + self.data[1][1]
        k = 3
        j = 1
        if abs(self.data[0][0]) > abs(self.data[0][1]):
            j += 1

        X, Y, U, V = self.data[0][k%j], self.data[1][k%j], -self.data[0][k%j] + self.data[0][k%(j+1)], -self.data[1][k%j] + self.data[1][k%(j+1)]
        #X, Y, U, V = self.data[0][1], self.data[1][1], -self.data[0][1] + self.data[0][0], -self.data[1][1] + self.data[1][0]

        line = self.ax.quiver(
            X, Y, U, V, 
            angles='xy', 
            scale_units='xy', 
            scale=1, 
            width=0.003, 
            headwidth=6,      # Larghezza della base della punta
            headlength=9,     # Lunghezza totale della punta
            headaxislength=9,  # <--- Impostalo UGUALE a headlength per base piatta
            color = self._color
        )

        self.lines = []
        self.lines.append(line)

    @property
    def flip(self):
        self.data[0] = self.data[0][::-1]
        self.data[1] = self.data[1][::-1]
        self.onlyDrawFlip()
