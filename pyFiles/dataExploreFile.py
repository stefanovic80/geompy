#dataExplore#File
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
        
        #q = self.degreesOfFreedom
        #k = (self.p+q-1)%q
        k = self.p%2
        #self._points = self._points + [ value ]
        
        
        self.addParams( "point" + str(k), value )
        self.draw()
        self.p += 1
        """
        try:
            self.draw()
        except:
            pass
        """
    
    def _points_generator(self):
        #self._points = [None, None, None]
        self._points = [None for u in range(self.degreesOfFreedom)]
        for j in range(self.degreesOfFreedom - 1):
            random_idx = random.randint(0, len(self.data[0]) -1)
            x = self.data[0][random_idx]
            y = self.data[1][random_idx]
            self._points[j] = point(x, y, draw = False)

    def getPoint(self):
        prefix = 'point'
        for key, val in self.params.items():
            if key.startswith(prefix):
                yield val#ontsTuple
            else:
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
