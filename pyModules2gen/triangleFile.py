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
        #self.sides = [line(draw = s), line(draw = s), line(draw = s)]
        
        self._color = random.choice(self.colors)
        self._colorV = random.choice(self.colors)
        
        #to set up "labels" decorated method
        self.j = 0

        #to set up setter decorated labels
        self.k = 0

        for v in self.vertices:
            v.color = self._colorV

        if draw == True:
            self.draw()

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

    @labels.setter
    def labels(self, label):
        j=self.k%3
        self.vertices[j].name = str(label)
        self.k+=1



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
                    #self.lims()
                    calc_function()
                    break
                except:
                    pass


    def calc1(self):
        for l in range(2):
            self.data[l] = np.array([])

        for k in range(2):
            for j in range(4):
                l = j%3
                self.data[k] = np.append(self.data[k], self.vertices[l].data[k])
