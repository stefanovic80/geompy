from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett
from ..pyFiles.dataExploreFile import dataExplore

from ..pyFiles import seed 

from ..pyFiles.Settings import settings

from ..pyFiles import plt, np, random

class triangle(dataExplore):
    
    def __init__(self, seed = seed, draw = True):

        super().__init__()
        s = False
        self.vertices = [point(draw = s ), point(draw = s), point(draw = s)]
        self.sides = [line(draw = s), line(draw = s), line(draw = s)]
        
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
            for side, label in zip(self.sides, sidesLabels):
                side.name = label

        self.j+=1

    def chooseCalc(self):
        self.__del__()
        calculation_functions = [self.calc]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    self.lims()
                    calc_function()
                    break
                except:
                    pass



    def calc(self):
        
        j = 0
        for lineItem in self.sides:
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
            
            j += 1
            
            for k in range(2):
                self.data[k] = np.append(self.data[k], lineItem.data[k])
