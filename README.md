This is meant to be the occasion for high school students to start over computer programming for scientific applications. Particularly, it's a tool for visualizing locus in analytical geometry by using python. 

# Installation

Just ensure you have a fully working python environment with matplotlib and numpy installed on it. Than download the script.py and run it on a python interprete, such as ipython

`run script.py`

![Alt Text](pictures/pythonInterpreter.png)


# Usage


At this stage the interpreter will ask you to choice the size of a Cartesian Plane. Say you want a Cartesian Plane with both axes ranging from -10 to 18, with 500 steps.


![Alt Text](pictures/cartesianPlane.png)


Than you can plot one of the following geometric places

### - Circomference

### - Straight Line

### - Parabola


## Random circumference

`C1 = circumference()`

`C1.plot()`

![Alt Text](pictures/circumferenceDraw.png)




# Circumference with specific center position and radius size




`C1.radius = 5`

to change the radius to 5

`C1.center = [2, 5]`

to move the center to the point [2, 5]. 

`C1.plot()`

To modify the plot

![Alt Text](pictures/circumferenceDraw2.png)



change color

`C1.plot( color = 'red')`

![Alt Text](pictures/circumferenceDrawRed.png)

or 

`C1.plot( color = 'black')`

In case you want to draw a straight line or a parabola, than do the some job with one of the following classes:

`L1 = straightLine()`

`L1.plot()`


for a straight line

`P1 = parabola()`

`P1.plot()`

for a parabola

clearly, straight lines or parabola do not have any radius or center. If you want to modify their position on the Cartesian Plane or their shape, than type

`P1.__dict__`

or

`L1.__dict__`

once replaced the random attributes chosen from the software, than plot again

`P1.plot()`

or

`L1.plot()`
