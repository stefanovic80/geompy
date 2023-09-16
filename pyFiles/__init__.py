# __init__.py
import matplotlib.pyplot as plt
import numpy as np
import random


global seed
seed = random.randint(1, 1000)

#xmin, xmax, steps, linewidth, seed = -1.2, 1.2, 500, 2, 1
#BUG on xmin and xmax: it doesn't accept all values number (plus/minus 1.2 don't work
#BUG on xmin and xmax: whenever u change them, they return to the default one!
xmin, xmax, steps, linewidth, seed = -1.2, 1.2, 500, 2, 1
