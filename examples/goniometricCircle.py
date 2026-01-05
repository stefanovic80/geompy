#import subprocess
#subprocess.call(['python', 'main.py'])

import sys
sys.path.append('../main')  
# Add the parent directory to the Python path
import main  # Import the main module

from main import *

# to run:
# move to the main folder
# type
# %run examples/goniometricCircle.py

#random.seed(number)


c = circumference()
c.radius = 1
O = c.center = point(0, 0)
c.color = c.center.color = 'b'
c.draw("c")
c.center.draw("O")
c.grid()

"""
P = point(c)
P.draw("P")
P.draw("P")
R = segment()
R.erase()
R.point[0] = c.center
R.point[1] = P
R.draw("R = 1", cut = True)
"""
