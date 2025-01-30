"""
Description: Strings methods
Author: KSG
Date: Jan 25
Usage: 
"""
# Strings are objects, we can use methods with them, dot notation
original_string = "hello, world!"

# capitalize() converts the first character of a string to uppercase
original_string = original_string.capitalize() # "Hello, world!"
print(original_string)

# center(): center-aligns a string within a specified width
width = 30
fill_char = '-'
centered_string = original_string.center(width, fill_char)
print(centered_string)

# startswith() returns a true if the string starts with specified prefix
is_hello = original_string.startswith("Hello") #True
print(is_hello)

# endswith() returns a true if the string endswith specified suffix.
is_world = original_string.endswith("World") # False
print(is_world)

# converts the string to uppercase
uppercase = original_string.upper() # HELLO, WORLD!
print(uppercase)

# converts the string to lowercase
lowercase = uppercase.lower() # hello, world!
print(lowercase)

# replace(): replaces all occurrences of a substring within another substring
original_string = "hello, world!  hello, python"
replaced_string = original_string.replace("hello", "hi")
print(replaced_string)


