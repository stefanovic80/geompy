# parabolaFile.py
from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore

class parabola(dataExplore):

    def __init__(self, draw = True):

        super().__init__()
        self._vertex = point( random.uniform(settings.xmin, settings.xmax), random.uniform(settings.ymin, settings.ymax), draw = False  )
        #self.concavity = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        
        
        self._a = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        self._b = None
        self._c = None
       
        self.j = 0
        self._color = random.choice(self.colors)

        self.degreesOfFreedom = 3
        self.dof = 3
        if draw == True:
            self.params['vertex'] = self._vertex
            self.params['a'] = self._a
            self.calc()
            self.onlyDraw()
            #self._points_generator()

    @property
    def concavity(self):
        return self._a

    @concavity.setter
    def concavity(self, value):
        self.params['a'] = self._a = value
        #self.chooseCalc()
        #self.onlyDraw()
    
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = self.params['a'] = value
        try:
            self.draw()
        except:
            pass


    @property
    def b(self):
        return self._b

    @a.setter
    def b(self, value):
        self._b = self.params['b'] = value
        try:
            self.draw()
        except:
            pass



    @property
    def c(self):
        return self._c

    @a.setter
    def c(self, value):
        self._c = self.params['c'] = value
        try:
            self.draw()
        except:
            pass




    @property
    def vertex(self):
        return self._vertex

    @vertex.setter
    def vertex(self, point):
        self.params['vertex'] = self._vertex = point
        #self.chooseCalc()
        #self.name = self._name





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

        if self._b > 0:
            signb = '+'
        elif self._b <0:
            signb = '-'

        if self._c > 0:
            signc = '+'
        elif self._c <0:
            signc = '-'



        a = str(round(self._a, 2))
        b = str(abs(round(self._b, 2)))
        c = str(abs(round(self._c, 2)))
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
        self._a = None
        self.data = [None, None]



    def calc(self, name = None):
        self.data = [ self._x ]
        self.data = self.data + [self._a*(self._x - self._vertex.coords[0])**2 + self._vertex.coords[1] ]


    # calculate from three points the parabola passing through (to be fixed!)
    def calc2(self, name = None):

        u = self.getPoint()
        point0 = next(u)
        point1 = next(u)
        point2 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        x1, y1 = point1.coords[0], point1.coords[1]
        x2, y2 = point2.coords[0], point2.coords[1]
        
        A = np.matrix([ [ x0**2, x0, 1  ], [ x1**2, x1, 1  ], [ x2**2, x2, 1  ] ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ y0  , y1  , y2 ] )#.reshape(-1, 1)
        parabParams = np.dot(Ainv, y)
        
        self._a = parabParams[0, 0]
        self._b = parabParams[0, 1]
        self._c = parabParams[0, 2]
        
        self.calc1() 
    
    #one point and vertex. To be debugged!
    def calc4(self, name = None):

        u = self.getPoint()
        point0 = next(u)
        x0, y0 = point0.coords[0], point0.coords[1]
        xv, yv = self._vertex.coords[0], self._vertex.coords[1]

        A = np.matrix([ [ -xv**2, 1  ], [ x0*(x0 - 2*xv), 1]  ])
        Ainv = np.linalg.inv(A)
        y = np.array( [ yv, y0 ])
        parabParams = np.dot(Ainv, y)

        self._a = parabParams[0, 0]
        self._c = parabParams[0, 1]
        self._b = -2*self._a*xv

        self.calc1()

    #what is this?
    def calc1(self, name = None):

        Delta = self._b**2 - 4*self._a*self._c
        self._vertex = point( -self._b/(2*self._a)  , -Delta/(4*self._a),  draw = False )
        #self.concavity = self._a
        self.calc()

    """
    def chooseCalc(self):
        self.__del__()

        calculation_functions = [self.calc2, self.calc1, self.calc]#, self.calc3]

        for calc_function in calculation_functions:
            if self.rotate == False:
                try:
                    self.lims()
                    calc_function()
                    break
                except:
                    pass
    """

    def draw(self):
        self.__del__()
        prefix = 'point'
        
        #1) concavity and vertex
        if 'a' in self.params.keys() and 'vertex' in self.params.keys():
            self.calc()
            self.onlyDraw()
        
        #2) all points
        elif all(isinstance(key, str) and key.startswith("point") for key in self.params.keys() ):
            self.calc2()
            self.onlyDraw()
        
        #3) vertex and one point
        elif 'vertex' in self.params.keys() and any(isinstance(key, str) and key.startswith(prefix) for key in self.params.keys() ):
            self.calc4()
            self.onlyDraw()
        #4) a, b and c
        elif 'a' in self.params.keys() and 'b' in self.params.keys() and 'c' in self.params.keys():
            self.calc1()
            self.onlyDraw()
        else:
            pass


    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93m.vertex.x = \033[0m {self._vertex.data[0]}\n"
            f"\033[93m.vertex.y = \033[0m {self._vertex.data[1]}\n"
            f"\033[93m.concavity = \033[0m {self._a}\n"
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
