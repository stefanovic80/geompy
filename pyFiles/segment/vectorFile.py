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










"""
class vector(segment):

    def clear_plot(self):
        # Invece di __del__, puliamo le linee esistenti
        if hasattr(self, 'lines'):
            for line in self.lines:
                line.remove()
        self.lines = []

    def onlyDraw(self):
        self.clear_plot()

        # Logica di calcolo indici pulita
        # Se abs(data[0][0]) > abs(data[0][1]), j=2, altrimenti j=1
        j = 2 if abs(self.data[0][0]) > abs(self.data[0][1]) else 1
        k = 3
        
        # Indici calcolati una volta sola
        idx_start = k % j
        idx_end = k % (j + 1)

        X = self.data[0][idx_start]
        Y = self.data[1][idx_start]
        U = self.data[0][idx_end] - self.data[0][idx_start]
        V = self.data[1][idx_end] - self.data[1][idx_start]

        line = self.ax.quiver(
            X, Y, U, V,
            angles='xy', scale_units='xy', scale=1,
            width=0.003, headwidth=6, headlength=9, headaxislength=9,
            color=self._color
        )
        self.lines.append(line)

    @property
    def flip(self):
        # Inverti i dati
        self.data[0] = self.data[0][::-1]
        self.data[1] = self.data[1][::-1]
        # Disegna usando la stessa logica di sempre
        self.onlyDraw()
"""
