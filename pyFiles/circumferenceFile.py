import matplotlib.pyplot as plt
import numpy as np
import random

plt.ion()

from .plotSettFile import plotSett


class circumference(plotSett):
    
    def __init__(self, xmin= -20, xmax = 20, step = 500):
        
        super().__init__(xmin, xmax, step)
        #plotSett.__init__(self)

        self.radius = random.uniform(0, (self.xmax-self.xmin)/2)
        self.center = [random.uniform(self.xmin, self.xmax), random.uniform(self.xmin, self.xmax)]
        self.circup = None
        self.circdw = None
        self.CD = None
        self.data = None
        self.name = None

        colors = ['b', 'blue', 'g', 'green', 'r', 'red',\
                'c', 'cyan', 'm', 'magenta', 'k', 'black']

        self.color = random.choice(colors)

    def remove(self):
        try:
            self.circdw.remove()    
            self.circup.remove()
        except:
            pass

        try:
            self.CD.remove()
        except:
            pass


    def draw(self ):
        self.remove()

        circ = np.sqrt( self.radius**2 - (self.x- self.center[0])**2)#circumference equation
        self.data = [ self.center[1] + circ ] #a one data list with upper side data of circ

        self.data = self.data + [ self.center[1] - circ ] #append one element of list with dw side of circ
        
        self.circdw, = self.ax.plot(self.x, self.data[1], linewidth=2, color = self.color, label = self.name)
        self.ax.legend()


        self.circup, = self.ax.plot(self.x, self.data[0], linewidth=2, color = self.color)#, markersize=12)
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.xmin, self.xmax)
    
    def centerDraw(self):
        self.CD = self.ax.scatter(self.center[0], self.center[1], color = self.color)# s=10, color = self.color, marker='o')



    def __str__(self):
        attributes = (
            f"Attributes:\n"
            f"\033[93mcenter:\033[0m {self.center[0]} {self.center[1]}\n"
            f"\033[93mradius:\033[0m {self.radius}\n"
            f"\033[93mxmin:\033[0m {self.xmin}\n"
            f"\033[93mxmax:\033[0m {self.xmax}\n"
            f"\033[93mx:\033[0m {self.x}\n"
            f"\033[93mdata:\033[0m {self.data}\n"
            f"\033[93mname:\033[0m {self.name}\n"
            f"\033[93mcolor:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93mdraw()\033[0m\n"
            f"\033[93mcenterDraw()\033[0m\n"
            f"\033[93mremove()\033"
        )
        
        return attributes + methods


"""
class segment():
    def __init__(self, xmax = xmax, xmin = xmin):

        self.angCoeff = np.random.randint(-20, 20)
        self.intercept = np.random.randint(xmin, xmax)
        self.idxMin = None
        self.idxMax = None
        self.segment = None
        self.data = None

    def remove(self, obj = picture):
        try:
            self.segment.remove()
        except:
            pass

    def plot(self, obj = picture, color = 'b',\
            xMin = picture.x[0], xMax = picture.x[-1]):
        self.remove(self)
        # obj.x[0] do not work: a bug has to be fixed
        print(obj.x)
        idxMin = np.where( obj.x >= xMin)[0][0]
        idxMax = np.where( obj.x >= xMax)[0][0]
        x = obj.x[idxMin: idxMax] # a local copy of x values
        self.data = self.angCoeff*x + self.intercept
        self.segment, = obj.ax.plot(x, self.data, linewidth=2, color = color)
    

class parabola():
    def __init__(self, xmax = xmax, xmin = xmin, extVar = eval("list(globals().keys() )") ):

        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-(xmax-xmin)/2, + (xmax + xmin)/2)
        self.parabola = None
        self.data = None
        self.name =  extVar  #[-2]


    def remove(self, obj = picture):
        try:
            self.parabola.remove()
        except:
            pass


    def plot(self, obj = picture, color = 'b' ):
        self.remove(self)

        self.data = self.concavity*(obj.x - self.xShift)**2 + self.yShift
        self.parabola, = obj.ax.plot(obj.x, self.data, linewidth=2, color = color)


class triangle(segment):
    def __init__(self):#, xmin, xmax):
        segment().__init__()
        super().__init__()
    
    def plot(self, obj = picture, color = 'b'):
        
        self.data = self.angCoeff*obj.x + self.intercept
        self.segment, = obj.ax.plot(obj.x, self.data)


#list(globals().keys())[-2]
"""
