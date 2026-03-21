# segmentFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings
from ..pointFile import point
from ..keys.segment_listOfKeys import method
from .segmentFile import segment





class vector(segment):

    def Draw(self):
        #self.__del__()


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
        
        idx0 = np.abs(self.data[0]).argmin()#first point being the one closer to the origin
        idx1 = 1 - idx0
        
        self.data[0] = self.data[0][[idx0, idx1]]
        self.data[1] = self.data[1][[idx0, idx1]]


        self.Draw()
    

    #--------------------------------------------------------
    @property
    def tail(self):
        return point(self.data[0][0], self.data[1][0])
    
    @tail.setter
    def tail(self, pt):
        self.__del__()
        self._point[0].__del__()#to be fixed
        self._point[0] = pt
        self.data[0][0] = pt.data[0]
        self.data[1][0] = pt.data[1]
        self.Draw()

    @property
    def head(self):
        return point(self.data[0][1], self.data[1][1])

    @head.setter
    def head(self, pt):
        self.__del__()
        self._point[1].__del__()
        self._point[1] = pt
        self.data[0][1] = pt.data[0]
        self.data[1][1] = pt.data[1]
        self.Draw()

    #--------------------------------------------------------
    
    @property
    def flip(self):
        self.__del__()
        self.data[0] = self.data[0][::-1]
        self.data[1] = self.data[1][::-1]
        self.Draw()
