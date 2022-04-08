
"""
Weekly task 07

Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

$ python es.py moby-dick.txt
116960

"""

# This task is the Weekly Task 07
# This program reads in a text file and outputs the number of e's it contains.
# Information that help be to solve this task: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-7.php ; https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

nameFile = input("Name file: ")

Symbol = input("Pick a Symbol ")

freq = 0
with open (nameFile, "r") as myfile:
    data = myfile.read().replace('\n', '')
    print(data)
    freq = 0
    for char in data:
        if char == Symbol:
            freq = freq + 1
    print(freq)
