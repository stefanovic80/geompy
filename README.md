**As the project is rapidly evolving, the present README file is only a rough explanation of how does it work. Hopefully a complete README file will be completed soon**


This is meant to be the occasion for high school students to start over computer programming for scientific applications with Python. Particularly, it's a tool for visualizing geometric loci by such as

 

### - [circumference](#draw-a-random-circumference)

### - [ellipse] (#draw-a-random-ellipse)

### - [segment](#draw-a-random-straight-line)

### - [parabola](#draw-a-random-parabola)


# Installation

Ensure you have matplotlib, random and numpy libreries installed on a fully working Ipython environment. Download the present project, than open a console and move to the analyticGeometry folder, where the main.py is located. Run the python intepreter, (type "ipython") and type

`run main.py`

![Alt Text](pictures/pythonInterpreter.png)


In case of different python libraries versions, dysfunctions may accur. In this case create a 'analyticGeomEnv' conda environment (it may take time, depending on internet connection speed)

`conda env create -f analyticGeomEnv.yml`

Once the job is done than activate it

`conda activate analyticGeomEnv`

and try again

`run main.py`

and choose a minimum (xmin) and a maximum (xmax) value for coordinates axes. In this case 

`xmin`
`-20`

`xmax`
`20`

# Usage

# Draw a (random) circumference

Each geometric locus is a python class. Say you want to draw a circumference, than you have to define a circumference type instance which I suggest you to call 'C1' as follows

`C1 = circumference()`

Once the "C1" instance is created, than use the "draw" method as follows

`C1.draw()`


![Alt Text](pictures/circumferenceDrawn.png)


You may want to add a grid with both x and y axes

`C1.grid()`

You may want to increase the grid density, than an N argument with values lower than 1 will do the job

`C1.grid(N = .5)`

by typiing 

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

`C1.plot( color = 'red')`

![Alt Text](pictures/circumferenceDrawRed.png)

to change to "black" type

`C1.plot( color = 'black' )`


# Delete a circumference

According with previous notes, we suppose the drawn circumference is a "C1" object. Than, type

`C1.remove()`

in order to erase the drawn circomference.





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

`L1.remove()`

erases the straight line you previously have drawn.

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

`P1.remove()`

erases the parabola you previously have drawn.






# How to see geometrical locus parameters
 
`C1.__dict__`

`P1.__dict__`

`L1.__dict__`

