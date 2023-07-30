This is meant to be the occasion for high school students to start over computer programming for scientific applications. Particularly, it's a tool for visualizing locus in analytical geometry by using python. 

# Installation

Just ensure you have a fully working python environment with matplotlib and numpy installed on it. Than download the script.py and run it on a python interprete, such as ipython

`run script.py`

![Alt Text](pictures/pythonInterpreter.png)


<!conda env create -f analyticGeomEnv.yml>

# Usage


At this stage the interpreter will ask you to choose the size of a Cartesian Plane. Say you want a Cartesian Plane with both axes ranging from -10 to 18, with 500 steps.


![Alt Text](pictures/cartesianPlane.png)


Than you can plot one of the following geometric places

### - Circomference

### - Straight Line

### - Parabola


# Draw a (random) circumference

Type

`C1 = circumference()`

"C1" is a "circumference" class type. It choose a random value for the circumference radius (C1.radius) and a couple of random values (C1.center) for x and y circumference center point

`C1.plot()`

the .plot() method draw the circumference

![Alt Text](pictures/circumferenceDraw.png)




## Draw a specific circumference


choose the radius

`C1.radius = 5`

choose the center position

`C1.center = [2, 5]`

Draw the desired circumference 

`C1.plot()`


![Alt Text](pictures/circumferenceDraw2.png)


# Change color

Say you have drawn a circumference by using a "circunference method" named "C1". To change it's color to red type this

`C1.plot( color = 'red')`

![Alt Text](pictures/circumferenceDrawRed.png)

to change to "black" type

`C1.plot( color = 'black')`


# Delete a circumference

According with previous notes, we suppose the drawn circumference is a "C1" object. Than

`C1.circup.remove()`

removes the upper side of the circomference, while

`C1.circdw.remove()`

removes the down side of it.





# Draw a (random) straight line


`L1 = straightLine()`

L1 is an object of "straightLine" class type which choose random values for the angular coefficient (L1.angCoeff) and the intercept (L1.intercept)

`L1.plot()`

L1.plot() draws the geometrical locus

![Alt Text](pictures/straightLine.png)


## Draw a specific straight line

choose the angular coefficient

`L1.angCoeff = 6`

choose the intercept

`L1.intercept = 10`

![Alt Text](pictures/straightLine2.png)


## Delete a straight line

According with previous notes, we suppose the drawn straight line is a "L1" object. Than

`L1.straightLine.remove()`

removes the straight line you previously have drawn.

# Draw a (random) Parabola


`P1 = parabola()`

P1 is an object of "parabola" class type which choose random values for the parabola parameters:

- x-shift (P1.xShift)

- y-shift (P1.yShift)

- concavity (P1.concavity)

`P1.plot()`

P1.plot() draws the geometrical locus

![Alt Text](pictures/parabola.png)


## Draw a specific parabola

choose an x-Shift of 

`P1.xShift = 5`

choose a y-Shift of 0

`P1.YShift = 0`

choose a concavity equal to 0.5

`P1.concavity = 0.5`

draw the parabola

`P1.plot()`

![Alt Text](pictures/parabola2.png)

## Delete a parabola

According with previous notes, we suppose the drawn parabola is a "P1" object. Than

`P1.parabola.remove()`

removes the parabola you previously have drawn.






# How to see geometrical locus parameters
 
`C1.__dict__`

`P1.__dict__`

`L1.__dict__`

