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
            #self.lines[0].remove()

    @property
    def labels(self):
        
        if self.j%3==0:
            verticesLabels = ['A', 'B', 'C']
            for vertice, label in zip(self.vertices, verticesLabels):
                vertice.name = label 
        elif self.j%3==1:
            self.tex = []
            sidesLabels = ['c', 'a', 'b']
            k = 0
            for sidesLabel in sidesLabels:
                l1=k%3
                l2=(k+1)%3
                labelx = 1.1*(self.vertices[l1].x[0] + self.vertices[l2].x[0])/2
                labely = (self.vertices[l1].y[0] + self.vertices[l2].y[0])/2
                self.tex = self.tex + [ self.ax.text(labelx, labely, sidesLabel, fontsize = 14, color = self._colorV, ha ="center", va="center") ]
                k+=1
        else:
            k = 0
            for k in range(3):
                l = k%3
                self.vertices[l].__del__()


        self.j+=1

    def __del__(self):
        super().__del__()
        try:
            for tex in self.tex:
                tex.remove()
        except:
            pass
            

    def chooseCalc(self):
        self.__del__()
        calculation_functions = [self.calc1]

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
            
            #side.lines[0].remove()

            #append each one, x and y respectively of triangle sides data
            for l in range(2):
                #self.data[l] = np.append(self.data[l], side.data[l])
                self.data[l] = np.concatenate((self.vertices[j].data[l], self.data[l], side.data[l], self.vertices[k].data[l]))

            j +=1
        
        for j in range(3):
            self.side[j].lines[j].remove()


    def calc1(self):
        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
