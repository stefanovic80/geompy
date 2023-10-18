# Import functions and classes from your package
#from pyFiles.module2 import MyClass
from pyFiles._plotSettFile import plotSett
from pyFiles.pointFile import point
from pyFiles.circumferenceFile import circumference
from pyFiles.ellipseFile import ellipse
from pyFiles.segmentFile import segment
from pyFiles.parabolaFile import parabola
#from pyFiles.triangleFile import triangle
#from pyFiles.angleFile import angle

from pyModules2gen.triangleFile import triangle

import matplotlib.pyplot as plt
import numpy as np
import random

from numpy import pi
from copy import copy



def main():
    print("Running main.py")
    
    __set = plotSett()
    __set.grid()
    # result = my_function()
    #print("Result from module1:", result)

    #seed = random.randint(1, 1000)
    #figure = plotSett()
    #instance.some_method()

if __name__ == "__main__":
    main()

