#%run main.py

# Import functions and classes from your package
from .pyFiles._plotSettFile import plotSett as start

import matplotlib.pyplot as plt
from numpy import *
import random


#----------------------------------------------------------------------------------------------------------
#line: m = angular coefficient, p and p = point, q = intercept
#parabola: a, b and c parabola coefficients, p, p, and p = points, v = vertex
#circumference: a, b and c circumference coefficients, d = centre, r = radius

import os
from itertools import combinations

#[params], Degree of Freedom (2 or 3)
loci = {\
        'line': (['m', 'po', 'po', 'q'], 2),\
        'parabola': (['a', 'b', 'c', 'po', 'po', 'po', 'v'], 3),\
        'circumference': (['a', 'b', 'c', 'ce', 'po', 'po', 'po', 'ra'], 3),\
        'ellipse': (['a', 'b', 'c', 'd', 'e', 'ec', 'fo', 'fo' 'po','po', 'po', 'po', 'po'], 5),\
        'hyperbola':(['a', 'b', 'c', 'd', 'e', 'ec', 'fo', 'fo' 'po','po', 'po', 'po', 'po'], 5)\
        }
    

for name, param in loci.items():
    string = "from .." + name + "." + name +  "CalcFile import "  +  name + "Calc\n\nclass method(" + name\
            +  "Calc):\n    def __init__(self):\n        super().__init__()\n        self.draws = {"
    # List of Keys
    dos = param[1]
    lok = set(list(combinations(param[0], dos)))
    output_dir = os.path.join(os.path.expanduser("~"), os.getcwd(), "geompy", "pyFiles", "keys")
    filePath = os.path.join(output_dir, name + "_listOfKeys.py")

    if not os.path.exists(filePath):
        number = 0
        with open(filePath, "w") as file:
            file.write(string)
            lok = sorted(lok)
            for i, combo in enumerate(lok):
                # Scrivere la combinazione nel file, ma evitare la virgola finale
                file.write(f"\n            {combo}: self.noMethod")
                if i < len(lok) - 1:  # Aggiungi la virgola solo se non è l'ultimo elemento
                    file.write(",")
            file.write("\n        }\n\n")  # Chiudere il dizionario alla fine
            file.write("    def noMethod(self):\n         print('This method has not been implemented yet!')\n")
#----------------------------------------------------------------------------------------------------------










from .pyFiles.pointFile import point
from .pyFiles.circumference.circumferenceFile import circumference
from .pyFiles.ellipse.ellipseFile import ellipse
from .pyFiles.hyperbola.hyperbolaFile import hyperbola
from .pyFiles.line.lineFile import line
from .pyFiles.segment.segmentFile import segment
from .pyFiles.parabola.parabolaFile import parabola
from .pyFiles.function.functionFile import function
from .pyFiles.function.functionFile import x

from .pyFiles.triangle.triangleFile import triangle
from .pyFiles.angle.angleFile import arc
_set = start()
_set.grid()





print(__name__) # __name__ = "geompy"

# Alternatively, you can define a function to be run upon import
#def initialize():
#    _set = plotSett()
#    _set.grid()
