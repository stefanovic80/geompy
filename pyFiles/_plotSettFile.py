# _plotSett.py
from . import plt, np, random
from .Settings import settings
from collections import deque

import sys
# to be removed in case of coding

def is_interactive():
    "check if code is working in interactive mode!"
    return hasattr(sys, "ps1")

if is_interactive():
    pass
    #plt.ion()

plt.ion()

plt.rcParams [ 'axes.labelsize' ] = 12
plt.rcParams [ 'figure.figsize' ] = ( settings.window_width , settings.window_width*settings.window_height/settings.window_width)
plt.rcParams [ 'font.size' ] = 12
plt.rcParams [ 'font.weight'] = 'bold'

#x = np.arange(-10, 10, 0.01)

#plt.gca().lines[-1].remove()

class plotSett():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()
    
    dof = 3

    def __init__(self, dof = dof):

        self.colors = colors = ['b', 'blue', 'g', 'green', 'r', 'red', 'm', 'magenta', 'k', 'black', settings.azure]
        self._linewidth = settings.linewidth
        self.plotSettings = None

        #self.data = [None, None] 
        self.data = [[], []]

        self.params = {}
        self.keys = deque(maxlen = dof)
        self.values = deque(maxlen = dof)

        self.hline = None
        self.vline = None

        plt.rcParams [ 'lines.linewidth' ] = self._linewidth

        #to be deprecated
        self.lims()
        
        self._name = None

        self._step = 2
        self._stepx = 2
        self._stepy = 2

        self._steps = 10
        self._stepsx = 10
        self._stepsy = 10
        
        #to be removed
        self.p = 0
        self.j = 0
        self.k = 0        
        self.lines = []

        self.sflk = None#deque(maxlen = self.dof) #Sorted First Letter Key
	        
        #to be implemented as .X.cut doesn't work on function
        self._cutOff = 0

	    #to be deprecated
        self.labCoords = [None, None]


    @property
    def lower(self):
	    return settings.xmin
		
    @lower.setter
    def lower(self, value):
        settings.xmin = value
        settings.ymin = value*settings.window_height/settings.window_width
        self.step = self._step
        self.grid_x()
        self.grid_y()
        self.lims()
        

    @property
    def higher(self):
        return settings.xmax

    @higher.setter
    def higher(self, value):
        settings.xmax = value
        settings.ymax = value*settings.window_height/settings.window_width
        self.step = self._step
        self.grid_x()
        self.grid_y()
        self.lims()


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

                self.outer_instance.ax.set_xlim( left = value)
                self.outer_instance.grid_x(bottomConcat = settings.xmin, topConcat = settings.xmax, step = self.outer_instance._stepx)

            @property
            def higher(self):
                return settings.xmax
            @higher.setter
            def higher(self, value):
                settings.xmax = value

                self.outer_instance.ax.set_xlim( right = value)
                self.outer_instance.grid_x(topConcat = settings.xmax, bottomConcat = settings.xmin, step = self.outer_instance._stepx)

            @property
            def data(self):
                return self.outer_instance.data[0]

            @data.setter
            def data(self, value):
                self.outer_instance.data[0] = value
                self.outer_instance.__del__()
                self.outer_instance.onlyDraw()


            @property
            def step(self):
                return self.outer_instance._stepx

            @step.setter
            def step(self, value):
                self.outer_instance._stepx = value
                self.outer_instance.grid_x(step = value, bottomConcat = settings.xmin, topConcat = settings.xmax )

            @property
            def steps(self):
                return self.outer_instance._stepsx

            @steps.setter
            def steps(self, value):
                self.outer_instance._stepsx = value
                self.outer_instance.grid_x(step = self.outer_instance._stepx, steps = value, bottomConcat = settings.xmin, topConcat = settings.xmax)
            
            @property
            def cut(self):
                #Bug: self.outer_instance.xmin and .xmax don't exist anymore!
                return self.outer_instance.xmin, self.outer_instance.xmax

            @cut.setter
            def cut(self, value):
                try:
                    self.outer_instance.x = value.x
                except:
                    self.outer_instance.x = value
                self.outer_instance.cutOffdata()
                self.outer_instance.k += 1

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
                
                self.outer_instance.ax.set_ylim( bottom = value)

                #self.outer_instance.grid_y()
                self.outer_instance.grid_y(bottomConcat = settings.ymin, topConcat = settings.ymax, step = self.outer_instance._stepy)
                
            @property
            def higher(self):
                return settings.ymax
            @higher.setter
            def higher(self, value):
                settings.ymax = value
                
                self.outer_instance.ax.set_ylim( top = value)
                #to be fixed!
                self.outer_instance.grid_y(bottomConcat = settings.ymin, topConcat = value, step = self.outer_instance._stepy)
                #self.outer_instance.grid_y(topConcat = value, bottomConcat = settings.ymin, self.outer_instance._majorStepy)
            
            @property
            def data(self):
                return self.outer_instance.data[1]
            
            @data.setter
            def data(self, value):
                self.outer_instance.data[1] = value
                self.outer_instance.__del__()
                self.outer_instance.onlyDraw()

            @property
            def step(self):
                return self.outer_instance._stepy

            @step.setter
            def step(self, value):
                self.outer_instance._stepy = value
                self.outer_instance.grid_y(step = value, bottomConcat = settings.ymin, topConcat = settings.ymax )

            @property
            def steps(self):
                #to be fixed
                return self.outer_instance._stepsy

            @steps.setter
            def steps(self, value):
                self.outer_instance._stepsy = value
                self.outer_instance.grid_y(step = self.outer_instance._stepy, steps = value, bottomConcat = settings.ymin, topConcat = settings.ymax)



        obj = c(outer_instance = self)
        
        return obj


    @property
    def color(self):
        return self._color
        

    @color.setter
    def color(self, c):
        if c in self.colors:
            self._color = c
            self.__del__()
            self.onlyDraw()
            self.label(self._name)
        elif c == "azure":
            self.color = settings.azure
        else:
            pass


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        self.__del__()
        self.onlyDraw()
        self.label(n)
    
    @property
    def linewidth(self):
        return self._linewidth

    @linewidth.setter
    def linewidth(self, n):
        self._linewidth = n
        self.__del__()
        self.onlyDraw()


    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
        self.grid_x(step = self._step, bottomConcat = settings.xmin, topConcat = settings.xmax )
        self.grid_y(step = self._step, bottomConcat = settings.ymin, topConcat = settings.ymax )

    @property
    def steps(self):
            return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value
        self.grid_x(step = self._step, steps = value, bottomConcat = settings.xmin, topConcat = settings.xmax)
        self.grid_y(step = self._step, steps = value, bottomConcat = settings.ymin, topConcat = settings.ymax)


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
        shift = (settings.xmax - settings.xmin)/40

        self.labCoords[0] = data[0][random_index] + shift
        self.labCoords[1] = data[1][random_index] + shift
        
        text = self.ax.text(self.labCoords[0], self.labCoords[1], self._name, fontsize = 12, color = self._color, ha="center", va="center")
        self.lines.append(text)

    def addParams(self, key, param):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(param)

        elif key in self.keys:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.values[idx]

            self.keys.append(key)
            self.values.append(param)

        self.params = dict(zip(self.keys, self.values))
        self.sflk = [ k[:2] for k in self.params.keys() ]       
    

    #to be deprecated
    def addParamsLeft(self, key, param):
        self.keys[0] = key
        self.values[0] = param

        self.params = dict(zip(self.keys, self.values))
        self.sflk = [ k[:2] for k in self.params.keys() ]



    def onlyDraw(self):
        self.__del__()
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self._linewidth, color = self._color)
        self.lines = []
        self.lines.append(line)

       
    def condition_mask(self):

        condition_mask0 = ( self.data[0] > settings.xmin) & (self.data[0] < settings.xmax)
        condition_mask1 = ( self.data[1] > settings.ymin) & (self.data[1] < settings.ymax)
        condition_mask = condition_mask0 & condition_mask1
        return np.where(condition_mask)
        


    def lims(self):
        self.limsx()
        self.limsy()

    def limsx(self):
        self._x = np.linspace(settings.xmin, settings.xmax, settings.steps)
        self.ax.set_xlim(settings.xmin, settings.xmax)


    def limsy(self):
        self._y = np.linspace(settings.ymin, settings.ymax, settings.steps)
        self.ax.set_ylim(settings.ymin, settings.ymax)
        

    def grid_(self, step = 2, steps = 10, topConcat = settings.xmax, bottomConcat = settings.xmin):

        minorStep = step / steps


        #grid---------------------------------------
        if (bottomConcat < 0) and (topConcat > 0):
            #------------ minor ticks
            minor_ticksPos = np.arange(0, topConcat, minorStep)
            minor_ticksNeg = np.arange(0, bottomConcat, -minorStep)[::-1]

            minor_ticks = np.append(minor_ticksNeg, minor_ticksPos)

            #----------- major ticks
            major_ticksPos = np.arange(0, topConcat, step)

            major_ticksNeg = np.arange(0, bottomConcat, -step)[::-1]

            major_ticks = np.append(major_ticksNeg, major_ticksPos)

            self.ax.spines['bottom'].set_position('zero')
            self.ax.spines['left'].set_position('zero')


        else:
            minor_ticks = np.arange(bottomConcat, topConcat, minorStep)

            major_ticks = np.arange(bottomConcat, topConcat, step)


        #grid---------------------------------------
        topArrayMinor = np.arange(topConcat, topConcat, minorStep)
        
        topArrayMajor = np.arange(topConcat, topConcat, step)

        bottomArrayMinor = np.arange( bottomConcat, bottomConcat, minorStep)

        bottomArrayMajor = np.arange( bottomConcat, bottomConcat, step)

        minor_ticks = np.concatenate((bottomArrayMinor, minor_ticks, topArrayMinor))

        major_ticks = np.concatenate((bottomArrayMajor, major_ticks, topArrayMajor))

        return minor_ticks, major_ticks

    @staticmethod
    def gridParams(axis):#, maxs = settings.ymax, mins = settings.ymin ):
        def decor(func):
            def wrapper(self, *args, **kwargs):
                
                func(self, *args, **kwargs)


                self.ax.grid(which='minor', alpha=0.2, linewidth = 1.0)
                self.ax.grid(which='major', alpha=0.6, linewidth = 1.0)  
                # alpha stands for transparency: 0 transparent, 1 opaque

                return self.grid_()
            return wrapper
        return decor

    @gridParams(axis = 'x')
    def grid_x(self, step = 2, steps = 10, topConcat = settings.xmax, bottomConcat = settings.xmin):
        minor_ticks, major_ticks = self.grid_()

        self.ax.set_xticks(minor_ticks, minor=True)
        self.ax.set_xticks(major_ticks)
        self.vline = self.ax.axhline(0, color = 'k', linewidth = self._linewidth)
       


    @gridParams(axis = 'y')
    def grid_y(self, step = 2, steps = 10, topConcat = settings.ymax, bottomConcat = settings.ymin):
        minor_ticks, major_ticks = self.grid_()

        self.ax.set_yticks(minor_ticks, minor=True)
        self.ax.set_yticks(major_ticks)
        self.hline = self.ax.axvline(0, color = 'k', linewidth = self._linewidth)

    def erase(self):
        try:#removes all lines
            for line in self.lines:
                line.remove()
                #self.draws.clear()
        except:
            pass

    
    def __del__(self):
        try:#removes all lines
            for line in self.lines:
                line.remove()
                #self.draws.clear()
        except:
            pass

    def __str__(self):

        # Specify the maximum number of elements to display
        max_elements = 5
        L0 = len(self.data[0])
        L1 = len(self.data[1])


        self.plotSettings = (
            f"\nSettings:\n"
            f"\033[93mX.lower = \033[0m {settings.xmin}\n"
            f"\033[93mX.higher = \033[0m {settings.xmax}\n"
            f"\033[93mY.lower = \033[0m {settings.ymin}\n"
            f"\033[93mY.higher = \033[0m {settings.ymax}\n"
            f"\033[93m.steps = \033[0m {settings.steps}\n"
            f"\033[93m._x = \033[0m {self._x[:10]}...\n"
            f"\033[93m.x = \033[0m {self.data[0][:min(max_elements, L0)]}...\n"
            f"\033[93m.y = \033[0m {self.data[1][:min(max_elements, L1)]}...\n"
        )
