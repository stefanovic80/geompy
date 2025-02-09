# triangleFile.py
from .. import plt, np, random
from .. import seed
from ..Settings import settings
from ..pointFile import point
from ..keys.triangle_listOfKeys import method


class triangle(method):
    
    def __init__(self, seed = seed, draw = False):

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
        
        self._side = 0

        for v in self.vertices:
            v.color = self._colorV
        
        self.draws = {('a', 'b', 'c'): self.calc1}
        

        if draw: self.drawSetts()

    
    #to be properly implemented!
    #------------------------------
    @property
    def ar(self):
        pass

    @ar.setter
    def ar(self, value):
        j = value
        lines = [None, None]
        for j in range(2):
            lines[j] = line()#draw = False)
            #lines[j+1] = line()#draw = False)
            lines[j].points = self.vertices[0]
            lines[j].points = self.vertices[1]
    #------------------------------

    @property
    def side(self):
        k = self._side%3
        l = (self._side +1)%3
        sideSize = ( (self.vertices[k].x[0] - self.vertices[l].x[0])**2 + (self.vertices[k].y[0] - self.vertices[l].y[0])**2 )**.5
        return self._side, sideSize


    @side.setter
    def side(self, value):
        k = value%3
        l = (value +1)%3
        self._side = k
        sideSize = ( (self.vertices[k].x[0] - self.vertices[l].x[0])**2 + (self.vertices[k].y[0] - self.vertices[l].y[0])**2 )**.5
        print(str(self._side) + ' ' + str(sideSize) ) 
        #return self._side, sideSize

    def size(self, newSize):

        #coeff = [None, None, None]
        for j in range(3):
            size = self.vertices[j%3].dist(self.vertices[(j+1)%3])
            #coeff[j] = newSize/size 

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
        cosine = [None, None, None] 
        sine = [None, None, None]
        for j in range(3):
            k = j%3
            l = (j+1)%3
            cathetus0 = x[l] - x[k]
            cathetus1 = y[l] - y[k]

            cosine[k] = cathetus0/size
            sine[k] = cathetus1/size
            tan[k] = cathetus1/cathetus0
            
            xm[k] = (x[l] + x[k])/2
            ym[k] = (y[l] + y[k])/2
        
        #triangle centroid coordinates calculations base on a system of two different lines
        
        xcentroid = (tan[0]*xm[1] - tan[1]*xm[0] + (ym[1] - ym[0])*tan[0]*tan[1])/(tan[0] - tan[1])
        ycentroid = -(xcentroid - xm[0])/tan[0] + ym[0]
        
        radius0 = ( ( xcentroid - x[0] )**2 + (ycentroid - y[0])**2 )**.5
        

        m = self._side
        size = self.vertices[m%3].dist(self.vertices[(m+1)%3])
        radius1 = newSize*radius0/size
        
        centroid = point(xcentroid, ycentroid, draw = False)
        xc, yc = centroid.x[0], centroid.y[0]
        
        t = [None, None, None]
        for j in range(3):
            
            n = 0
            if xc > x[j]:
                n = np.pi

            t[j] = np.arctan( (yc - y[j])/(xc - x[j]) ) + n
            self.vertices[j] = centroid.dist(radius1, angle = t[j])
        
        self.draw()
        
    @property
    def vertex(self):
        self.l += 1
        #u = self.vertices[self.l%3].name
        self.vertices[self.l%3].name = 'm'
        

    @vertex.setter
    def vertex(self, point):
        self.vertices[self.l%3].__del__()
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
