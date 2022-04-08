"""
Weekly Task 03

Write a program that asks a user to input a string and outputs every second letter in reverse order.

$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.
.o zletrv pu o wr cu h

"""

# This task is the Weekly Task 03
# This program request to the user to asks the user to input any positive integer 
# information on reversing a string found on: https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# using the [-2] instruction as requested in the task
# to move every 2 and put back

sentence = input("Enter the a sentence:")
print(sentence[::-2])

