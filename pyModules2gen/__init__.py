import numpy as np
import matplotlib.pyplot as plt

from config import xmin, xmax

# mainFolder/pyFiles/__init__.py
from config import xmin, xmax

def update_config(new_xmin, new_xmax):
    global xmin, xmax
    xmin = new_xmin
    xmax = new_xmax
