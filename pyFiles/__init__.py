# __init__.py
import matplotlib.pyplot as plt
import numpy as np
import random

import ctypes

global seed
seed = random.randint(1, 1000)


"""
def update_config(new_xmin, new_xmax):
    global xmin, xmax
    xmin = new_xmin
    xmax = new_xmax
    # Update the config.py file
    with open('config.py', 'w') as config_file:
        config_file.write(f'xmin = {xmin}\n')
        config_file.write(f'xmax = {xmax}\n')
"""
try:
    xmin
except:
    xmin = float(input("xmin\n"))
    xmax = float(input("xmax\n"))


steps, linewidth, seed = 1000, 2, 1
