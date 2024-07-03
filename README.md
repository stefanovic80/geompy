**As this project is rapidly evolving, the current README file provides only a preliminary explanation of its functionality and operation. Hopefully, an accurate and comprehensive README file will be available soon.**


The present project, primarily built on top of matplotlib and numpy python libreries, is designed specifically for fast and easy geometric loci visualization with python.

Although there are already many existing standalone applications such as GeoGebra, the different concept of the present project makes it suitable as a valuable tool for coding learning. 

 
In fact, while there are numerous Python libraries and software tools available for scientific purposes, many of them are often too much complex and challenging; which makes them prohibitive for educational use. 


As I personally believe that coding is a skill that can be acquired only by tackling real tasks rather than through simple exercises, the present project is intended to be a valuable occasion to introduce students to computer programming with python, while supporting them with their mathematical tasks.

# Installation and start up

Make sure you have matplotlib, random and numpy libraries installed on a fully working Ipython environment. Download the present project and rename it's folder with "geompy".


Open a console, move it where the geompy folder is located, start off an ipython session and import all modules

`from geompy import *`


a new window with a Cartesian plane comes up

![Alt Text](pictures/pythonInterpreter.png)
 

If everything works fine, than jump over next section. In case of any error message, due to any package version mismatch, than you need to create a 'analyticGeomEnv' conda environment. So, go back to your OS console, on the "analyticGeometry" folder and type

`conda env create -f analyticGeomEnv.yml`

`conda activate analyticGeomEnv`.

(it may take time, depending on the available connection speed). Once activated, try again to run main.py on your ipython interpreter, as previously explained.




# Usage


After loading geompy into IPython, let's consider drawing a circumference. You can create a "circumference" type instance, labeled "c", by typing:

`c = circumference()`

Here "c" is a python variable, simultaneously a circumference with random center coordinates and a random radius value is drawn in the plot window.


![Alt Text](pictures/circumference.png)


by typing


`c.radius = 4`


the .radius attribute of the "c" instance is being modified. Should you need your "c" circumference centered at P(1, 2) and having a thin line width, than you can modify its corrispective attributes accordingly:


`c.center = point(1, 2)`

`c.linewidth = 1`




# Draw points and lines

As further examples you can generate two points and a line by typing


`A = point() #random coordinates`

`B = point(3, 4)`

`l = line()`

and you can modify them by typing


`A.x = -2`

`l.m = -1`

`l.q = 1.2`

where "l.m" and "l.q" are the angular coefficient and the intercept respectively.




- Select randomly a point among the ones of the "c" geometrical locus

`P = point(c)`


- Choose a point by mouse click:

the .click method, allows the user to manually select the point with the mouse. It has to be called two times:


`P.click("P")`










**Draw a line from angular coefficient "m" and intercept "q"**


`l1 = line()`

`l1.m = 1`

`l1.q = -2`

`l1.name = "l1"`



![Alt Text](pictures/lineDraw_m_q.png)

**Draw a line passing through two different point: A and B respectively**


`A = point(3, 4)`

`A.name = 'A'`

`B = point(-2, 1)`


`l2 = line()`

`l2.name = "l2"`


`l2.points = A`

`l2.points = B`


`l2.name = "l2"`

![Alt Text](pictures/line_through_A_B.png)

**Draw a line passing through one point, say point A, and having a specific angular coefficient "m"**


`l3 = lines()`

`l3.points = A`

`l3.m = -1`

`l3.name = "l3"`

![Alt Text](pictures/line_through_A_m.png)

**Draw a line passing through one point, say point A, and having a specific y-intercept "q"**

`l4 = line()`

`l4.points = A`

`l4.q = -1`

`l4.name = "l4"`


![Alt Text](pictures/line_through_A_q.png)


























# Geometrical loci classes and attributes managing 

Here a comprensive list of all classes available in geompy


`point()`

`line()`

`parabola()`

`ellipse()` (still to be further improved!)

`hyperbole()` (still to be developed!)

`function()`

`triangle()`

`arc()`

and here some examples about how they can be used


`A = point(-8, 1)`

`A.name = 'A'`

`l = line()`

`l.name = 'l'`

`p = parabola()`

`p.vertex = point(0, 1)`

`f = function()`

`f.y = x**3/(x+1)`

`f.name = 'f'`

`t = triangle()`




![Alt Text](pictures/comprensive.png)
















Each geompy class has attributes which set it's geometrical specifications. Some of these attributes available are the some for all types of classes (such as .color or .linewidth), while others are specific of the type of geometrical locus (such as .radius and .center). To view a comprehensive list of attributes that can be modified, simply type:

`print(c)`






![Alt Text](pictures/circumference_02.png)

As an example, one of the listed attributes is "color," allowing you to set the color of the circumference:

`c.color = "blue" # or simply c.color = "b"`


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



This flexibility extends to drawing and managing all other geometrical loci which are available as geompy classes and can be found from the list of ipython variables








# Change geometrical loci parameters


Explore the following examples:


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





![Alt Text](pictures/parabola_vertex00.png)





# Data visualization

- A numbered list of all points coordinates calculated into c instance

`c.points `

- A list of all x values calculated into c instance

`c.x`


- A list of all y values calculated into c instance

`c.y`


# Parabola/circumference passing through three points

Draw a circumference/parabola passing through three points:

`A = point(4, 1)`

`B = point(1, 6)`

`C = point(-2, -4)`


`c1 = circumference()`

`c1.points = A`

`c1.points = B`

`c1.points = C`



![Alt Text](pictures/circumferenceThroughA_B_C.png)


# Line tangent to a circumference and passing through a given point


`P = point(8, 2)`


`t1 = c1.tangent(P)`

`t2 = c1.tangent(P)`

![Alt Text](pictures/linesTangent.png)








# Labeling

You can choose a simple string type labeling or even a latex formula, as follows

`P.name = "P"`

`A.name = "A"`

`B.name = "B"`

`C.name = "C"`

`c.name = "c"`

`c1.name = "c1"`

`p.name = "p"`


or

`c1.name = r"$(x -1 )^2 + (y - 2)^2 = 16$"`


`P.name = "P(8, 2)"`







![Alt Text](pictures/labeling.png)







# Cut Off data

Let consider a straight line with angular coefficient 0.2 and intercept 1.2:

`l1 = line()`

`l1.m = .2`

`l1.q = 1.2`

by typing

`l1.X.cut = -4`

all points with x value before -4 are removed, by typing again

`l1.X.cut = 2`

all poits with x values after 2 are removed

![Alt Text](pictures/cutLine.png)










# Arcs drawing

The arc class takes two lines as argument



`l0 = line()`

`l1 = line()`

`l0.m = 1`

`l0.m = -1.2`

`l0.q = -.5`

`l1.q = -2.2`

`alpha = arc(l0, l1)`

`alpha.size`

![Alt Text](pictures/angle0.png)

by typing

`alpha.draw()`


![Alt Text](pictures/angle1.png)

# Plot settings

Choose one of the instances you have used so far (in this example P) and change the plot size and grid as follows

- `P.lower = -20`

set both left and bottom coordinates to -20

- `P.higher = 20`

set both right and up coordinates to -20

- `P.step = 2`

set major grid step to 2

- `P.steps = 20`

set the number of minor steps in between two adjacent major steps to 20

![Alt Text](pictures/grid.png)



Let say you need to adjust limits of X only coordinate or Y only coordinate.


`f1 = function()`

`f1.y = log10(x)`

`f1.X.lower = -.1`

`f1.Y.lower = -2`

`f1.Y.higher = 1.2`

![Alt Text](pictures/log.png)


# Rotation


`p = parabola()`

`p.concavity = -1.2`

`p.vertex = point(0, 1)`

`A = point(4, 2)`

`A.name = 'A'`

![Alt Text](pictures/parabola_toBeRotated.png)

`A.rotation(p, angle = -pi/3)`

![Alt Text](pictures/parabolaRotated.png)





# Draw a (random) circumference

As a further example, say you want to draw a circumference.
Firstly define a circumference type instance which I suggest you to call 'C1' as follows

`c = circumference()`


![Alt Text](pictures/circumferenceDrawn.png)


by typing 


Now you want to see details of "c" instance. By typing


`print(c)`

all c details are available

![Alt Text](pictures/print_C1_screenshot.png)

here how to change its attributes


`c.color = 'red'`

or simply

`c.color = 'r'`

Once the attribute is going to be changed, than use again the "draw" method

`c.name = "c1"`

![Alt Text](pictures/changeColor.png)




## Draw a specific circumference

In the some way you can change the radius size or you can add a name 


`c.radius = 4`

`c.name = "first circumference"`

"center" is an instance of point class which is conteined into C1 instance. This means that typing


`print(c.center)`

You gonna have a list of all Attributes, methods and settings related to the C1.center instance



![Alt Text](pictures/printC1center.png)


you can change the center coordinates by typing

`c.center = point(2, 5)`

`c.name = "c"`


![Alt Text](pictures/circumferenceDraw2.png)


# Change color

Say you have drawn a circumference by using a "circunference method" named "c". To change it's color to red type this

`c.color = "red"`

![Alt Text](pictures/circumferenceDrawRed.png)

to change to "black" type

`c.color = 'black'`



# Draw a (random) Parabola


`p1 = parabola()`

p1 is an object of "parabola" class type which choose random values for the parabola parameters:

- x vertex coordinte (p1.vertex.x)

- y vertex coordinate (p1.vertex.y)

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
