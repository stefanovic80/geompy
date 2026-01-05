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
c.grid(majorStep = .2)

P_1 = point(c)
P_2 = point(c)
P_3 = point(c)
P_1.draw("$P_1$")
P_2.draw("$P_2$")
P_3.draw("$P_3$")

O = c.center

secant1 = segment()
secant2 = segment()
secant3 = segment()
radius1 = segment()
radius2 = segment()

tangent = segment()

secant1.erase()
secant2.erase()
secant3.erase()

radius1.erase()
radius2.erase()

tangent.erase()

secant1.point[0] = P_1
secant1.point[1] = P_3

secant2.point[0] = P_3
secant2.point[1] = P_2

secant3.point[0] = P_2
secant3.point[1] = P_1

radius1.point[0] = O
radius1.point[1] = P_1

radius2.point[0] = O
radius2.point[1] = P_2


secant1.draw("$s_1$", cut = True)
secant2.draw("$s_2$", cut = True)
secant3.draw("$s_3$", cut = True)

radius1.draw("$R_1$", cut = True)
radius2.draw("$R_2$", cut = True)

tangent.angCoeff = -1/radius2.angCoeff
tangent.point[0] = P_2

tangent.draw("tangent", cut = True)
