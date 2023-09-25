**As this project is rapidly evolving, the present README file is only a rough explanation of what it does and how does it work. Hopefully an exact and complete  README file will be available soon**



It's already plenty of python libreries and other software dealing with scientific purposes, however their complexity often make them proibitive for any didactical use.

This project, mainly built on top of matplotlib and numpy, is a python library for fast geometric loci visualization. This is meant to be the occasion for high school students and their professors, dealing with geometrical loci drawings, to start over computer programming for scientific applications with Python. 




# Installation and start up

Ensure you have matplotlib, random and numpy libreries installed on a fully working Ipython environment. Download the present project, than open a console and move to the folder where the main.py file is located; which is "analyticGeometry". Run the ipython intepreter (type "ipython"), and type

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

command shows the list of all the available python variables and classes 

![Alt Text](pictures/who.png)


In analyticGeometry for each representable geometric locus there is an associated python class which has the some name. Here the actually available classes

### - [point](#draw-a-point)

### - [circumference](#draw-a-random-circumference)

### - [ellipse] (#draw-a-random-ellipse)

### - [segment](#draw-a-random-straight-line)

### - [parabola](#draw-a-random-parabola)



If you want to draw a point type geometrical locus, than you have to define a point class type instance. 


If you want to draw a segment type geometrical locus, than you have to define a segment class type instance. 


# Draw a point

Let's draw a point in a cartesian plane. Firstly define a point class type instance and draw a point

`P = point()`

`P.draw()`

as no arguments are in between the brackets, than coordinates are randomly choosen, and no names figures on the plot.

with

`print(P)`

all details of P instance are reported. Furthermore, you can change the point color


`P.color = 'blue'`

`P.draw()`


Alternatively coordinates and name can choosen as point() and draw() arguments respectively


`P_1 = point(3, -9)`

`P_1 = draw("P_1")`

You may want to add both a grid and x and y axes

`P.grid()`

by typing it more times, you gonna increase grid density or dropped it down if -1 argument is added

`P.grid(-1)`

otherwise use the majorStep argiment to set the desired scale 

`P.grid(majorStep = 2)`


# Draw a (random) segment

`L1 = segment()`

`L1.draw()`

L1 is an object of "segment" class type. Than a segment with random values for both angular coefficient and intercept is drawn. 


![Alt Text](pictures/straightLine.png)


## Draw a specific straight line

Delete all speciments of L1 instance

`L1.erase()`

by typing 

`print(L1)`

you know which attributes to fill up in order to draw a specific segment. Say you want to draw a segment from it's angular coefficient and intercept and you want to call it "L1"

`L1.angCoeff = 6`

`L1.intercept = 10`

`L1.draw("L1") = 10`


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



according with matplotlib library, you can choose the color you like more from the following list


- ``'b'``          blue

- ``'g'``          green

- ``'r'``          red

- ``'c'``          cyan

- ``'m'``          magenta

- ``'y'``          yellow

- ``'k'``          black

- ``'w'``          white


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
