**As this project is rapidly evolving, the current README file provides only a preliminary explanation of its functionality and operation. Hopefully, an accurate and comprehensive README file will be available soon.**

There are already plenty of Python libraries and other software designed for scientific purposes. However, their complexity often makes them prohibitive for educational use.

This project, mainly built on top of matplotlib and numpy, is a python library for fast geometric loci visualization. 
It is intended to provide high school students and their professors who deal with geometric locus drawings an opportunity to start over computer programming for scientific applications with Python.



# Installation and start up

Make sure you have matplotlib, random and numpy libraries installed on a fully working Ipython environment. Download the present project, then open a console and move to the folder where the main.py file is located; which is named "analyticGeometry". Run the ipython intepreter (type "ipython"), and type

`run main.py`

![Alt Text](pictures/pythonInterpreter.png)

If everything goes fine (which means there is no need for a specific conda environment), just go ahead with it by choosing the minimum (xmin) and maximum (xmax) values for both the Cartesian axes. In this example, you gonna choose -20 and 20, respectively:

`xmin`

`-20`

`xmax`

`20`


in case of any error, due to any package version mismatch, than you must create a 'analyticGeomEnv' conda environment. So, go back to your OS console, on the "analyticGeometry" folder and type

`conda env create -f analyticGeomEnv.yml`

`conda activate analyticGeomEnv`.

(it may take time, depending on the available connection speed). Once activated, try again to run main.py on your ipython interpreter, as previously explained.



# Usage

The 

`who`

command shows the list of all the python variables currently in use

![Alt Text](pictures/who.png)


among them, there are some having the some name as some of the most typical geometrical loci

### - [point](#draw-a-point)

### - [circumference](#draw-a-random-circumference)

### - [ellipse] (#draw-a-random-ellipse)

### - [segment](#draw-a-random-straight-line)

### - [parabola](#draw-a-random-parabola)


Such variables are python classes. For each one of them you can define one or more instances. Each instance corresponds with a specific geometrical locus of that type. The .draw() shows the respective plot

As an example, say you want to draw a circumference. As first step you have to create a circumference type instance, than you gonna use the .draw() method to provide it's graphic representation


`C = circumference()`

`C.draw()`

as a python instance, the C variable has attributes, other methods, or even instances of different classes (in this case, there is a point class type instance, which is the circumference center),  which can be shown by typing 

`print(C)`

each one of them can be constumized by the user as in this example

`C.radius = 7`

`C.color = 'blue'`

`C.center = point(0, 0)`

`C.draw()`


In case you need to deal with more than one circumference, than you just have to create other instances of the some type as follows:


`C1 = circumference()`

`C1.draw()`

In the some way, if you want to draw a point type geometrical locus, than you have to define a point class type instance. If you want to draw a segment type geometrical locus, than you have to define a segment class type instance and so on.


# Draw a point

As already seen from the "who" command, a "point" class is available on analyticGeometry.

Let's draw a point in a cartesian plane.

`P = point()`

`P.draw()`

as no arguments are passed in between the brackets, than coordinates are randomly choosen and no names will result on the plot. Otherwise

`P = point(3, -9)`

`P = draw("P_1")`

Details of P instance 

`print(P)`

show that an alternative way to change coordinates is passing them into the .coords attribute as a python list of two numbers

`P.coords = [6, -4]`

according with matplotlib library, the .color attribute can be choosen from the following list

- ``'b'``          blue

- ``'g'``          green

- ``'r'``          red

- ``'c'``          cyan

- ``'m'``          magenta

- ``'y'``          yellow

- ``'k'``          black

- ``'w'``          white


You can pass an instance ossociated with a geometric locus into point class


`c = circumference()`
`c.draw()`
`P = point(c)`
`P.draw("P")`


# Add axes and a grid

Choose one of the defined instances, no matter of which class they come from, and use the .grid() method

`P.grid()`


by typing it more times, you gonna increase grid density or dropped it down if -1 is passed as grid argument

`P.grid(-1)`

otherwise use the majorStep argument to set the desired scale 

`P.grid(majorStep = 2)`


# Draw a (random) segment

`s1 = segment()`

`s1.draw()`

s1 is an object of "segment" class type. Two random points are generated and a segment pssing through is draw.


![Alt Text](pictures/straightLine.png)


print(s1)

shows all specifications of "s1" segment type instance.


## Draw a specific straight line

**Draw a line from angular coefficient and intercept**

First of all delete all speciments of s1 instance

`s1.erase()`

`s1.angCoeff = 1`

`s1.intercept = 10`

`s1.draw("s1") = 10`

(the optional "s1" string passed into the .draw() method is the straight line name)

**Draw a line passing through two different point: A and B respectively**


`A = point(3, 6)`

`B = point(-2, 1)`


`s1.erase()`

`s1.point[0] = A

`s1.point[1] = B`

`s1.draw("s1")`

in case you need a straight line (the optional "s1" string passed into the .draw() method is the straight line name). 

Otherwise 

`s1.draw("s1", cut = True)`

in case you need a segment in between A and B



**Draw a line passing through one point, say point A, and having a specific angular coefficient**

`A = point(3, 6)`

`s1.erase()`

`s1.point[0] = A

`s1.angCoeff = -1

`s1.draw("s1")`

**Draw a line passing through one point, say point A, and having a specific y-intercept**

`A = point(3, 6)`

`s1.erase()`

`s1.point[0] = A

`s1.intercept = -1

`s1.draw("s1")`



![Alt Text](pictures/straightLine2.png)


# Draw a (random) circumference

As a further example, say you want to draw a circumference.
Firstly define a circumference type instance which I suggest you to call 'C1' as follows

`C1 = circumference()`

Once the "C1" instance is created, than use the "draw" method as follows

`C1.draw()`


![Alt Text](pictures/circumferenceDrawn.png)


by typing 

`print(C1)`

you can see all details of your circumference instance: attributes and methods.

![Alt Text](pictures/circumferenceDraw_withGrid.png)


Now you want "C1" instance being not just a random circumference, but you want to choose both it's center position and it's radius. First of all, you need to know attributes, instances and plot settings of "C1" instance, than


`print(C1)`


![Alt Text](pictures/print_C1_screenshot.png)

you can change details such as the color just by typing


`C1.color = 'red'`

or 

`C1.color = 'r'`

Once the attribute is going to be changed, than use again the "draw" method

`C1.draw()`

![Alt Text](pictures/changeColor.png)




## Draw a specific circumference

In the some way you can change the radius size or you can add a name 


`C1.radius = 4`

`C1.name = "first circumference"`

`C1.draw()`

"center" is an instance of point class which is conteined into C1 instance. This means that typing


`print(C1.center)`

You gonna have a list of all Attributes, methods and settings related to the C1.center instance



![Alt Text](pictures/printC1center.png)


you can change the center coordinates by typing

`C1.center.coords = [2, 5]`

`C1.draw()`


![Alt Text](pictures/circumferenceDraw2.png)


# Change color

Say you have drawn a circumference by using a "circunference method" named "C1". To change it's color to red type this

`C1.draw( color = 'red')`

![Alt Text](pictures/circumferenceDrawRed.png)

to change to "black" type

`C1.draw( color = 'black' )`



# Draw a (random) Parabola


`P1 = parabola()`

P1 is an object of "parabola" class type which choose random values for the parabola parameters:

- x-shift (P1.xShift)

- y-shift (P1.yShift)

- concavity (P1.concavity)

`P1.draw()`

P1.draw() draws the geometrical locus

![Alt Text](pictures/parabola.png)


## Draw a specific parabola

choose an x-Shift of 

`P1.xShift = 5`

choose a y-Shift of 0

`P1.YShift = 0`

choose a concavity equal to 0.5

`P1.concavity = 0.5`

draw the parabola

`P1.draw()`

![Alt Text](pictures/parabola2.png)
