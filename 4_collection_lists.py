"""
Description: Lists
Author: KSG
Date: Jan 25
Usage: 
"""

# A list of integers.
daily_step_count = [10343, 9385, 7029, 10931, 5921]

# A list of mixed data values.
employee_data = ["A123", 55024.23, 595, True]

# A list of lists.
list_of_lists = [["A", "B", "C"], [1, "x", True], [False, 12, 5.5]]


# Accessing List Elements
# Accessing by Index:
daily_step_count = [10343, 9385, 7029, 10931, 5921]
print(daily_step_count[2]) # Output: 7029
# Here, daily_step_count[2] retrieves the value at index 2 of the list,
# which is 7029.



# Modifying Elements 
# Charging an Element:
daily_step_count[4] = 100
print(daily_step_count) # Output: [10343, 9385, 7029, 10931, 100]
# This changes the element at index 4 to 100.


# Appending and Inserting Elements
# Appending:
daily_step_count.append(8694)
print(daily_step_count) # Output: [10343, 9385, 7029, 10931, 100, 8694]
# append(8694) adds 8694 to the end of the list.



# Inserting:
daily_step_count.insert(3, 4473)
print(daily_step_count) # Output: [10343, 9385, 7029, 4473, 10931, 100, 8694]
# insert(3, 4473) inserts 4473 before the element currently at index 3.



# Removing Elements
# Removing by Value: 
daily_step_count.remove(7029)
print(daily_step_count) # Output: [10343, 9385, 4473, 10931, 100, 8694]
# remove(7029) removes the first occurrence of 7029 from the list.



# Popping:
popped = daily_step_count.pop()
print(daily_step_count) # Output: [10343, 9385, 4473, 10931, 100]
print(popped)           # Output: 8694
# pop() removes and returns the last item in the list.



# Index and Count
# Finding the Index:
index_value = daily_step_count.index(100)
print(index_value) # Output: 4
# index(100) finds the index of the first occurrence of 100.



# Counting Ocurrences:
count = daily_step_count.count(100)
print(count) # Output: 1
# count(100) returns the number of times 100 appears in the list.



# Sorting and Reversing:
daily_step_count.sort()
print(daily_step_count) # Output: [100, 4473, 9385, 10343, 10931]
# sort() sorts the list in ascending order.




# Reversing:
daily_step_count.reverse()
print(daily_step_count) # Output [10931, 10343, 9385, 4473, 100]
# reverse() reverses the order of the list elements.



# Slicing
# Examples:
red_river = ['R', 'R', 'C', ' ', 'P', 'o', 'l', 'y', 't', 'e', 'c', 'h', 'n', 'i', 'c']
print(red_river[2: 12: 2]) # Output: ['C', 'P', 'l', 't', 'c']
print(red_river[: 10: 1])  # Output: ['R', 'R', 'C', ' ', 'P', 'o', 'l', 'y', 't', 'e']
print(red_river[5: : 3])   # Output: ['o', 't', 'h', 'c']
print(red_river[:: 5])     # Output: ['R', 'o', 'c']
print(red_river[-1: -5: -1]) # Output: ['c', 'i', 'n', 'h']
# These slicing examples show how to extract parts of a list using start,
# stop, and step indices.

