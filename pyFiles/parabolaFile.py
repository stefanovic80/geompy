# parabolaFile.py
from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore
from .parabolaCalcFile import parabolaCalc

class parabola(dataExplore, parabolaCalc):

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
            """
            self.params[None] = None
            self.params['vertex'] = self._vertex
            self.params['a'] = self._a
            """
            self.addParams('None', None)
            self.addParams('vertex', self._vertex)
            self.addParams('a', self._a)

            self.calc()
            self.onlyDraw()
            #self._points_generator()

    @property
    def concavity(self):
        return self._a

    @concavity.setter
    def concavity(self, value):
        self.addParams('a', value) 
        self.params['a'] = self._a = value
    
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self.addParams('a', value)
        self._a = value
        #try:
        self.draw()
        #except:
        #    pass


    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self.addParams('b', value)
        self._b = value
        try:
            self.draw()
        except:
            pass



    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self.addParams('c', value)
        self._c = value
        try:
            self.draw()
        except:
            pass


    @property
    def vertex(self):
        return self._vertex

    @vertex.setter
    def vertex(self, point):
        self.addParams('vertex', point)
        self._vertex = point
        try:
            self.draw()
        except:
            pass
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








    
    def draw(self):
        """ 
        self.__del__()
        prefix = 'point'
        
        #to be fixed
        j = 0
        
        keys = list(self.params.keys())[j:]

        #1) concavity and vertex
        if 'a' in keys and 'vertex' in keys:
            otherKey = next((k for k in self.params if k not in {"vertex", "a"}), None)
            self.params[None] = self.params.pop(otherKey)
            self.params[None] = None
            
            self.calc()
            self.onlyDraw()
        #done


        #3) vertex and one point
        elif 'vertex' in self.params.keys() and any(isinstance(key, str) and key.startswith(prefix) for key in self.params.keys() ):
            
            self.calc4()
            self.onlyDraw()

        #11) vertex, b (self._b)
        elif 'vertex' in self.params.keys() and 'b' in self.params.keys():
            
            otherKey = next((k for k in self.params if k not in {"vertex", "b"}), None)
            self.params[None] = self.params.pop(otherKey)
            self.params[None] = None


            self.calc11()
            self.onlyDraw()

        #12) vertex, c (self._c)
        elif 'vertex' in self.params.keys() and 'c' in self.params.keys():

            otherKey = next((k for k in self.params if k not in {"vertex", "c"}), None)
            self.params[None] = self.params.pop(otherKey)
            self.params[None] = None


            self.calc12()
            self.onlyDraw()

            
        #2) all points
        elif all(isinstance(key, str) and key.startswith("point") for key in self.params.keys() ):
            self.calc2()
            self.onlyDraw()
        
        #4) a, b and c
        elif 'a' in self.params.keys() and 'b' in self.params.keys() and 'c' in self.params.keys():
            self.calc1()
            self.onlyDraw()
        
        #5) c (self._c), point0, point1
        elif 'c' in self.params.keys() and ( sum(1 for key in self.params.keys() if isinstance(key, str) and key.startswith("point")) == 2):
            self.calc5()
            self.onlyDraw()
        
        #6) a (self._a), point0, point1
        elif 'a' in self.params.keys() and ( sum(1 for key in self.params.keys() if isinstance(key, str) and key.startswith("point")) == 2):
            self.calc6()
            self.onlyDraw()

        #7) b (self._b), point0, point1
        elif 'b' in self.params.keys() and ( sum(1 for key in self.params.keys() if isinstance(key, str) and key.startswith("point")) == 2):
            self.calc7()
            self.onlyDraw()

        #8) a (self._a), b (self._b), point0
        elif 'a' in self.params.keys() and 'b' in self.params.keys() and any(isinstance(key, str) and key.startswith(prefix) for key in self.params.keys() ): 
            self.calc8()
            self.onlyDraw()

        #9) a (self._a), c (self._c), point0
        elif 'a' in self.params.keys() and 'c' in self.params.keys() and any(isinstance(key, str) and key.startswith(prefix) for key in self.params.keys() ):
            self.calc9()
            self.onlyDraw()

        #10) b (self._b), c (self._c), point0
        elif 'b' in self.params.keys() and 'c' in self.params.keys() and any(isinstance(key, str) and key.startswith(prefix) for key in self.params.keys() ):
            self.calc10()
            self.onlyDraw()

        else:
            pass
        """
        pass

    def draw(self):
        self.__del__()

        listOfKeys = list( self.params.keys() )
        lpk0, lpk1, lpk2  = listOfKeys[-1], listOfKeys[-2], listOfKeys[-3] #Last Parameter Key, meddle one, first one
        

        if 'point' in lpk0:
            pass

        #if concavity 'a' as last inserted parameter
        elif lpk0 == 'a':
            
            if 'vertex' == lpk1:
                #otherKey = next((k for k in self.params if k not in {"vertex", "a"}), None)
                #self.params[None] = self.params.pop(otherKey)
                #self.params[None] = None
                
                #self.params[lpk2] = None

                self.calc()
                self.onlyDraw()
            elif 'b' == lpk1:
                if 'c' == lpk2:
                    self.calc1()
                    self.onlyDraw()
            elif 'c' == lpk1:
                pass



        #if 'b' as last inserted parameter
        elif lpk0 == 'b':
            pass
        
        #if 'c' as last inserted parameter
        elif lpk0 == 'c':
            pass


        #if 'vertex' as last inserted parameter
        elif lpk0 == 'vertex':
            pass

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93m.a = \033[0m {self._a}\n"
            f"\033[93m.b = \033[0m {self._b}\n"
            f"\033[93m.c = \033[0m {self._c}\n"
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
