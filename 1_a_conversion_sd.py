"""
Description: implicit and explicit type conversions
Author: KSG
Date: Jan 25
Usage: 
"""

age = 25
print(type(age))

current_salary = 67293.21

# Implicit casting
age_and_salary = age + current_salary
print(type(age_and_salary))

months_old = "11"
years_old = 25

# Explicit casting
age = float(years_old) + (float(months_old) / 12)
print("Age as a float:", age)

age = int(age)
print("Age as an int:", age)