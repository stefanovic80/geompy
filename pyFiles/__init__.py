# __init__.py
import matplotlib.pyplot as plt
import numpy as np
import random

import ctypes

global seed
seed = random.randint(1, 1000)

xmin = float(input("xmin\n"))
xmax = float(input("xmax\n"))
#xmin, xmax, steps, linewidth, seed = -1.2, 1.2, 500, 2, 1
steps, linewidth, seed = 500, 2, 1
