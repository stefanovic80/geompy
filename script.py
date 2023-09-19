import subprocess
subprocess.call(['python', 'main.py'])

from main import *

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

R = segment()
R.erase()
R.point[0] = c.center
R.point[1] = P
R.draw("R = 1")
