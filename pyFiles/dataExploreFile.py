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
    def X(self):

        class c():
            def __init__(self, outer_instance):
                self.outer_instance = outer_instance

            @property
            def lower(self):
                return settings.xmin
            @lower.setter
            def lower(self, value):
                settings.xmin = value
                #to be fixed
                #self.outer_instance.limsx()
                #self.outer_instance.grid_y()
                
                self.outer_instance.ax.set_xlim( bottom = value)
                self.outer_instance.grid_x(bottomConcat = settings.xmin, topConcat = settings.xmax)
            
            @property
            def higher(self):
                return settings.xmax
            @higher.setter
            def higher(self, value):
                settings.xmax = value
                #to be fixed
                #self.outer_instance.limsx()
                
                self.outer_instance.ax.set_xlim( top = value)
                self.outer_instance.grid_x(topConcat = settings.xmax, bottomConcat = settings.xmin)

            @property
            def data(self):
                return self.outer_instance.data[0]

            @data.setter
            def data(self, value):
                self.outer_instance.data[0] = value
                self.outer_instance.__del__()
                self.outer_instance.onlyDraw()
        

            @property
            def majorStep(self):
                return self.outer_instance.majorStep
            
            @majorStep.setter
            def majorStep(self, value):
                #self._majorStep = value
                self.outer_instance.grid_x(majorStep = value, bottomConcat = settings.xmin, topConcat = settings.xmax )

            @property
            def minorSteps(self):
                return self.outer_instance._minorSteps
            
            @minorSteps.setter
            def minorSteps(self, value):
                #self._minorSteps = value
                self.outer_instance.grid_x(majorStep = self.outer_instance._majorStep, minorSteps = value, bottomConcat = settings.xmin, topConcat = settings.xmax)


        obj = c(outer_instance = self)

        return obj






    @property
    def Y(self):
        
        class c():
            def __init__(self, outer_instance):
                self.outer_instance = outer_instance
                
            @property
            def lower(self):
                return settings.ymin
            @lower.setter
            def lower(self, value):
                settings.ymin = value
                #to be fixed
                #self.outer_instance.limsy()
                
                self.outer_instance.ax.set_ylim( bottom = value)

                #self.outer_instance.grid_y()
                self.outer_instance.grid_y(bottomConcat = settings.ymin, topConcat = settings.ymax)
                
            @property
            def higher(self):
                return settings.ymax
            @higher.setter
            def higher(self, value):
                settings.ymax = value
                #may be removed
                #self.outer_instance.limsy()
                
                self.outer_instance.ax.set_ylim( top = value)
                #to be fixed!
                self.outer_instance.grid_y(topConcat = value, bottomConcat = settings.ymin)
            
            @property
            def data(self):
                return self.outer_instance.data[1]
            
            @data.setter
            def data(self, value):
                self.outer_instance.data[1] = value
                self.outer_instance.__del__()
                self.outer_instance.onlyDraw()

            @property
            def majorStep(self):
                return self.outer_instance.majorStep

            @majorStep.setter
            def majorStep(self, value):
                #self._majorStep = value
                self.outer_instance.grid_y(majorStep = value, bottomConcat = settings.ymin, topConcat = settings.ymax )

            @property
            def minorSteps(self):
                #to be fixed
                return self.outer_instance._minorSteps

            @minorSteps.setter
            def minorSteps(self, value):
                #self._minorSteps = value
                self.outer_instance.grid_y(majorStep = self.outer_instance._majorStep, minorSteps = value, bottomConcat = settings.ymin, topConcat = settings.ymax)



        obj = c(outer_instance = self)
        
        return obj


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

            #def point(self, value):
            #    self.x(value = self.outer_instance.x)

        obj = c(outer_instance = self)
        #obj.cut.x(5)
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
