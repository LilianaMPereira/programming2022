"""
Weekly Task 08

Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4] on the one set of axes.

Some marks will be given for making the plot look nice.

"""

# This task is the Weekly Task 08
# This program displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4] on the one set of axes.
# Information that help be to solve this task: https://www.w3schools.com/python/matplotlib_intro.asp ; https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html


import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(0,4,100)

# the function, which f(x)=x here
y1 = x

# the function, which is g(x)=x^2 here
y2 = x**2

# the function, which is h(x)=x^3 here
y3 = x**3

# setting the axes at the centre
fig = plt.figure()


# plot the function
plt.plot(x,y1, 'r',  label='f(x)=x')

# plot the function
plt.plot(x,y2, 'b',  label='g(x)=x^2')

# plot the function
plt.plot(x,y3, 'g',  label='h(x)=x^3')

plt.legend()

plt.xlabel('X')
plt.ylabel('Y')

plt.show()


