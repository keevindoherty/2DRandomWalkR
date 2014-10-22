"""Generates a text file of all the steps for a random walk.

This is my Python implementation of the Perl code found on
Vincent Granville's blog post about 2D Random Walks in R
for producing the necessary random walk data set.
"""

import random

x = 0
y = 0
max_x = -1
max_y = -1
min_x = 999999999
min_y = 999999999

m = 200
n = 200
niter = 2000
end = 400000
ax = [0]*end
ay = [0]*end

# end must be > niter * m

extremes = open("extremes.txt", "w")
for k in range(0,end):
    ax[k] = x
    ay[k] = y
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    extremes.write("%d\t%d\t%d\t%d\n" % (max_x, max_y, min_x, min_y))
    rnd1 = -.5+random.random()
    rnd2 = -.5+random.random()
    x += rnd1
    y += rnd2
extremes.close()

rw = open("rw.txt","w")
rw.write("iter\tx\ty\n")
for it in range(0,niter):
    for k in range(0,n):
        idx = m*it + k
        rw.write("%d\t%d\t%d\n" % (it, ax[idx], ay[idx]))
rw.close()
print("%d | %d | %d | %d\n"  % (min_x, max_x, min_y, max_y))
