# _plotSett.py
from . import plt, np, random
from .Settings import settings

# to be removed in case of coding
plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 18
plt.rcParams [ 'figure.figsize' ] = ( 9 , 9)
plt.rcParams [ 'font.size' ] = 10
plt.rcParams [ 'font.weight'] = 'bold'



def first_non_zero_digit(num):
    num_str = str(num)
    for char in num_str:
        if char != '0' and char != '.':
            return char
    return None  # Return None if all digits are zero


class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()
    
    def __init__(self):

        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'm', 'magenta', 'k', 'black', settings.azure]
        self._linewidth = settings.linewidth
        self.plotSettings = None

        self.data = [None, None]
        self.tex = [None, None]  # label text
        #density of grid
        
        self.hline = None
        self.vline = None

        plt.rcParams [ 'lines.linewidth' ] = self._linewidth
        
        #it may be better to use settings.attributes instead
        #------------------------
        self.xMin = settings.xmin
        self.xMax = settings.xmax

        self.yMin = settings.ymin
        self.yMax = settings.ymax
        #------------------------

        self.lims()

        self.rotate = False
        self._name = None
        self._points = []

        self._majorStep = 2#2#None

        #used in cutOff method
        self.j = 0
        self._cutOff = 0

    @property
    def gridReset(self):
        self.left = -10
        self.right = 10
        self.majorStep = 2
        self.minorSteps = 10


    @property
    def left(self):
        return self.xMin

    @left.setter
    def left(self, value):
        settings.xmin = value
        settings.ymin = value
        self.xMin = value
        self.yMin = value
        self.majorStep = self._majorStep
        self.lims()
        #self.draw()

    @property
    def right(self):
        return self.xMax

    @right.setter
    def right(self, value):
        settings.xmax = value
        settings.ymax = value
        self.xMax = value
        self.yMax = value
        self.majorStep = self._majorStep
        #self.minorSteps = 10
        self.lims()
        #self.draw()

    @property
    def bottom(self):
        return self.yMin

    @bottom.setter
    def bottom(self, value):
        settings.ymin = value
        self.yMin = value
        self.grid( bottomConcat = value, topConcat = self.yMax )
        self.ax.set_ylim( bottom = value )
        self._y = np.linspace(self.yMin, self.yMax, settings.steps)



    @property
    def up(self):
        return self.yMax

    @up.setter
    def up(self, value):
        settings.ymax = value
        self.yMax = value
        self.grid(topConcat = value, bottomConcat = self.yMin)
        self.ax.set_ylim( top = value )
        self._y = np.linspace(self.yMin, self.yMax, settings.steps)
    

    @property
    def color(self):
        return self._color
        

    @color.setter
    def color(self, c):
        if c in self.colors:
            self._color = c
            self.onlyDraw()
            #self.draw()
            self.label(self._name)
        elif c == "azure":
            self.color = settings.azure
        else:
            pass



    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        self.onlyDraw()
        #self.draw()
        self.label( n )
    
    @property
    def linewidth(self):
        return self._linewidth

    @linewidth.setter
    def linewidth(self, n):
        self._linewidth = n
        self.onlyDraw()
        #self.draw()


    @property
    def majorStep(self):
        return self.majorStep

    @majorStep.setter
    def majorStep(self, value):
        self._majorStep = value
        self.grid(majorStep = self._majorStep, bottomConcat = self.yMin, topConcat = self.yMax )

    @property
    def minorSteps(self):
            return self._minorSteps

    @minorSteps.setter
    def minorSteps(self, value):
        self._minorSteps = value
        self.grid(majorStep = self._majorStep, minorSteps = value, bottomConcat = self.yMin, topConcat = self.yMax)


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
    def points(self):
        j = 0
        for u in zip(self.data[0], self.data[1]):
            print(str(j) + ' ' + str(u))
            j+=1

    @points.setter
    def points(self, value):
        self.erase()
        self._points = self._points + [ value ]
        try:
            self.draw()
        except:
            pass


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


        """
        @x.setter
        def x(self, value):
            #instance = value
            # Define the behavior for x here
            print(f"x set to {value}")
        """

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


    def label(self, name):
        try:
            self.tex.remove()
        except:
            pass

        if isinstance(name, str):
            self._name = name

        idx = self.condition_mask()
        data = [self.data[0][idx], self.data[1][idx] ]

        random_index = np.random.randint(len(data[0]))
        shift = (self.xMax - self.xMin)/40
        labelx = data[0][random_index] + shift
        labely = data[1][random_index] + shift
        
        #labelx, labely may necessitte to be attributes
        self.tex = self.ax.text(labelx, labely, self._name, fontsize = 12, color = self._color, ha="center", va="center")



    def draw(self):
        #self.lims()
        self.chooseCalc()
        self.onlyDraw()

    def onlyDraw(self):
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        
        #to check!
        self.lines = []
        self.lines.append(line)

       
    def condition_mask(self):

        condition_mask0 = ( self.data[0] > self.xMin) & (self.data[0] < self.xMax)
        condition_mask1 = ( self.data[1] > self.yMin) & (self.data[1] < self.yMax)
        condition_mask = condition_mask0 & condition_mask1
        return np.where(condition_mask)
        


    def lims(self):
        self._x = np.linspace(self.xMin, self.xMax, settings.steps)
        self._y = np.linspace(self.yMin, self.yMax, settings.steps)
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)
        
        
    def grid(self, majorStep = 2, minorSteps = 10, topConcat = settings.xmax, bottomConcat = settings.xmin):

        #if majorStep == None:
        #    majorStep = 2
        #else:
        #    pass
        
        minorStep = majorStep / minorSteps
        
        
        #x grid---------------------------------------
        if (self.xMin < 0) and (self.xMax > 0):
            #------------ minor ticks
            Xminor_ticksPos = np.arange(0, self.xMax, minorStep)
            Xminor_ticksNeg = np.arange(0, self.xMin, -minorStep)[::-1]

            Xminor_ticks = np.append(Xminor_ticksNeg, Xminor_ticksPos)
            
            #----------- major ticks
            Xmajor_ticksPos = np.arange(0, self.xMax, majorStep)

            Xmajor_ticksNeg = np.arange(0, self.xMin, -majorStep)[::-1]

            Xmajor_ticks = np.append(Xmajor_ticksNeg, Xmajor_ticksPos)

            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')


        else:
            Xminor_ticks = np.arange(self.xMin, self.xMax, minorStep)
        
            Xmajor_ticks = np.arange(self.xMin, self.xMax, majorStep)

        self.ax.set_xticks(Xminor_ticks, minor = True)
        self.ax.set_xticks(Xmajor_ticks) # minor = False can be neglected

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.vline = self.ax.axvline(0, color = 'k', linewidth = self._linewidth)

        #y grid---------------------------------------
        topArrayMinor = np.arange(self.xMax, topConcat, minorStep)
        
        topArrayMajor = np.arange(self.xMax, topConcat, majorStep)

        bottomArrayMinor = np.arange( bottomConcat, self.xMin, minorStep)

        bottomArrayMajor = np.arange( bottomConcat, self.xMin, majorStep)



        Yminor_ticks = np.concatenate((bottomArrayMinor, Xminor_ticks, topArrayMinor))

        Ymajor_ticks = np.concatenate((bottomArrayMajor, Xmajor_ticks, topArrayMajor))

        
        self.ax.set_yticks(Yminor_ticks, minor=True)
        self.ax.set_yticks(Ymajor_ticks)
        

        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.6)
        

        # alpha stands for transparency: 0 transparent, 1 opaque
        self.hline = self.ax.axhline(0, color = 'k', linewidth = self._linewidth)    
    

    def __del__(self):
        try:#removes all lines
            for line in self.lines:
                line.remove()
        except:
            pass

        try:#removes all geometrical locus points
            for u in self.point:
                u.remove()
        except:
            pass

        try:#removes point texts
            self.tex.remove()
        except:
            pass
        

    def __str__(self):
        self.plotSettings = (
            f"\nSettings:\n"
            f"\033[93m.xmin = \033[0m {settings.xmin}\n"
            f"\033[93m.xmax = \033[0m {settings.xmax}\n"
            f"\033[93m.steps = \033[0m {settings.steps}\n"
            f"\033[93m._x = \033[0m {self._x[:10]}...\n"
        )
