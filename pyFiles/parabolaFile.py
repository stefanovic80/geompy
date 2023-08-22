# parabolaFile.py
from . import plt, np, random

plt.ion()

from ._plotSettFile import plotSett


class parabola(plotSett):

    def __init__(self, xmin= -20, xmax = 20, steps = 500):

        super().__init__(xmin, xmax, steps)
        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-(xmax-xmin)/2, + (xmax + xmin)/2)
        self.parabola = None
        self.data = None
        self.name =  None

        colors = ['b', 'blue', 'g', 'green', 'r', 'red',\
                'c', 'cyan', 'm', 'magenta', 'k', 'black']

        self.color = random.choice(colors)





    def remove(self):
        try:
            self.parabola.remove()
        except:
            pass


    def __del__(self):
    	self.remove()

    def draw(self ):
        self.remove()

        self.data = self.concavity*(self.x - self.xShift)**2 + self.yShift
        self.parabola, = self.ax.plot(self.x, self.data, linewidth=2, color = self.color, label = self.name) # can be optimized for ALL pictures vi rmParams!

    def __str__(self):
        attributes = (
            f"\033[93mType:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93mxShift:\033[0m {self.xShift}\n"
            f"\033[93myShift:\033[0m {self.yShift}\n"
            f"\033[93mconcavity:\033[0m {self.concavity}\n"
            f"\033[93mx:\033[0m {self.x}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mremove()\033[0m\n"
        )
        
        plotSettings = (
            f"\nSettings:\n"
            f"\033[93mxmin:\033[0m {self.xmin}\n"
            f"\033[93mxmax:\033[0m {self.xmax}\n"
            f"\033[93msteps:\033[0m {self.steps}\n"
        
        )
        
        return attributes + methods + plotSettings



"""

class triangle(segment):
    def __init__(self):#, xmin, xmax):
        segment().__init__()
        super().__init__()
    
    def plot(self, obj = picture, color = 'b'):
        
        self.data = self.angCoeff*obj.x + self.intercept
        self.segment, = obj.ax.plot(obj.x, self.data)


#list(globals().keys())[-2]
"""
