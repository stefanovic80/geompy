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

A = point()
B = point()
C = point()

A.color = B.color = C.color
A.draw("A")
B.draw("B")
C.draw("C")

AB = segment()
BC = segment()
CA = segment()

AB.erase()
BC.erase()
CA.erase()

AB.color = BC.color = CA.color

AB.point[0] = A
AB.point[1] = B

BC.point[0] = B
BC.point[1] = C

CA.point[0] = C
CA.point[1] = A

AB.draw(cut = True)
BC.draw(cut = True)
CA.draw(cut = True)
