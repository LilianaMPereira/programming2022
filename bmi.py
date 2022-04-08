"""
Weekly Tasks 02
1. Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

The inputs are the person's height in centimetres and weight in kilograms.
The output  their BMI (You may need to look up how this is calculated)
$ python bmi.py
Enter weight(kg): 65
Enter height(cm): 180
The BMI is (kg/m2) 20.06.


This program is a simple calculation, with a formula already determined for the BMI Calculation.

The user has to enter the data using the requested unit of measure, in this case he enters the height in centimeters and the weight in kilograms.

In order to fit the correct parameter (if obese, healthy, etc.), the value for each of them must be determined.

"""

# This program calculate the BMI (Body Mass Index) Formula and is the Weekly Task 02
# Information about how calculate the BMI in Pyton:https://www.askpython.com/python/examples/bmi-calculator


height = float(input("Enter height (cm): "))
weight = float(input("Enter weight (kg): "))

BMI = weight / (height/100)**2

print(f"You BMI is {BMI}")

if BMI <= 16:
    print("Underweight.")
elif BMI <= 25:
    print("Healthy Weight.")
elif BMI <= 30:
    print("Over weight.")
elif BMI <= 35:
    print("Obesity I.")
elif BMI <= 40:
    print("Obesity II.")
else:
    print("Obesity III.")