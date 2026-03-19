import os
path = "/home/stefanovjc/Documents/"
os.chdir(path)
%matplotlib qt
from geompy import *
import random

O = point(0, 0)
O.X.lower = -1
O.X.higher = 18
O.Y.lower = -5

O.X.step = 1
O.Y.step = 1








for j in range(10):
    x0 = random.uniform(3, 6)
    x1 = random.uniform(2, 6)
    y0 = random.uniform(3, 5)
    y1 = -random.uniform(2, 5)
    
    A, B = vector(), vector()
    Ap, Bp = point(x0, y0), point(x1, y1)
    A.points, A.points = O, Ap
    B.points, B.points = O, Bp
    

    #--------------------------------------------
    
    alpha, beta = angle(), angle()
    alpha.centre = beta.centre = O
    C = point(3, 0, draw = False)
    alpha.color = A.color
    beta.color = B.color
    alpha.points, alpha.points = C, Ap
    beta.points, beta.points = Bp, C
    alpha.radius = 1.2
    sizeA = alpha.size*180/pi
    sizeB = beta.size*180/pi
    
    alphaName = text()
    alphaName.color = alpha.color
    alphaName.x, alphaName.y = 3, 1
    alphaName.name = fr"$\alpha = {sizeA:.2f} $"
    
    
    betaName = text()
    betaName.color = beta.color
    betaName.x, betaName.y = 3, -1
    betaName.name = fr"$\alpha = {sizeA:.2f} $"
    betaName.name = fr"$\beta = {sizeB:.2f}$"
    
    vecAName = text()
    vecAName.x, vecAName.y = x0/2, y0*1.4/2
    vecAName.color = A.color
    vecAName.name = r"$\vec{A}$"
    
    
    vecBName = text()
    vecBName.x, vecBName.y = x1/2, y1*1.4/2
    vecBName.color = B.color
    vecBName.name = r"$\vec{B}$"
    pathFile = "/home/stefanovjc/Documents/vetors" + str(j) + ".png"
    plt.savefig(pathFile)
