from ..pyFiles.lineFile import line
from ..pyFiles.pointFile import point
from ..pyFiles._plotSettFile import plotSett
from ..pyFiles.dataExploreFile import dataExplore
from ..pyFiles.circumferenceFile import circumference

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
        
        #to set up setter decorated vertex
        self.l = 0

        for v in self.vertices:
            v.color = self._colorV

        if draw == True:
            self.draw()

    def size(self, newSize):
        j = 0
        size = self.vertices[j%3].dist(self.vertices[(j+1)%3])
        coeff = newSize/size #= self.vertices[j%3].dist(self.vertices[(j+1)%3])

        for j in range(3):
            #k = j%3
            size = self.vertices[j%3].dist(self.vertices[(j+1)%3])

            cosine = (self.vertices[(j+1)%3].x[0] - self.vertices[j%3].x[0])/size 
            """
            self.vertices[j%3].x = self.vertices[j%3].x[0] - cosine*coeff*size/2
            self.vertices[(j+1)%3].x = self.vertices[(j+1)%3].x[0] + cosine*coeff*size/2
            
            sine = (self.vertices[(j+1)%3].y[0] - self.vertices[j%3].y[0])/size
            self.vertices[j%3].y = self.vertices[j%3].y[0] - sine*coeff*size/2
            self.vertices[(j+1)%3].y = self.vertices[(j+1)%3].y[0] + sine*coeff*size/2


            """
            self.vertices[j%3].x = self.vertices[j%3].x[0] - cosine*(newSize -size)/2
            self.vertices[(j+1)%3].x = self.vertices[(j+1)%3].x[0] + cosine*(newSize -size)/2
       

            sine = (self.vertices[(j+1)%3].y[0] - self.vertices[j%3].y[0])/size
            self.vertices[j%3].y = self.vertices[j%3].y[0] - sine*(newSize -size)/2
            self.vertices[(j+1)%3].y = self.vertices[(j+1)%3].y[0] + sine*(newSize -size)/2
            
        self.draw()



    #the one
    def size1(self, newSize):

        coeff = [None, None, None]
        for j in range(3):
            size = self.vertices[j%3].dist(self.vertices[(j+1)%3])
            coeff[j] = newSize/size 

        #x, y = vertices coords
        #xm, ym = middle points for each side
        #tan = angular coefficient of each side
        x = [None, None, None]
        y = [None, None, None]
        xm = [None, None, None]
        ym = [None, None, None]
        tan = [None, None, None]
        for j in range(3):
            k = j%3
            l = (j+1)%3
            size = self.vertices[k].dist(self.vertices[l])
            x[k] = self.vertices[k].x[0]
            x[l] = self.vertices[l].x[0]
            y[k] = self.vertices[k].y[0]
            y[l] = self.vertices[l].y[0]
        
        #cosine = cosine for each side
        #sine = sine for each side
        cosine = [None, None] 
        sine = [None, None]
        for j in range(2):
            k = j%3
            l = (j+1)%3
            cathetus0 = x[l] - x[k]
            cathetus1 = y[l] - y[k]
            cosine[k] = cathetus0/size
            sine[k] = cathetus1/size
            
            tan[k] = cathetus1/cathetus0
            xm[k] = (x[l] + x[k])/2
            ym[k] = (y[l] + y[k])/2
        
        #triangle centroid coordinates calculations base on a system of two different 
        j = 0
        xcentroid = (tan[j]*xm[j+1] - tan[j+1]*xm[j] + (ym[j+1] - ym[j])*tan[j]*tan[j+1])/(tan[j] - tan[j+1])
        ycentroid = -(xcentroid - xm[0])/tan[0] + ym[0]
        
        sideCentroid_dist = [None, None]
        for j in range(2):
            sideCentroid_dist[j] = ( (xm[j] - xcentroid)**2 + (ym[j] - ycentroid)**2 )**.5
        

        j = 0
        self.vertices[j%3].x = self.vertices[j%3].x[0] - cosine[j]*coeff[j]*size/2
            
        self.vertices[j%3].y = self.vertices[j%3].y[0] - sine[j]*coeff[j]*size/2
        

        
        j += 1

        self.vertices[j%3].x = self.vertices[j%3].x[0] - cosine[j]*coeff[j]*size/2

        self.vertices[j%3].y = self.vertices[j%3].y[0] - sine[j]*coeff[j]*size/2


        self.vertices[(j+1)%3].x = self.vertices[(j+1)%3].x[0] + cosine[j]*coeff[j]*size/2
            
        self.vertices[(j+1)%3].y = self.vertices[(j+1)%3].y[0] + sine[j]*coeff[j]*size/2
        return point(xcentroid, ycentroid)

    @property
    def vertex(self):
        self.l += 1
        #u = self.vertices[self.l%3].name
        self.vertices[self.l%3].name = 'm'
        

    @vertex.setter
    def vertex(self, point):
        self.vertices[self.l%3] = point
        self.l += 1
        #self.erase() 
        try:
            self.draw()
            #self.l = 0
        except:
            pass

        #return self.vertices[self.l%3]


    @property
    def labels(self):
        
        if self.j%3==0:
            verticesLabels = ['0', '1', '2']
            for vertice, label in zip(self.vertices, verticesLabels):
                vertice.name = label
        elif self.j%3==1:
            verticesLabels = ['A', 'B', 'C']
            
            for vertice, label in zip(self.vertices, verticesLabels):
                vertice.name = label

        else:
            k = 0
            for k in range(3):
                l = k%3
                self.vertices[l].__del__()

        self.j+=1



        """
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
        """
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
                    self.lims()
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
