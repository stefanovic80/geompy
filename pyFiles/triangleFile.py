# triangle.py
from . import plt, np, random

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .segmentFile import segment

class triangle(plotSett):


    def __init__(self, xmin= -20, xmax = 20, steps = 500, linewidth = 2):
        
        super().__init__(xmin, xmax, steps, linewidth)

        self.segment = {'01': segment(), '12': segment(), '20': segment()}
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

        #x.sort(reverse = True)
        #y.sort(reverse = True)
        #angCoeff calculation

    def draw(self):
        self.remove()
        
        self.segment['01'].color = self.segment['12'].color = self.segment['20'].color = self.color

        self.segment['01'].draw()
         
        self.segment['12'].point[0].coords = self.segment['01'].point[1].coords
        self.segment['12'].draw()
        
        self.segment['20'].point[0].coords = self.segment['12'].point[1].coords

        self.segment['20'].draw()

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mType:\033[0m circumference\n"
            f"\nAttributes:\n"
            f"\033[93mradius:\033[0m {self.radius}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        instances = (
            f"\nInstances:\n"
            f"\033[93mcenter\033[0m\n"
        )
        
        return attributes + instances + self.plotSettings
    
