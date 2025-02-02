#dataExplore#File
from . import plt, np, random
from . import seed
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point


class dataExplore(plotSett):

    def drawSetts(self):
        key = sorted(self.sflk)
        key = tuple(key) #hashable
        self.draws[key]()() 
        self.onlyDraw()

        params = iter( self.params.items() )
        for element in self.params.items():
            print( next(params) )


    def noMethod(self):
        print('This method has not been implemented yet!')

    def cantCalculate(self):
        print("It can't be calculated!")

    @property
    def points(self):
        j = 0
        listOfPoints = []

        for u in zip(self.data[0], self.data[1]):
            listOfPoints = listOfPoints + [ point(u[0], u[1], draw = False) ]
            j+=1

        return listOfPoints


    @points.setter
    def points(self, value):
        
        k = self.p%self.dof
        
        self.addParams( "point" + str(k), value )
        self.drawSetts()
        self.p += 1

    def getPoint(self):
        prefix = 'point'
        filtered_dict = {key: val for key, val in self.params.items() if key.startswith(prefix)}
        
        for key, val in filtered_dict.items():
            yield val


    @property
    def integral(self):
        j = 0
        space = ' '
        integral = 0
        init = self.data[0][0]
        for u, v in zip(self.data[0], self.data[1]):
            #to be fixed!"
            integral = integral + (u - init)*v
            init = u
            print(str(j) + space + str(u) + space + str(v) + ' ' + str(integral) )
            j+=1


    #to be fixed
    @property
    def derivative(self):
        j = 0
        space = ' '
        derivative = np.diff(self.data[1])/np.diff(self.data[0])
        for u, v, z in zip(self.data[0][:-1], self.data[1][:-1], derivative):
            
            init = u
            print(str(j) + space + str(u) + space + str(v) + ' ' + str(z) )
            j+=1
    
    @property
    def rotate(self):
        return self._angle
        
    @rotate.setter
    def rotate(self, value):
        self.__del__()
        point = value[0]
        angle = value[1]
        self._angle = angle
        self._rotationPoint = point
        A = np.matrix( [ [ np.cos(angle) , -np.sin(angle) ], [ np.sin(angle) , np.cos(angle) ] ] )
        data0 = self.data[0]
        #self.data[0] = A[0, 0]*(self.data[0] - self._centre.data[0] ) + A[0, 1]*( self.data[1] - self._centre.data[1] ) + self._centre.data[0]
        #self.data[1] = A[1, 0]*(data0 - self._centre.data[0]) + A[1, 1]*( self.data[1] - self._centre.data[1] ) + self._centre.data[1]
        self.data[0] = A[0, 0]*(self.data[0] - point.data[0] ) + A[0, 1]*( self.data[1] - point.data[1] ) + point.data[0]
        self.data[1] = A[1, 0]*(data0 - point.data[0]) + A[1, 1]*( self.data[1] - point.data[1] ) + point.data[1]
        self.onlyDraw()
        
    @property
    def x(self):
        return self.data[0]

    @x.setter
    def x(self, value):
        differences = np.abs( self.data[0] - value)
        #Find the index of the closest element
        closest_index = np.argmin(differences)
        self._cutOff = closest_index
        #get the actual value of the clostest element
        closest_elementx = self.data[0][closest_index]
        closest_elementy = self.data[1][closest_index]
        
        print(closest_index, closest_elementx, closest_elementy )
        
    
    @property
    def y(self):
        return self.data[1]


    @y.setter
    def y(self, value):
        k = self.j%2
        if k==0:
            differences = np.abs( self.data[1] - value)
            #Find the index of the closest element
            closest_index = np.argmin(differences)
            #may be deprecated
            self._cutOff = closest_index
            #get the actual value of the clostest element
            closest_elementx = self.data[0][closest_index]
            closest_elementy = self.data[1][closest_index]
            
            self.j+=1
            print(closest_index, closest_elementx, closest_elementy )
        else:
            self.cutOffdata()
            self.j+=1

    
    #should be deprecated
    @property
    def cut(self):
        class c():
            def __init__(self, outer_instance):
                self.outer_instance = outer_instance
                self.j = 0                
            def x(self, value):
                try:
                    self.outer_instance.x = value.x
                except:
                    self.outer_instance.x = value
                self.outer_instance.cutOffdata()
                self.outer_instance.k+=1

            def y(self, value):
                try:
                    self.outer_instance.y = value.y
                except:
                    self.outer_instance.y = value
                self.outer_instance.cutOffdata()
                self.outer_instance.k+=1

        obj = c(outer_instance = self)
        return obj
    

    def cutOffdata(self):

        if self.k%2 == 0:
            self.data = [arr[self._cutOff:] for arr in self.data]
        else:
            end = len(self.data[1])
            idx = end - self._cutOff
            self.data = [arr[:-idx] for arr in self.data]
        #self.k+=1

        self.__del__()
        self.onlyDraw() 
