# triangle.py
from . import plt, np, random

#plt.ion()

from ._plotSettFile import plotSett
from .pointFile import point
from .segmentFile import segment

class triangle(plotSett):


    def __init__(self, xmin= -20, xmax = 20, steps = 500, linewidth = 2):
        
        super().__init__(xmin, xmax, steps, linewidth)

        self.point = [point(), point(), point()]
        self.segment = {'01': segment(), '02': segment(), '12': segment()}
        self.lines = None
        self.data = None
        self.name = None
        self.color = random.choice(self.colors)

    def calc(self):
        
        x = [None, None, None]
        y = [None, None, None]
        for j in range(3):
            x[j] = self.point[j].coords[0]
            y[j] = self.point[j].coords[1]

        #angCoeff calculation

        self.segment['01'].angCoeff = ( y[0] - y[1] )/(x[0] - x[1] )

        self.segment['02'].angCoeff = ( y[0] - y[2] )/(x[0] - x[2] )

        self.segment['12'].angCoeff = ( y[1] - y[2] )/(x[1] - x[2] )

        #intercept calculation

        self.segment['01'].intercept = ( x[0]*y[1] - x[1]*y[0]  )/( x[0] - x[1]  )


        self.segment['02'].intercept = ( x[0]*y[2] - x[2]*y[0]  )/( x[0] - x[2]  )


        self.segment['12'].intercept = ( x[1]*y[2] - x[2]*y[1]  )/( x[1] - x[2]  )

    def draw(self):
        self.remove()

        
        self.segment['01'].color = self.color
        self.segment['02'].color = self.color
        self.segment['12'].color = self.color

        
        self.segment['01'].draw()
        self.segment['02'].draw()
        self.segment['12'].draw() 

        self.segment['01'].xMax = self.point[0].coords[0]

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
    
