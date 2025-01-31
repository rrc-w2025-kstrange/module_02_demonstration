"""
Description: Standard Operators
Author: KSG
Date: Jan 25
Usage: 
"""

# + (Addition)
# Adds two numbers or concatenates two strings
result = 5 + 5 # Adds 5 and 5, resulting in 10

# + also concatenates strings, resulting in "John Doe"
full_name = "John" + "" + "Doe"

# - (Subtraction)
# Subtracts the second number from the first
result = 10 - 5 # Subtracts 5 from 10, resulting in 5

# * (Multiplication)
# Multiplies two numbers
result = 14 * 3 # Multiplies 14 and 3, resulting in 42

# / (Division)
# Divides the first number by the second, result is a float
result = 42 / 4 # Divides 42 by 4, resulting in 10.5
print("/", result) # Output is / 10.5

# // (Floor Division)
# Performs division and returns the integer part (floors the result)
result = 42 // 4 # Divides 42 by 4 and floors the result, resulting in 10
print("//", result) # Outputs: // 10

# % (Modulus)
# Returns the remainder of the division
result = 100 % 55 # 100 divided by 55 leaves a remainder of 45
print("%", result) # Outputs: % 45

# ** (Exponentiation)
# Raises the first number to the power of the second
result = 2 ** 4 # 2 raised to the power of 4, resulting in 16
print("**", result) # Outputs: ** 16
