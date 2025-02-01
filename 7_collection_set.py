"""
Description: # Sets
Author: KSG
Date: Jan 25
Usage: 
"""

# Sets, remember a set cannot contain duplicate values.

# Creating sets: 
# set created with {}
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
print(primes)
# Output: {2, 3, 5, 7, 11, 13, 17, 19, 23}

# Empty set created with function set ()
fives = set()
print(fives)
# Output: set()


# Adding Elements add() method.
primes.add(29)
print(primes)
# Output: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

fives.add(5)
print(fives)
# Output: {5}

fives.add(35)
print(fives)
# Output: {35, 5}


# Removing Elements using remove() causes exception if it doesn't exist
primes.remove(3)
print(primes)
# Output: {2, 5, 7, 11, 13, 17, 19, 23, 29}

## primes.remove(22)
## KeyError: 22
# exception occurs: 22 is not within the set.


# Removing Elements using discard() if the element doesn't exist statement
# is ignored
primes.discard(5)
print(primes)
# Output: {2, 7, 11, 13, 17, 19, 23, 29}

# Element, 5, doesn't exist statement is ignored
primes.discard(5)


# union() method returns a new set containing all unique elements from
# both sets
union = primes.union(fives)
print('the new union is:', union)
# Output: the new union is: {2, 35, 5, 7, 11, 13, 17, 19, 23, 29}


# Difference for set operations
difference = primes.difference(fives)
print(difference)
# Output: {2, 7, 11, 13, 17, 19, 23, 29}

difference = fives.difference(primes)
print(difference)
# Output: {35, 5}


# Intersection for set operations
intersect = primes.intersection(fives)
print(intersect)
# Output: set()

primes.add(5)
# Intersection for set operations
intersect = primes.intersection(fives)
print(intersect)
# Output: {5}
