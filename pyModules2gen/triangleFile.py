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
        for l in range(2):
            self.data[l] = np.array([])
        for side in self.sides:
            k = (j+1)%3
            #defines a side passing through vertices j and k
            side.points = self.vertices[j]
            side.points = self.vertices[k]
            side.color = self._color

            lims = [ self.vertices[j].x[0], self.vertices[k].x[0] ]
            lims.sort()
            
            #cut Off triangle sides
            for l in range(2):
                side.x = lims[l]
                side.cutOff
            

            #append each one, x and y respectively of triangle sides data
            for l in range(2):
                self.data[l] = np.append(self.data[l], side.data[l])
            
            #side.__del__()
            j +=1
