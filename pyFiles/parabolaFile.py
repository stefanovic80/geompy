# parabolaFile.py
from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore

class parabola(dataExplore):

    def __init__(self, draw = True):

        super().__init__()
        self._vertex = point( random.uniform(settings.xmin, settings.xmax), random.uniform(settings.xmin, settings.xmax), draw = False  )
        #self.concavity = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        
        
        self.a = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        self.b = None
        self.c = None
       
        self.j = 0
        self._color = random.choice(self.colors)


        if draw == True:
            self.draw()

    @property
    def concavity(self):
        return self.a

    @concavity.setter
    def concavity(self, value):
        self.a = value
        self.chooseCalc()
        self.onlyDraw()

    @property
    def vertex(self):
        return self._vertex

    @vertex.setter
    def vertex(self, point):
        self._vertex = point
        self.chooseCalc()
        self.name = self._name

    @property
    def equation(self):
        #to be inherited
        try:
            self.tex.remove()
        except:
            pass

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]
        random_index = np.random.randint(len(data[0]))
        shift = (settings.xmax - settings.xmin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        #--------------------

        if self.b > 0:
            signb = '+'
        elif self.b <0:
            signb = '-'

        if self.c > 0:
            signc = '+'
        elif self.c <0:
            signc = '-'



        a = str(round(self.a, 2))
        b = str(abs(round(self.b, 2)))
        c = str(abs(round(self.c, 2)))
        eq = "y = " + a + r"$x^2$" + signb + b + "x" + signc + c
        try:
            eq = self._name + ": " + eq
        except:
            pass
        #labelx, labely may necessitte to be attributes
        if self.j%2 == 0:
            self.tex = self.ax.text(labelx, labely, eq, fontsize = 12, color = self._color, ha="center", va="center")
        self.j += 1


    #to be partially inherited
    def erase(self):
        self.__del__()
        
        #self._points = [] may have to be moved into _plotSett
        self._vertex = None
        self.a = None
        self.data = [None, None]



    def calc(self, name = None):
        self.data = [ self._x ]
        self.data = self.data + [self.a*(self._x - self._vertex.coords[0])**2 + self._vertex.coords[1] ]


    # calculate from three points the parabola passing through (to be fixed!)
    def calc2(self, name = None):
        x0 = self._points[0].coords[0]
        x1 = self._points[1].coords[0]
        x2 = self._points[2].coords[0]

        y0 = self._points[0].coords[1]
        y1 = self._points[1].coords[1]
        y2 = self._points[2].coords[1]

        A = np.matrix([ [ x0**2, x0, 1  ], [ x1**2, x1, 1  ], [ x2**2, x2, 1  ] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ y0  , y1  , y2 ] )#.reshape(-1, 1)
        parabParams = np.dot(Ainv, y)
        
        self.a = parabParams[0, 0]
        self.b = parabParams[0, 1]
        self.c = parabParams[0, 2]
        
        self.calc1() 
    
    #what is this?
    def calc1(self, name = None):

        Delta = self.b**2 - 4*self.a*self.c
        self._vertex = point( -self.b/(2*self.a)  , -Delta/(4*self.a),  draw = False )
        #self.concavity = self.a
        self.calc()



    def chooseCalc(self):
        self.__del__()

        calculation_functions = [self.calc, self.calc1, self.calc2]#, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    self.lims()
                    calc_function()
                    break
                except:
                    pass


    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93m.vertex.x = \033[0m {self._vertex.data[0]}\n"
            f"\033[93m.vertex.y = \033[0m {self._vertex.data[1]}\n"
            f"\033[93m.concavity = \033[0m {self.a}\n"
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            #f"\033[93m.data[0] =\033[0m {self.data[0]}\n"
            #f"\033[93m.data[1] =\033[0m {self.data[1]}\n"
            f"\033[93m.name:\033[0m {self._name}\n"
            f"\033[93m.color:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings
