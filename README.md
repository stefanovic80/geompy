**As this project is rapidly evolving, the current README file provides only a preliminary explanation of its functionality and operation. Hopefully, an accurate and comprehensive README file will be available soon.**


The present project, primarily built on top of matplotlib and numpy python libreries, is designed specifically for fast and easy geometric loci visualization with python.

Although there are already many existing standalone applications such as GeoGebra, the different concept of the present project makes it suitable as a valuable tool for coding learning. 

 
In fact, while there are numerous Python libraries and software tools available for scientific purposes, many of them are often too much complex and challenging; which makes them prohibitive for educational use. 


As I personally believe that coding is a skill that can be acquired only by tackling real tasks rather than through simple exercises, the present project is intended to be a valuable occasion to introduce students to computer programming with python, while supporting them with their mathematical tasks.

# Installation and start up

Make sure you have matplotlib, random and numpy libraries installed on a fully working Ipython environment. Download the present project.


Open a console, move it where the geompy folder is located, start off an ipython session and import all modules

`from geompy import *`


a new window with a Cartesian plane comes up

![Alt Text](pictures/pythonInterpreter.png)
 

If everything works fine, than jump over next section. In case of any error message, due to any package version mismatch, than you need to create a 'analyticGeomEnv' conda environment. So, go back to your OS console, on the "analyticGeometry" folder and type

`conda env create -f analyticGeomEnv.yml`

`conda activate analyticGeomEnv`.

(it may take time, depending on the available connection speed). Once activated, try again to run main.py on your ipython interpreter, as previously explained.




# Usage


Once geompy is loaded into ipython, say you want to draw a circumference, than you must type

`c1 = circumference()`


and a circumference with random center and radius is drawn into the plot window

![Alt Text](pictures/circumference.png)




here "c1" is a python variable. More precisely, it's a "circumference" class type instance. Say you need a circumference centered in P(1, 2) having a radius r = 4, than


`c1.center = point(1, 2)`

`c1.radius = 4`

by typing

`print(c1)`

You gonna have a list of all Attributes, methods and settings related to the c1 which can be changed by the user


![Alt Text](pictures/printC1center.png)

as an example, one of the attributes reported here is color, which means that by typing


`c1.color = "blue"`

or simply

`c1.color = "b"`


you can set the color you like more. 

In the some manner you can draw and mangage all other geometrical loci; as in the following examples

### - [point](#draw-a-point)

`P = point()`

`P.y = -5`

### - [circumference](#draw-a-random-circumference)

`c = circumference()`

`c.linewidth = 1`

### - [ellipse] (#draw-a-random-ellipse)

`el = ellipse()`

### - [line](#draw-a-random-straight-line)

`l = line()`

`l.m = -1.4`

### - [parabola](#draw-a-random-parabola)

`p = parabola()`

`p.vertex = point(0, 0)`


 According with ipython syntax, the 

`who`

command shows a complete list of all variables currently in use, which includes all classes loaded from geompy 



![Alt Text](pictures/who.png)






# Labeling

You can choose a simple string type labeling or even a latex formula, as follows

`c1.name = "c1"`

or

`c1.name = r"$(x -1 )^2 + (y - 2)^2 = 16$"`


`P = point(4, 1)`

`P.name = "P"`

or

`P.name = "P(4, 1)"`



# Data visualization

A numbered list of all points coordinates calculated into c instance

`c.points `

A list of all x values calculated into c instance

`c.x`


A list of all y values calculated into c instance

`c.y`


# Cut Off data

Typing one time 

`c.cutOff = 150`

the first 150 points are removed. By typing it one more time

`c.cutOff = 100`

last 100 points are removed. In both cases points are removed both from the plot and from the instance itself.

# Draw a point


Random point (no arguments passed within the parentheses)

`A = point()`

A specific point, sai A(3; -9)

`A = point(3, -9)`

Change coordinates to (1; 7)

`A.x = 1`

`A.y = 7`


A random point among the ones of the "c" geometrical locus 

`P = point(c)`


Choose point with mouse:

the .click method, allows the user to manually select the point with the mouse. It has to be called two times: 


`P.click("P")`


# Plot settings

Choose one of the instances you have used so far (in this example P) and change the plot size and grid as follows

`P.left = -20`

`P.right = 20`

`P.majorStep = 2`

`P.minorSteps = 20`


![Alt Text](pictures/grid.png)





# Change geometrical loci parameters





When you create a Python instance like c = circumference(), it becomes a versatile object with various attributes, methods, and even instances of different classes. For instance, in the previous case of a circumference type instance, there is a point class instance in it, which is the center of the circumference. 

You can explore these attributes and methods by simply typing


`print(c)`


![Alt Text](pictures/printCircumference.png)



Each of these aspects can be customized by the user, as demonstrated in this example:

`c.radius = 7`

`c.color = 'blue'`

`c.center = point(0, 0)`


the .color attribute can be choosen from the following list

- ``'b'``          blue

- ``'g'``          green

- ``'r'``          red

- ``'azure'``      azure

- ``'m'``          magenta

- ``'y'``          yellow

- ``'k'``          black

- ``'w'``          white




![Alt Text](pictures/grid.png)


# Draw a (random) segment

`l1 = line()`


l1 is an object of "line" class type. Two random points are generated and a segment passing through is drawn.


![Alt Text](pictures/straightLine.png)





## Draw a specific straight line

**Draw a line from angular coefficient and intercept**

First of all delete all speciments of s1 instance

`l1.erase()`

`l1.m = 1`

`l1.q = 10`


`l1.name = "l1"`


**Draw a line passing through two different point: A and B respectively**


`A = point(3, 6)`

`B = point(-2, 1)`


`l1.erase()`

`l1.point[0] = [A, B]`





**Draw a line passing through one point, say point A, and having a specific angular coefficient**

`A = point(3, 6)`

`s1.erase()`

`s1.point = [A, None]`

`s1.m = -1`

`s1.name = "s1"`

**Draw a line passing through one point, say point A, and having a specific y-intercept**

`A = point(3, 6)`

`l1.erase()`

`l1.point = [A, None]`

`l1.q = -1`

`l1.name = "s1"`



![Alt Text](pictures/straightLine2.png)


# Draw a (random) circumference

As a further example, say you want to draw a circumference.
Firstly define a circumference type instance which I suggest you to call 'C1' as follows

`c1 = circumference()`


![Alt Text](pictures/circumferenceDrawn.png)


by typing 


Now you want to see detalils of "C1" instance. By typing


`print(c1)`

all C1 details are available

![Alt Text](pictures/print_C1_screenshot.png)

here how to change its attributes


`c1.color = 'red'`

or simply

`c1.color = 'r'`

Once the attribute is going to be changed, than use again the "draw" method

`c1.name = "C1"`

![Alt Text](pictures/changeColor.png)




## Draw a specific circumference

In the some way you can change the radius size or you can add a name 


`c1.radius = 4`

`c1.name = "first circumference"`

"center" is an instance of point class which is conteined into C1 instance. This means that typing


`print(c1.center)`

You gonna have a list of all Attributes, methods and settings related to the C1.center instance



![Alt Text](pictures/printC1center.png)


you can change the center coordinates by typing

`c1.center = point(2, 5)`

`c1.name = "c1"`


![Alt Text](pictures/circumferenceDraw2.png)


# Change color

Say you have drawn a circumference by using a "circunference method" named "c1". To change it's color to red type this

`c1.color = "red"`

![Alt Text](pictures/circumferenceDrawRed.png)

to change to "black" type

`c1.color = 'black'`



# Draw a (random) Parabola


`p1 = parabola()`

p1 is an object of "parabola" class type which choose random values for the parabola parameters:

- x-shift (p1.xShift)

- y-shift (p1.yShift)

- concavity (p1.concavity)


![Alt Text](pictures/parabola.png)


## Draw a specific parabola

choose an x-Shift of 

`p1.vertex.x = 5`

choose a y-Shift of 0

`p1.vertex.y = 0`

choose a concavity equal to 0.5

`p1.concavity = 0.5`

or

`p1.a = 0.5`

![Alt Text](pictures/parabola2.png)
