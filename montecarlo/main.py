# import libraries
import numpy as np

# initialize variables
n_simulations = 100000
n_points_circle = 0
n_points_square = 0

# create lists to store x and y values
l_xs = []
l_ys = []

# loop n_simulations times
for _ in range(n_simulations):

    # x is randomly drawn from a continuous uniform distritbuion
    x = np.random.uniform(-1, 1)
    # store x in the list
    l_xs.append(x)

    # y is randomly drawn from a continuous uniform distribution
    y = np.random.uniform(-1, 1)
    # store y in the list
    l_ys.append(y)

# loop n_simulations times
for i in range(n_simulations):

    # calculate the distance between the point and the origin
    dist_from_origin = l_xs[i] ** 2 + l_ys[i] ** 2

    # if the distance is smaller than or equal to 1, the point is in the circle
    if dist_from_origin <= 1:
        n_points_circle += 1

    # by definition of the uniform distribution, the point is in the square
    n_points_square += 1

# estimate the value of pi
pi = 4 * n_points_circle / n_points_square
print(pi)
