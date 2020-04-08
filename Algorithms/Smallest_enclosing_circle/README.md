# Smallest Circle

The challenge is to design an algorithm in python that is finding the smallest circle around a cluster of points in 2D.
Input data is an array of points, each point consists of a X and a Y coordinate. (example data below)
By default, a random number of random points should be generated with each call of the script (25 to 60 points, x/y in range -15.0 to +15.0).
The circle is defined with a center point (consisting of a X and a Y coordinate) and a radius.
All points must be within this circle, while the radius of this circle should be as small as possible.
The output results should be plotted on a 2D plane, with all points and the result circle.
This challenge is only considering two dimensions, X and Y.

## Observation

A smallest circle has three points on its boundary, or only two in which case they are opposite to each other (i.e circle's diameter)

#### Find Circle with three points

- Given three points `(x1, y1), (x2, y2) and (x3, y3)`, we should find the circle's center and radius

- Equation of circle in general form is `x² + y² + 2gx + 2fy + c = 0` and in radius form is `(x – h)² + (y -k)² = r²`, where `(h, k)` is the center of the circle and r is the radius.

- substitute the three known points, getting 3 equations in 3 unknowns g, f, and c
`````
x1^2 + y1^2 + 2gx1 + 2fy1 + c = 0
x2^2 + y2^2 + 2gx2 + 2fy2 + c = 0
x3^2 + y3^2 + 2gx3 + 2fy3 + c = 0
``````

- solve the three equations with each other and find g, f and c => (circle's center and radius)

#### Find Circle with two points

- Circle that intersects 2 points where the points are the circle diameter,  For this case, the circle’s centre should be the midpoint of a and b and the radius should be half of the distance ab


## Files

- find_circle.py: Contains two functions, one to find the circle with two points and the other to find the circle with three points.

- start.py: start the program, generate random points, find the smallest circle and plot it with the points

- requirements.txt: Contain a list of dependencies to be installed, use the command to install all of dependencies `pip install -r requirements.txt`

## Run

- Install all of dependencies `pip3 install -r requirements.txt`

- Run `python start.py`
