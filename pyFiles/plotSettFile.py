import matplotlib.pyplot as plt
import numpy as np

plt.ion()



class plotSett():
    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot(111)
    def __init__(self, xmin = -10, xmax = 10, step = 500):
        self.xmin = xmin
        self.xmax = xmax
        self.step = step

        x = [t/abs(self.step) for t in range(self.xmin*self.step, self.xmax*self.step + 1, 1)]
        self.x = np.array(x)



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
