#%run main.py

# Import functions and classes from your package
from .pyFiles._plotSettFile import plotSett as start
from .pyFiles.pointFile import point
from .pyFiles.circumferenceFile import circumference
from .pyFiles.ellipseFile import ellipse
from .pyFiles.lineFile import line
from .pyFiles.segmentFile import segment
from .pyFiles.parabolaFile import parabola
from .pyFiles.functionFile import function
from .pyFiles.functionFile import x

from .pyModules2gen.triangleFile import triangle
from .pyModules2gen.angleFile import arc

import matplotlib.pyplot as plt
from numpy import *
#import numpy as np
import random
import os

_set = start()
_set.grid()

print(__name__) # __name__ = "geompy"

# Alternatively, you can define a function to be run upon import
#def initialize():
#    _set = plotSett()
#    _set.grid()
