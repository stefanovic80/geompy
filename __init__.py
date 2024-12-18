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
from itertools import combinations

_set = start()
_set.grid()








loci = {\
        'line': ['m', 'p', 'p', 'q'],\
        'parabola': ['a', 'b', 'c', 'p', 'p', 'p', 'c'],\
        'circumference':['a', 'b', 'c', 'd']\
        }


for name, param in loci.items():
    #List of Keys
    lok = set( list(combinations(param, 3)) )
    output_dir = os.path.join(os.path.expanduser("~"), os.getcwd(), "geompy", "pyFiles", "keys")
    filePath = os.path.join(output_dir, name + "_listOfKeys.py")
    
    if not os.path.exists(filePath):
        #os.makedirs(output_dir, exist_ok = True)
        number = 0
        with open(filePath, "w") as file:
            file.write("keys = {\\\n")
            for combo in lok:
                # Convertire ogni tupla in una stringa e scriverla nel file
                file.write(f"    {combo}: self.calc" + f"{number:02}" + " ,\\\n")
                number += 1
            file.write("}")



#for i in range(100):  # Ciclo da 0 a 99
#    print(f"{i:02}")

"""
#Line
#parameters
name = "line"
params = ['m', 'p', 'p', 'q']
#List of Keys
lok = set( list(combinations(params, 3)) )
output_dir = os.path.join(os.path.expanduser("~"), os.getcwd(), "geompy", "pyFiles", "keys")
filePath = os.path.join(output_dir, name + "_listOfKeys.py")

if not os.path.exists(filePath):
    #os.makedirs(output_dir, exist_ok = True)
    with open(filePath, "w") as file:
        file.write("keys = [\\\n")
        for combo in lok:
            # Convertire ogni tupla in una stringa e scriverla nel file
            file.write(f"    {combo} ,\\\n")
        file.write(" ]")




#Parabola
#parameters
params = ['a', 'b', 'c', 'p', 'p', 'p', 'c']
#List of Keys
lok = set( list(combinations(params, 3)) )
output_dir = os.path.join(os.path.expanduser("~"), os.getcwd(), "geompy", "pyFiles", "keys")
filePath = os.path.join(output_dir, "parabola_listOfKeys.py")

if not os.path.exists(filePath):
    #os.makedirs(output_dir, exist_ok = True)
    with open(filePath, "w") as file:
        file.write("keys = [\\\n")
        for combo in lok:
            # Convertire ogni tupla in una stringa e scriverla nel file
            file.write(f"    {combo} ,\\\n")
        file.write(" ]")

"""

print(__name__) # __name__ = "geompy"

# Alternatively, you can define a function to be run upon import
#def initialize():
#    _set = plotSett()
#    _set.grid()
