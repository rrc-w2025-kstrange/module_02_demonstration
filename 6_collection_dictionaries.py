"""
Description: # Dictionaries
Author: KSG
Date: Jan 25
Usage: 
"""

# Dictionaries

# Accessing and Modifying Values:
# Accessing by Key:
fruit_inventory = {'apples': 23, 'oranges': 10, 'bananas': 59, 'pears': 29}
value = fruit_inventory['oranges']
print(value) # Output: 10


# Modifying Value
fruit_inventory['oranges'] = 25
print(fruit_inventory['oranges']) # Output: 25


# Adding New Key-Value Pairs: 
fruit_inventory['plums'] = 100
print(fruit_inventory)
# Output: {'apples': 23, 'oranges': 25, 'bananas': 59, 'pears': 29,
# 'plums': 100}


# Dictionary Methods:
# Keys, Values, and Items:
print(fruit_inventory.keys())
# Output: dict_keys(['apples', 'oranges', 'bananas', 'pears', 'plums'])
print(fruit_inventory.values())
# Output: dict_values([23, 25, 59, 29, 100])
print(fruit_inventory.items())
# Output: dict_items([('apples', 23), ('oranges', 25), ('bananas', 59),
# ('pears', 29), ('plums', 100)])


# Getting and Removing Items:
print(fruit_inventory.get('apples'))
# Output: 23


# Removing. pop() method removes the key-value pair based on the key argument
fruit_inventory.pop('plums')
print(fruit_inventory.get('plums', 'fruit is not currently in the dictionary'))
# Output: fruit is not currently in the dictionary


# Removing oranges
fruit_inventory.pop('oranges')
print(fruit_inventory)
# Output: {'apples': 23, 'bananas': 59, 'pears': 29}


# Removing all
fruit_inventory.clear()
print(fruit_inventory)
# Output: {}

