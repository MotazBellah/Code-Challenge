#!/usr/bin/env python
import math
import random
import itertools
import matplotlib.pyplot as plt
import json
from find_circle import circle_three_points, circle_two_points

# Function to generate random points
def generate_points():
    # Get random no. of the points
    points_length = random.randint(25, 60)
    # Create Set to make sure the points are unique
    points_set = set()
    while len(points_set) < points_length:
        x_value = random.randint(-15, 15)
        y_value = random.randint(-15, 15)
        # create point as a dict
        point = {'x': x_value, 'y': y_value}
        # convert dict to JSON string to be able to add to set
        # sets only support storing hashable objects
        points_set.add(json.dumps(point))
    # Get the final result by convert each point to python dict
    return [json.loads(i) for i in points_set ]

# Function to draw the points and circle
# using matplotlib
def draw():
    points = generate_points()
    # Get x-points and y-points
    x = [i['x'] for i in points]
    y = [i['y'] for i in points]
    # Get x, y pair by merge the two list in tuple
    point = list(zip(x, y))

    fig, ax = plt.subplots()
    # Get the x,y center and the radius
    center_x, center_y, radius = smallest_circle(point)
    print(center_x, center_y, radius)
    # Plot the points on the 2D plane
    z = plt.scatter(x, y, color='r', s=8)
    # Plot the circle
    circle = plt.Circle((center_x, center_y), radius, color='b', fill=False)
    # Add the circle to the plane
    ax.add_patch(circle)
    # Save the image
    plt.savefig('img.png')


# Function to check whether a point lies inside
# or on the boundaries of the circle
def is_in_circle(c, p):
    # from circle eqn:
    # (x-xc)^2 + (y - yc)^2 <= radius^2
	return c is not None and math.hypot(p[0] - c[0], p[1] - c[1]) <= c[2]

# Function to check if all points lies inside
# or on the boundaries of the circle
def is_valid_circle(circle, points):
    for point in points:
        if not is_in_circle(circle, point):
            return False
    return True

# Function to find the smallest circle
def smallest_circle(points):
    # Intialize the circle
    circle = 0, 0, 1e14

    if len(points) == 0:
        return 0, 0, 0

    if len(points) == 1:
        return  points[0], points[1], 0

    # Go over all pair of points
    for pair in itertools.permutations(points, r=2):
        # Get the smallest circle that
        # intersects each pair
        c = circle_two_points(pair[0], pair[1])

        # Update circle if c encloses all points
        # and has a smaller radius
        if(c[2] < circle[2] and is_valid_circle(c, points)):
            circle = c

    # Go over all triples of points
    for triple in itertools.permutations(points, r=3):
        # Get the smallest circle that
        # intersects each triple
        try:
            c = circle_three_points(triple[0], triple[1], triple[2])
        except ZeroDivisionError:
            pass

        # Update circle if c encloses all points
        # and has a smaller radius
        if(c[2] < circle[2] and is_valid_circle(c, points)):
            circle = c

    return circle

if __name__ == "__main__" :
    draw()
