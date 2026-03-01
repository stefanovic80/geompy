# lineFile.py
from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point

from . import seed
from .keys.line_listOfKeys import method


class vector():#method):
    #to be deprecated        
    dof = 2

    def __init__(self, seed = seed, draw = True):#, dof = dof):

        super().__init__()

        #if draw: self.drawSetts()


    def draw(self, X, Y, U, V):
        plt.quiver(X, Y, U, V, angles= 'xy', scale_units='xy', scale=1, width = 0.003)

    def name(name):
        plt.text(X + U/2 + 0.2, Y + V/2 + 0.2, name, fontsize=52)

