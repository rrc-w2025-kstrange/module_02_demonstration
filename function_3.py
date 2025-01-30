"""
Description: formatting a float and an integer using f-string
Author: KSG
Date: Jan 25
Usage:
"""

# The print() function and f-strings formatting a float.
value = 3.14959
print(f"The value is {value:.2f}.") #round to 2 decimals

# The print() function and f-strings formatting an integer.
number = 123
print(f"The number is {number:05}.") #zero-padded to 5 places
