import random
import matplotlib.pyplot as plt
NUM_POINTS = 10000

# Randomly generate points (x[i], y[i]) such that -1 <= x[i] = 1 and -1 <= y[i] <= 1.
x = [random.uniform(-1,1) for i in xrange(NUM_POINTS)]
y = [random.uniform(-1,1) for i in xrange(NUM_POINTS)]

circle_x = []
circle_y = []

outsiders_x = []
outsiders_y = []

# Determine which points are inside the circle (and for visualization purposes, also
# determine which are outside the circle).
for i in xrange(NUM_POINTS):
    if x[i]**2 + y[i]**2 <= 1:
        circle_x.append(x[i])
        circle_y.append(y[i])
    else:
        outsiders_x.append(x[i])
        outsiders_y.append(y[i])

# Plot it.
fig = plt.figure()
fig.set_size_inches(10, 10)
plt.scatter(outsiders_x, outsiders_y, s=1, color='green')
plt.scatter(circle_x, circle_y, s=1, color='red')

print "Estimate of area of circle (pi):", 4 * (len(circle_x)*1.0 / len(x))

plt.show()
