#dataExploreFile
from . import plt, np, random
from . import seed
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point


class dataExplore(plotSett):
    
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
        self.erase()
        self._points = self._points + [ value ]
        try:
            self.draw()
        except:
            pass


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

    #to be deprecated
    @property
    def cutOff(self):
        self.cutOffdata()
    
    #to be deprecated
    @cutOff.setter
    def cutOff(self, n):
        if n == False:
            self.j = 0
            self._cutOff = 0
            #to be fixed!
        elif not isinstance(n, bool):
            self._cutOff = n
        else:
            pass
        
        self.cutOffdata()

    def cutOffdata(self):

        if self.k%2 == 0:
            self.data = [arr[self._cutOff:] for arr in self.data]
        else:
            end = len(self.data[1])
            idx = end - self._cutOff
            self.data = [arr[:-idx] for arr in self.data]
        self.k+=1

        self.__del__()
        self.onlyDraw() 

