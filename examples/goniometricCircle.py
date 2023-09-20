import subprocess
subprocess.call(['python', 'main.py'])
from main import *

# to run:
# move to the main folder
# type
# %run examples/goniometricCircle.py

#random.seed(number)

c = circumference()
c.radius = 1
c.center = point(0, 0)
c.color = c.center.color = 'b'
c.draw("c")
c.center.draw("O")
c.grid()

P = point(c)
P.draw("P")
P.draw("P")

R = segment()
R.erase()

R.point[0] = c.center
R.point[1] = P

#segment limits
xLim = []
for u in R.point:
    xLim = xLim + [ u.coords[0] ]

xLim.sort()

R.xMin = xLim[0]
R.xMax = xLim[1]
#segment limits

R.draw("R = 1")
