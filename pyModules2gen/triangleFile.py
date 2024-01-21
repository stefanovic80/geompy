from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett

from ..pyFiles import seed #steps, linewidth, seed

from ..pyFiles.Settings import settings#xmin, xmax, linewidth, steps

from ..pyFiles import plt, np, random

class triangle(plotSett):
    
    def __init__(self, seed = seed, draw = True):

        super().__init__()
        s = False
        self.vertices = [point(draw = s ), point(draw = s), point(draw = s)]
        self.lines = [line(draw = s), line(draw = s), line(draw = s)]
        
        self._color = random.choice(self.colors)

        if draw == True:
            self.draw()
    def draw(self):
        j = 0
        for lineItem in self.lines:
            k = (j+1)%3
            lineItem.points = self.vertices[j]
            lineItem.points = self.vertices[k]
            
            lineItem.color = self._color

            lims = [ self.vertices[j].x[0], self.vertices[k].x[0] ]
            lims.sort()
            
            lineItem.x = lims[0]
            lineItem.cutOff
            lineItem.x = lims[1]
            lineItem.cutOff
            
            j += 1
