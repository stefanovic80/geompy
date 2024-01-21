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
        self._colorV = random.choice(self.colors)
        
        #to set up "labels" decorated method
        self.j = 0

        for v in self.vertices:
            v.color = self._colorV

        if draw == True:
            self.draw()

    @property
    def labels(self):
        
        if self.j%2 == 0:
            verticesLabels = ['A', 'B', 'C']
            for vertice, label in zip(self.vertices, verticesLabels):
                vertice.name = label 
        else:
            sidesLabels = ['c', 'a', 'b']
            for side, label in zip(self.lines, sidesLabels):
                side.name = label

        self.j+=1


    def draw(self):
        j = 0
        for lineItem in self.lines:
            k = (j+1)%3
            lineItem.points = self.vertices[j]
            lineItem.points = self.vertices[k]
            
            lineItem.color = self._color
            
            
            #if lineItem.angCoeff < 1:
            lims = [ self.vertices[j].x[0], self.vertices[k].x[0] ]
            lims.sort()
                    
            lineItem.x = lims[0]
            lineItem.cutOff
            lineItem.x = lims[1]
            lineItem.cutOff
            
            """
            else:
                lims = [ self.vertices[j].y[0], self.vertices[k].y[0] ]
                lims.sort()
            
                lineItem.y = lims[0]
                lineItem.cutOff
                lineItem.y = lims[1]
                lineItem.cutOff
            """
            j += 1
