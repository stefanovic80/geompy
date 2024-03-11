# Import functions and classes from your package
from pyFiles._plotSettFile import plotSett

#may be deleted
#from geompy.pyFiles import plotSett
"""
from pyFiles.pointFile import point
from pyFiles.circumferenceFile import circumference
from pyFiles.ellipseFile import ellipse
from pyFiles.lineFile import line
from pyFiles.parabolaFile import parabola
from pyModules2gen.triangleFile import triangle
from pyModules2gen.angleFile import angle


from geompy.pyFiles.pointFile import point
from .pyFiles.circumferenceFile import circumference
from .pyFiles.ellipseFile import ellipse
from .pyFiles.lineFile import line
from .pyFiles.parabolaFile import parabola

from .pyModules2gen.triangleFile import triangle
from .pyModules2gen.angleFile import angle
"""


import matplotlib.pyplot as plt
import numpy as np
import random
import os

from numpy import pi#, sqrt, sin, cos, tan, arctan, 
from copy import copy


def main():
    print("Running main.py")

    _set = plotSett()
    _set.grid()
    
if __name__ == "__main__":
    main()

