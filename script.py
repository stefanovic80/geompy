import matplotlib.pyplot as plt
import numpy as np

plt.ion()



class plotSett():
    #xmin = -10
    #xmax = 10
    #step = 500

    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot(111)

    #x = [t/abs(plotSett.step) for t in range(xmin*plotSett.step, xmax*plotSett.step + 1, 1)]
    #x = np.array(x)

"""

    def __init__(self, xmin = -10, xmax = 10, step = 200, grid = False):


    x = [t/abs(step) for t in range(xmin*step, xmax*step + 1, 1)]
        self.x = np.array(x)
        
        self.xmin = self.x[0]
        self.xmax = self.x[-1]
        self.step = 200

        self.fig = plt.figure(figsize =(9, 9))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(xmin, xmax)
        self.ax.grid(grid)
    def grid(self, grid = True):
        self.ax.grid(grid)
        #self.ax.set_xticks(self.x)
        #self.ax.set_xticklabels([])
"""


#xmin = int(input('xmin = \n '))
#xmax = int(input('xmax = \n '))
#step = int(input('step = \n '))
#grid = bool(input('grid = \n '))

#picture = plot(xmin = xmin, xmax = xmax, step = step)
#picture as a "plot" class type object



class circumference(plotSett):
    def __init__(self, xmin = -10, xmax = 10):
        
        super().__init__()
        #self.remove(self)
        self.xmin = xmin 
        self.xmax = xmax

        self.radius = np.random.randint((self.xmax-self.xmin)/2)
        self.center = [np.random.randint(self.xmin, self.xmax), np.random.randint(self.xmin, self.xmax)]
        self.circup = None
        self.circdw = None
        self.data = None
        
    def remove(self):
        try:
            self.circdw.remove()    
            self.circup.remove()
        except:
            print(".remove() not working")

    def plot(self, color = 'b' ):
        #self.remove(self)
        
        step = 500

        x = [t/abs(step) for t in range(self.xmin*step, self.xmax*step + 1, 1)]
        x = np.array(x)

        circ = np.sqrt( self.radius**2 - (x- self.center[0])**2)#circumference equation
        self.data = [ self.center[1] + circ ] #a one data list with upper side data of circ
        self.circup, = self.ax.plot(x, self.data[0], linewidth=2, color = color)#, markersize=12)

        self.data = self.data + [ self.center[1] - circ ] #append one element of list with dw side of circ
        self.circdw, = self.ax.plot(x, self.data[1], linewidth=2, color = color)



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
