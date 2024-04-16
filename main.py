# Import functions and classes from your package
from pyFiles._plotSettFile import plotSett

#may be deleted
#from geompy.pyFiles import plotSett

"""
#how to adjust plot size according with monitor size
from screeninfo import get_monitors

def get_monitor_size():
    monitors = get_monitors()
    sizes = []
    for monitor in monitors:
        sizes.append((monitor.width, monitor.height))
    return sizes

print("Monitor sizes (width, height):", get_monitor_size())
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

