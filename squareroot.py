"""

Weekly task 6
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.


$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

"""

# This task is the Weekly Task 06
# This program takes a positive floating point number as input and outputs an approximation of its square root.
# Information that help be to solve this task: https://www.programiz.com/python-programming/examples/square-root ; https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python ; https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap04/sqrt.html ; https://www.youtube.com/watch?v=szQUIRPrAgQ
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ ; https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
# Import square root function from math module.
# Import getFloat function from pcinput.py to ensure input is a positive floating point number. 
# Method used requested is Newton's method

x = float(input('Please enter a positive number: '))


if x < 0:
    print (" The input is a negative number")
    
    x = abs(x)
    print ("Get the positive value for the input: ", x)

def sqrt(x):
        
        n = x 

        while abs(x*x - n) > 0.001:            
            x = x - ((x*x - n)/(2*x)) # method Newton-Raphson equation
        return x

# result with 1 decimals
print ("The square root of ", x , "is approx. ", round(sqrt(x),1))
