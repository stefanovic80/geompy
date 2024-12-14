# parabolaFile.py
from . import plt, np, random
from .Settings import settings
from ._plotSettFile import plotSett
from .pointFile import point
from .dataExploreFile import dataExplore
from .parabolaCalcFile import parabolaCalc

class parabola(dataExplore, parabolaCalc):
    
    dof = 3

    def __init__(self, draw = True, dof = dof):

        super().__init__()
        self._vertex = point( random.uniform(settings.xmin, settings.xmax), random.uniform(settings.ymin, settings.ymax), draw = False  )
        
        self._a = random.uniform(settings.xmin, settings.xmax)**-1#to be checked out!
        self._b = None
        self._c = None
       
        self.j = 0
        self._color = random.choice(self.colors)
        
        #'a'.isupper()
        self.draws = {
                ('a', 'b', 'c'): self.calc_a_b_c,
                ('a', 'b', 'p'): self.calc_a_b_p,
                ('a', 'b', 'v'): self.calc_a_b_v,
                ('a', 'c', 'p'): self.calc_a_c_p,
                ('a', 'c', 'v'): self.calc_a_c_v,
                ('a', 'p', 'p'): self.calc_a_p_p,
                ('a', 'p', 'v'): self.calc_a_p_v,
                ('a', 'v'): self.calc_a_v,
                ('b', 'c', 'p'): self.calc_b_c_p,
                ('b', 'c', 'v'): self.calc_b_c_v,
                ('b', 'p', 'p'): self.calc_b_p_p,
                ('b', 'v'): self.calc_b_v,
                ('c', 'p', 'p'): self.calc_c_p_p,
                ('c', 'v'): self.calc_c_v,
                ('p', 'p', 'p'): self.calc_p_p_p,
                ('p', 'v'): self.calc_p_v,
                }

        if draw == True:
            self.addParams('vertex', self._vertex)
            self.addParams('a', self._a)
            self.drawSetts()

    @property
    def concavity(self):
        return self._a


    @concavity.setter
    def concavity(self, value):
        self.addParams('a', value) 
        self.params['a'] = self._a = value
        self.drawSetts()

    @property
    def a(self):
        return self._a


    @a.setter
    def a(self, value):
        self.addParams('a', value)
        self._a = value
        self.drawSetts()


    @property
    def b(self):
        return self._b


    @b.setter
    def b(self, value):
        self.addParams('b', value)
        self._b = value
        self.drawSetts()


    @property
    def c(self):
        return self._c


    @c.setter
    def c(self, value):
        self.addParams('c', value)
        self._c = value
        self.drawSetts()


    @property
    def vertex(self):
        return self._vertex


    @vertex.setter
    def vertex(self, point):
        self.addParams('vertex', point)
        self._vertex = point
        self.drawSetts()


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
