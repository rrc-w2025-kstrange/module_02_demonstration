"""
Description: # Tuples
Author: KSG
Date: Jan 25
Usage: 
"""

# Tuples
# Accessing Tuple Elements
# Accessing by Index:
Provinces_and_territories = ('BC', 'AB', 'MB', 'SK', 'ON', 'QC', 'NB', 
                             'NL', 'NS', 'PE', 'NT', 'NU', 'YT')
manitoba = Provinces_and_territories[2]
print(manitoba) # Output: MB
# Retrieves the value at index 2 of the tuple.


# Tuples are Immutable:
# The following line of code causes an exception:
# provinces_and_territories[2] = "Manitoba"
##### TypeError: 'tuple' object does not support item assignment
# Tuples cannot be modified once created.


# Creating New Tuples
# Concatenation:
letters = ('a', 'b', 'c')
numbers = (1, 2, 3)
letters = letters + ('d',)
letters_and_numbers = letters + numbers
print(letters_and_numbers) # Output: ('a', 'b', 'c', 'd', 1, 2, 3)
# You can concatenate tuples to create new ones.


# Tuple Functions:
# Length, Max, Min, Sum, and Sorting:
random_tuple = (1, 66, 3, 7, 42, 78, 12, 55)
length = len(random_tuple)
print(length) # Output: 8

max_value = max(random_tuple)
print(max_value) # Output: 78

min_value = min(random_tuple)
print(min_value) # Output: 1

sum_value = sum(random_tuple)
print(sum_value) # Output: 264

sorted_tuple = sorted(random_tuple)
print(sorted_tuple) # Output: [1, 3, 7, 12, 42, 55, 66, 78]
# sorted() function sorts increasing

# Creating tuples from Other Sequences:
name = "John"
tuple_name = tuple(name)
print(tuple_name) # Output: ('J', 'o', 'h', 'n')

list_of_numbers = [1, 2, 3]
tuple_of_numbers = tuple(list_of_numbers)
print(tuple_of_numbers) # Output: (1, 2, 3)



