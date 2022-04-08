""""
Weekly task 4

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.


$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1
"""

# This task is the Weekly Task 04
# This program request to the user to input input any positive integer and outputs the successive values of the following calculation. 
# Information about Python Program to test Collatz Conjecture for a Given Number found on: https://codingdeekshi.com/python-program-to-test-collatz-conjecture-for-a-given-number/ ; https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/.




while True:
    try:
        InputValue = int(input("Enter a positive integer: ")) 
      
        if InputValue < 0:
           raise ValueError   
        break  
    except ValueError:

        print("That's not a positive integer. Try again!")


OutputSerie =[InputValue]
while  InputValue > 1:
   
    if InputValue % 2 == 0:  
        InputValue = InputValue //2
     
        OutputSerie.append(InputValue)
        
 
    else:
        InputValue = (InputValue * 3) + 1
         
        OutputSerie.append(InputValue)

print("This is the sequence: " )
print( OutputSerie)