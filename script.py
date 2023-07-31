import matplotlib.pyplot as plt
import numpy as np

plt.ion()

class plot():
    def __init__(self, xmin = -1, xmax = 1, step = 200):# = True):
        x = [t/abs(step) for t in range(xmin*step, xmax*step + 1, 1)]
        self.x = np.array(x)
        self.fig = plt.figure(figsize =(9, 9))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(xmin, xmax)
        self.ax.grid(False)
    #def set_grid(self, grid = True):
    #    self.ax.grid(grid)

xmin = int(input('xmin = \n '))
xmax = int(input('xmax = \n '))
step = int(input('step = \n '))


picture = plot(xmin = xmin, xmax = xmax, step = step)
#picture as a "plot" class type object



class circumference():
    def __init__(self, xmax = xmax, xmin = xmin):
        self.radius = np.random.randint((xmax-xmin)/2)
        self.center = [np.random.randint(xmin, xmax), np.random.randint(xmin, xmax)]
        self.circup = None
        self.circdw = None
        self.data = None
        
    def remove(self, obj = picture):
        try:
            self.circdw.remove()    
            self.circup.remove()
        except:
            pass
    def plot(self, obj = picture, color = 'b' ):
        self.remove(self)

        circ = np.sqrt( self.radius**2 - (obj.x- self.center[0])**2)#circumference equation
        self.data = [ self.center[1] + circ ] #a one data list with upper side data of circ
        self.circup, = obj.ax.plot(obj.x, self.data[0], linewidth=2, color = color)#, markersize=12)

        self.data = self.data + [ self.center[1] - circ ] #append one element of list with dw side of circ
        self.circdw, = obj.ax.plot(obj.x, self.data[1], linewidth=2, color = color)


class straightLine():
    def __init__(self, xmax = xmax, xmin = xmin):#,  angCoeff = np.random.randint(-20, 20), \
           # intercept = np.random.randint(xmin, xmax ), obj = picture, color = 'b'  ):
        self.angCoeff = np.random.randint(-20, 20)
        self.intercept = np.random.randint(xmin, xmax)
        self.strightLine = None
        self.data = None

    def remove(self, obj = picture):
        try:
            self.straightLine.remove()
        except:
            pass

    def plot(self, obj = picture, color = 'b' ):
        self.remove(self)

        self.data = self.angCoeff*obj.x + self.intercept
        self.straightLine, = obj.ax.plot(obj.x, self.data, linewidth=2, color = color)#, markersize=12)



class parabola():
    def __init__(self, xmax = xmax, xmin = xmin):#,  angCoeff = np.random.randint(-20, 20), \
           # intercept = np.random.randint(xmin, xmax ), obj = picture, color = 'b'  ):
        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-(xmax-xmin)/2, + (xmax + xmin)/2)
        self.parabola = None
        self.data = None

    def remove(self, obj = picture):
        try:
            self.parabola.remove()
        except:
            pass


    def plot(self, obj = picture, color = 'b' ):
        self.remove(self)

        self.data = self.concavity*(obj.x - self.xShift)**2 + self.yShift
        self.parabola, = obj.ax.plot(obj.x, self.data, linewidth=2, color = color)#, markersize=12)

#class straightLineCalc():
#    def __init__(self, straightLine1, straightLine2):
#        self.straightLineData1 = straightLineData1
#        self.straightLineData2 = straightLineData2
#        self.L1.angCoeff = L1.angCoeff
#        self.L2.angCoeff = L2.angCoeff
#    def angCoeffDiff(self):
#        ang = np.arctan(self.L1.angCoeff) - np.arctan(self.L2.angCoeff)
#        return ang
