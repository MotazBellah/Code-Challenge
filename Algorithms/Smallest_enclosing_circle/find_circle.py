#!/usr/bin/env python
import math

# Function to return the smallest circle
# that intersects 2 points where the points are the circle diameter
def circle_two_points(a, b):
	# circle's center should be the midpoint between a and b
	# radius should be the half of distance a and b
	x = (a[0] + b[0]) / 2.0
	y = (a[1] + b[1]) / 2.0
	r0 = math.hypot(x - a[0], y - a[1])
	r1 = math.hypot(x - b[0], y - b[1])
	return (x, y, max(r0, r1))

# Function to find the circle on
# which the given three points lie
# The General Form of the equation of a circle is x2 + y2 + 2gx +2fy + c = 0.
# The centre of the circle is (-g, -f) and the radius is √(g2 + f2 - c).
# put each coordinates in eqn of the circle
# then we have three equations with three nuknown variable (g, f, c)
# solve the three equations with each other
# and find g, f and c => (circle's center and radius)
def circle_three_points(a, b, r):
	# Unpack the each pair
    x1, y1 = a
    x2, y2 = b
    x3, y3 = r

    x12 = x1 - x2
    x13 = x1 - x3

    y12 = y1 - y2
    y13 = y1 - y3

    y31 = y3 - y1
    y21 = y2 - y1

    x31 = x3 - x1
    x21 = x2 - x1

	# x1^2 - x3^2
    sx13 = pow(x1, 2) - pow(x3, 2)
    #
	# y1^2 - y3^2
    sy13 = pow(y1, 2) - pow(y3, 2)

    sx21 = pow(x2, 2) - pow(x1, 2)
    sy21 = pow(y2, 2) - pow(y1, 2)

    f = (((sx13) * (x12) + (sy13) *
	    (x12) + (sx21) * (x13) +
		(sy21) * (x13)) / (2 *
	    ((y31) * (x12) - (y21) * (x13))));

    g = (((sx13) * (y12) + (sy13) * (y12) +
	    (sx21) * (y13) + (sy21) * (y13)) /
	    (2 * ((x31) * (y12) - (x21) * (y13))))

    c = (-pow(x1, 2) - pow(y1, 2) -
	     2 * g * x1 - 2 * f * y1)


	# circle center
    h = -g
    k = -f
	# radius r as r^2 = h^2 + k^2 - c
    sqr_of_r = h * h + k * k - c

	# r is the radius
    r = math.sqrt(sqr_of_r)

    return h, k, r
