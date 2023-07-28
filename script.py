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
        self.circup = 0
        self.circdw = 0
    def plot(self, obj = picture, color = 'b' ):
        try:
            self.circup.remove()
            self.circdw.remove()
        except:
            pass


        circ = np.sqrt( self.radius**2 - (obj.x- self.center[0])**2)#circumference equation
        y_up = self.center[1] + circ
        y_dw = self.center[1] - circ #circumference equation
        self.circup, = obj.ax.plot(obj.x, y_up, linewidth=2, color = color)#, markersize=12)
        self.circdw, = obj.ax.plot(obj.x, y_dw, linewidth=2, color = color)
        #[ value for value in A if np.isnan(value) != True]
        return y_up, y_dw






class straightLine():
    def __init__(self, xmax = xmax, xmin = xmin):#,  angCoeff = np.random.randint(-20, 20), \
           # intercept = np.random.randint(xmin, xmax ), obj = picture, color = 'b'  ):
        self.angCoeff = np.random.randint(-20, 20)
        self.intercept = np.random.randint(xmin, xmax)
        self.strightLine = 0

    def plot(self, obj = picture, color = 'b' ):
        try:
            self.straightLine.remove()
        except:
            pass
            #self.radius = random.randint(0, xmax-xmin)

        line = self.angCoeff*obj.x + self.intercept
        self.straightLine, = obj.ax.plot(obj.x, line, linewidth=2, color = color)#, markersize=12)
        #[ value for value in A if np.isnan(value) != True]
        return line






class parabola():
    def __init__(self, xmax = xmax, xmin = xmin):#,  angCoeff = np.random.randint(-20, 20), \
           # intercept = np.random.randint(xmin, xmax ), obj = picture, color = 'b'  ):
        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-(xmax-xmin)/2, + (xmax + xmin)/2)
        self.parabola = 0

    def plot(self, obj = picture, color = 'b' ):
        try:
            self.parabola.remove()
        except:
            pass
            #self.radius = random.randint(0, xmax-xmin)

        parab = self.concavity*(obj.x - self.xShift)**2 + self.yShift
        self.parabola, = obj.ax.plot(obj.x, parab, linewidth=2, color = color)#, markersize=12)
        #[ value for value in A if np.isnan(value) != True]
        return parab

#class straightLineCalc():
#    def __init__(self, straightLine1, straightLine2):
#        self.straightLineData1 = straightLineData1
#        self.straightLineData2 = straightLineData2
#        self.L1.angCoeff = L1.angCoeff
#        self.L2.angCoeff = L2.angCoeff
#    def angCoeffDiff(self):
#        ang = np.arctan(self.L1.angCoeff) - np.arctan(self.L2.angCoeff)
#        return ang
