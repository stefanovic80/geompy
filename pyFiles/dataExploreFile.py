#dataExploreFile
from . import plt, np, random
from . import seed
from .Settings import settings

from ._plotSettFile import plotSett
from .pointFile import point


class dataExplore(plotSett):
    """
    def __init__(self):
        super.__init__()
        self.attrib = None
    """
    @property
    def points(self):
        j = 0
        listOfPoints = []
        for u in zip(self.data[0], self.data[1]):
            #print(str(j) + ' ' + str(u))
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
            integral = integral + (u- init)*v
            init = u
            print(str(j) + space + str(u) + space + str(v) + ' ' + str(integral) )
            j+=1

    @property
    def x(self):
        return self.data[0]

    @x.setter
    def x(self, value):
        differences = np.abs( self.data[0] - value)
        #Find the index of the closest element
        closest_index = np.argmin(differences)
        #get the actual value of the clostest element
        closest_elementx = self.data[0][closest_index]
        closest_elementy = self.data[1][closest_index]
        
        print(closest_index, closest_elementx, closest_elementy)
         

    @property
    def y(self):
        return self.data[1]


    @y.setter
    def y(self, value):
        differences = np.abs( self.data[1] - value)
        #Find the index of the closest element
        closest_index = np.argmin(differences)
        #get the actual value of the clostest element
        closest_elementx = self.data[0][closest_index]
        closest_elementy = self.data[1][closest_index]

        print(closest_index, closest_elementx, closest_elementy)





    @property
    def cutOff(self):
        return self._cutOff

        #x-----------
        class coordsSel():
            @property
            def x(self):
                return self._cutOff

            @x.setter
            def x(self, xvalue):
                idx = np.where( self.data[0] > xvalue)[0][0]
                self.cutOff = idx

        obj = coordsSel()
        #return obj.x(xvalue)

       #y-----------
        @property
        def y(self):
            return "it's working"

        @y.setter
        def y(self, value):
            #instance._x = value
            # Define the behavior for x here
            print(f"x set to {value}")


        return self._cutOff


    @cutOff.setter
    def cutOff(self, n):
        self._cutOff = n
        self.cut_data()



    def cut_data(self):
        if self._cutOff is not None:
            if self.j%2 == 0:
                self.data = [arr[self._cutOff:] for arr in self.data]
            else:
                self.data = [arr[:-self._cutOff] for arr in self.data]
            self.j += 1
            self.__del__()
            self.onlyDraw() 






