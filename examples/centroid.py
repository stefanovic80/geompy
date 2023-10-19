#import subprocess
#subprocess.call(['python', 'main.py'])

import sys
sys.path.append('../main')
# Add the parent directory to the Python path
import main  # Import the main module

from main import *

t = triangle()
t.draw()
A = copy(t.A)
B = copy(t.B)
C = copy(t.C)

vertices = [A, B, C]
names = ['A', 'B', 'C']

A.grid(majorStep = 2, minorSteps = 10)

j = 0
for vertex, name in zip(vertices, names):
    vertex.color = 'k'
    vertex.draw(name)

coordsD = t.AB.dist( t.AB.length/2 )
coordsE = t.BC.dist( t.BC.length/2 )
coordsF = t.CA.dist( t.CA.length/2 )

D = point(coordsD[0], coordsD[1])
E = point(coordsE[0], coordsE[1])
F = point(coordsF[0], coordsF[1])

medA = segment()
medB = segment()
medC = segment()
medA.erase()
medB.erase()
medC.erase()

midPoints = [D, E, F]
vertices = [C, A, B]
medians = [medC, medA, medB]
for midPoint, vertex, median in zip(midPoints, vertices, medians):
    median.point[0] = vertex
    median.point[1] = midPoint
    median.color = 'b'
    median.draw(cut = True)
