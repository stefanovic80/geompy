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
        
        self._a = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        self._b = None
        self._c = None
       
        self.j = 0
        self._color = random.choice(self.colors)

        self.degreesOfFreedom = 3
        self.dof = 3
        if draw == True:
            self.addParams('vertex', self._vertex)
            self.addParams('a', self._a)

            self.calc_a_v()
            self.onlyDraw()


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
        self.draw_a()


    @property
    def b(self):
        return self._b


    @b.setter
    def b(self, value):
        self.addParams('b', value)
        self._b = value
        self.draw_b()


    @property
    def c(self):
        return self._c


    @c.setter
    def c(self, value):
        self.addParams('c', value)
        self._c = value
        self.draw_c()


    @property
    def vertex(self):
        return self._vertex


    @vertex.setter
    def vertex(self, point):
        self.addParams('vertex', point)
        self._vertex = point
        self.draw_vertex()


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
        
        self._vertex = None
        self._a = None
        self.data = [None, None]


    def draw_a(self):
        self.__del__()

        listOfKeys = list( self.params.keys() )
        lpk0, lpk1 = listOfKeys[-1], listOfKeys[-2] #Last Parameter Key, meddle one, first one
        try:
            lpk2 = listOfKeys[-3]
        except:
            pass
        
        #a_b_c
        if 'b' in listOfKeys and 'c' in listOfKeys:
            self.calc_a_b_c()
            self.onlyDraw()
        
        #a_c_p
        elif 'c' in listOfKeys and any('point' in key for key in listOfKeys):
            self.calc_a_c_p()
            self.onlyDraw()

        #a_v
        elif 'vertex' == lpk1:
            self.calc_a_v()
            self.onlyDraw()
        
        #a_p_p
        elif 'point' in lpk1 and 'point' in lpk2:
            self.calc_a_p_p()
            self.onlyDraw()

        #a_c_p
        elif 'c' in listOfKeys and any('point' in key for key in listOfKeys):
            self.calc_a_c_p()
            self.onlyDraw()
        
        #a_b_v
        elif 'b' in listOfKeys[:-1] and 'v' in listOfKeys[:-1]:
            self.calc_a_b_v()
            self.onlyDraw()

        #a_p_v
        elif vertex in listOfKeys[:-1] and any('point' in key for key in listOfKeys[:-1]):
            self.calc_a_p_v()
            self.onlyDraw()

        print(self.params)


    def draw_b(self):
        self.__del__()

        listOfKeys = list( self.params.keys() )
        lpk1, lpk2  = listOfKeys[-2], listOfKeys[-3] #Last Parameter Key, meddle one, first one

        #b_v
        if 'vertex' == lpk1:
            self.calc_b_v()
            self.onlyDraw()
        
        #a_b_c
        elif 'a' in listOfKeys and 'c' in listOfKeys:
            self.calc_a_b_c()
            self.onlyDraw()
        
        #a_b_p
        elif 'a' in listOfKeys and any( 'point' in key for key in listOfKeys):
            self.calc_a_b_p()
            self.onlyDraw()
        
        #a_c_p
        elif 'c' in listOfKeys and any( 'point' in key for key in listOfKeys ):
            self.calc_b_c_p()
            self.onlyDraw()
        
        #a_b_v
        elif 'a' in listOfKeys[:-1] and 'vertex' in listOfKeys[:-1]:
            self.calc_a_b_v()
            self.onlyDraw()
        
        print(self.params)


    def draw_c(self):
        self.__del__()

        listOfKeys = list( self.params.keys() )
        lpk1, lpk2  = listOfKeys[-2], listOfKeys[-3] #Last Parameter Key, meddle one, first one
        
        #c_v
        if 'vertex' == lpk1:
            self.calc_c_v()
            self.onlyDraw()
        
        #a_b_c
        elif 'a' in listOfKeys and 'b' in listOfKeys:
            self.calc_a_b_c()
            self.onlyDraw()
        
        #a_b_p
        elif 'b' in listOfKeys and any( 'point' in key for key in listOfKeys ):
            self.calc_b_c_p()
            self.onlyDraw()
        
        #a_c_p
        elif 'a' in listOfKeys and any( 'point' in key for key in listOfKeys ):
            self.calc_a_c_p()
            self.onlyDraw()
        
        #c_p_p
        elif 'point' in listOfKeys[-2] and 'point' in listOfKeys[-3]:
            self.calc_c_p_p()
            self.onlyDraw()
        
        #a_c_v
        elif 'a' in listOfKeys[:-1] and 'vertex' in listOfKeys[:-1]:
            self.calc_a_c_v()
            self.onlyDraw()
        
        print(self.params)


    def draw_vertex(self):
        self.__del__()

        listOfKeys = list( self.params.keys() )
        lpk1 = listOfKeys[-2] #Last Parameter Key, meddle one, first one
        
        #a_v
        if lpk1 == 'a':
            self.calc_a_v()
            self.onlyDraw()
        
        #p_v
        elif 'point' in lpk1:
            self.calc_p_v()
            self.onlyDraw()
        
        #b_p_v
        elif 'b' in lpk1 and 'vertex' in listOfKeys[:-1]:
            self.calc_b_v()
            self.onlyDraw()
        
        #c_v
        elif 'c' in lpk1:
            self.calc_c_v()
            self.onlyDraw()

        #a_b_v
        elif 'a' in listOfKeys[:-1] and 'b' in listOfKeys[:-1]:
            self.calc_a_b_v()
            self.onlyDraw()

    def draw(self):
        self.__del__()
        
        listOfKeys = list( self.params.keys() )
        lpk1, lpk2  = listOfKeys[-2], listOfKeys[-3] #Last Parameter Key, meddle one, first one
        
        if 'point' in lpk1 and 'point' in lpk2:
            self.calc_p_p_p()
            self.onlyDraw()
        elif 'b' in listOfKeys and 'c' in listOfKeys:
            self.calc_b_c_p()
            self.onlyDraw()

        elif 'a' in listOfKeys and 'c' in listOfKeys:
            self.calc_a_c_p()
            self.onlyDraw()

        elif 'a' in listOfKeys and 'b' in listOfKeys:
            self.calc_a_b_p()
            self.onlyDraw()

        elif 'a' in listOfKeys and 'vertex' in listOfKeys:
            self.calc_a_p_v()
            self.onlyDraw()

        elif 'a' in listOfKeys and any( 'point' in key for key in listOfKeys[:-1] ):
            self.calc_a_p_p()
            self.onlyDraw()

        elif 'b' in listOfKeys and any( 'point' in key for key in listOfKeys[:-1] ):
            self.calc_b_p_p()
            self.onlyDraw()

        elif 'c' in listOfKeys and any( 'point' in key for key in listOfKeys[:-1] ):
            self.calc_c_p_p()
            self.onlyDraw()


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
            f"\033[93m.data[0] = \033[0m {self.data[0][:10]}...\n"
            f"\033[93m.data[1] = \033[0m {self.data[1][:10]}...\n"
            f"\033[93m.name:\033[0m {self._name}\n"
            f"\033[93m.color:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.erase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings
