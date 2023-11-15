#from pyFiles import xmin, xmax


# Import functions and classes from your package
#from pyFiles.module2 import MyClass
from pyFiles._plotSettFile import plotSett
from pyFiles.pointFile import point
from pyFiles.circumferenceFile import circumference
from pyFiles.ellipseFile import ellipse
from pyFiles.segmentFile import segment
from pyFiles.parabolaFile import parabola
from pyFiles.config import xmin, xmax

from pyModules2gen.triangleFile import triangle
from pyModules2gen.angleFile import angle

import matplotlib.pyplot as plt
import numpy as np
import random

from numpy import pi
from copy import copy



def main():
    print("Running main.py")

    global xmin, xmax
    
    

    _set = plotSett()
    _set.grid()
    # result = my_function()
    #print("Result from module1:", result)

    #seed = random.randint(1, 1000)
    #figure = plotSett()
    #instance.some_method()

if __name__ == "__main__":
    main()

