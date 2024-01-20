from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett

from ..pyFiles import seed #steps, linewidth, seed

from ..pyFiles.Settings import settings#xmin, xmax, linewidth, steps

from ..pyFiles import plt, np, random

class triangle(plotSett):
    
    def __init__(self, seed = seed):
        self.points = [point(), point(), point()]
        self.lines = [line(), line(), line()]
        
        j = 0
        for lineItem in self.lines:
            k = (j+1)%3
            lineItem.points = self.points[j]
            lineItem.points = self.points[k]

            lims = [ self.points[j].x[0], self.points[k].x[0] ]
            lims.sort()
            
            lineItem.x = lims[0]
            lineItem.cutOff
            lineItem.x = lims[1]
            lineItem.cutOff
            
            j += 1
