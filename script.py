import matplotlib.pyplot as plt
import numpy as np

plt.ion()

class plot():
    def __init__(self, xmin = -1, xmax = 1, step = 200):# = [ t/200 for t in range(-200, 201)]):
        x = [t/abs(step) for t in range(xmin*step, xmax*step + 1, 1)]
        self.x = np.array(x)
        self.fig = plt.figure(figsize =(9, 9))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(xmin*1.2, xmax*1.2)
        self.ax.set_ylim(xmin*1.2, xmax*1.2)

xmin = int(input('xmin = \n '))
xmax = int(input('xmax = \n '))
step = int(input('step = \n '))
picture = plot(xmin = xmin, xmax = xmax, step = step)

class circumference():
    def __init__(self, radius = 1, center = [0, 0]):
        self.radius = radius
        self.center = center
        self.circup = 0
        self.circdw = 0
    def plot(self, obj = picture, color = 'b' ):
        #last = x[-1]**2
        circ = np.sqrt( self.radius**2 - (obj.x- self.center[0])**2)#circumference equation
        y_up = self.center[1] + circ
        y_dw = self.center[1] - circ #circumference equation
        self.circup, = obj.ax.plot(obj.x, y_up, linewidth=2, color = color)#, markersize=12)
        self.circdw, = obj.ax.plot(obj.x, y_dw, linewidth=2, color = color)


class straightLine():
    def __init__(self, angCoeff = np.random.randint(-20, 20), \
            intercept = np.random.randint(-1, 1)/10):
        self.angCoeff = angCoeff
        self.intercept = intercept
    def plot(self, obj = picture):
        y = self.angCoeff*obj.x + self.intercept
        straightLine, = obj.ax.plot(obj.x, y)


#plt.close()#automatically opens plots. To be removed
#plt.close()
