# Import functions and classes from your package
from pyFiles._plotSettFile import plotSett


import matplotlib.pyplot as plt
import numpy as np
import random
import os

from numpy import pi#, sqrt, sin, cos, tan, arctan, 
from copy import copy


def main():
    print("Running main.py\n")
    
    print(__name__)
    _set = plotSett()
    _set.grid()
    
if __name__ == "__main__":
    #if __name__ == "main":
    main()

