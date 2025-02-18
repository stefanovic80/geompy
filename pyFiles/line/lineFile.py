# lineFile.py
from .. import plt, np, random
from ..Settings import settings
from .._plotSettFile import plotSett
from ..pointFile import point

from .. import seed
from ..keys.line_listOfKeys import method


class line(method):
    #to be deprecated        
    dof = 2

    def __init__(self, seed = seed, draw = True):#, dof = dof):
        
        super().__init__()

        if draw: self.drawSetts()
    
    @property
    def m(self):
        return self.angCoeff


    @m.setter
    def m(self, value):
        """
        Sets the slope (angular coefficient) of the line and recalculates
        the line equation accordingly. Updates the internal parameters and 
        redraws the line representation.
    
        Parameters:
        value (float): The new slope (angular coefficient) of the line.
        """
        self.addParams("m", value)
        self.angCoeff = value
        self.drawSetts()

    @property
    def q(self):
        return self.intercept

    @q.setter
    def q(self, value):
        """
        Sets the intercept of the line and recalculates
        the line equation accordingly. Updates the internal parameters and
        redraws the line representation.
        
        Parameters:
        value (float): The new intercept of the line.
        """
        self.addParams("q", value)
        self.intercept = value
        self.drawSetts()
    
    #to be fixed
    def system(self, line):
        # Case when the first line is vertical
        if self.angCoeff == np.inf:  # Se la pendenza della prima retta è infinita
            x = self.data[0][0]  # La coordinata x è l'intercetta della retta verticale
            y = line.angCoeff * x + line.intercept  # Troviamo y dalla seconda retta
            return point(x, y)
    
        # Caso in cui la seconda retta è verticale
        elif line.angCoeff == np.inf:  # Se la pendenza della seconda retta è infinita
            x = line.data[0][0]  # La coordinata x è l'intercetta della retta verticale
            y = self.angCoeff * x + self.intercept  # Troviamo y dalla prima retta
            return point(x, y)
    
        # Caso generale, nessuna retta è verticale
        else:
            x = -(self.intercept - line.intercept) / (self.angCoeff - line.angCoeff)
            y = self.angCoeff * x + self.intercept
            return point(x, y)




    """
    def system(self, line):
        x = -(self.intercept - line.intercept)/(self.angCoeff - line.angCoeff) #if self.intecept not equal np.inf
        y = self.angCoeff*x + self.intercept
        return point(x, y)
    """
    
    @property
    def dataGroup(self):
        return self.data + self.labCoords

    @dataGroup.setter
    def dataGroup(self, value):
        self.data = value[0:2]

    def erase(self):
        self.__del__()

        self.data = [None, None]
        self.angCoeff = None
        self.intercept = None


    @property
    def equation(self):

        #to be (properly) inherited
        try:
            self.tex.remove()
        except:
            pass

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]
        random_index = np.random.randint(len(data[0]))
        shift = (settings.xmax - settings.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        #--------------------

        if self.intercept > 0:
            sign = '+'
        elif self.intercept <0:
            sign = '-'

        q = str(round(abs( self.q), 2))
        m = str(round(self.m, 2))
        eq = "y = " + m + "x" + sign + q
        try:
            eq = self._name + ": " + eq
        except:
            pass
        #labelx, labely may necessitte to be attributes
        if self.j%2 == 0:
            self.tex = self.ax.text(labelx, labely, eq, fontsize = 12, color = self._color, ha="center", va="center")
        self.j += 1


    def __str__(self):

        super().__str__()

        attributes = (
            f"Attributes:\n"#change 93 to 91 to make it red
            f"\033[93mClass type = \033[0m line\n"
            f"\033[93m.m = \033[0m {self.angCoeff}\n"
            f"\033[93m.q = \033[0m {self.intercept}\n"
            f"\033[93m.color = \033[0m {self._color}\n"
            f"\033[93m.linewdith =\033[0m {self._linewidth}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033\n"
        )            
        
        return attributes + methods + self.plotSettings

