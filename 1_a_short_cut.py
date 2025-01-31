"""
Description: Shortcut Operators
Author: KSG
Date: Jan 25
Usage: 
"""

# This is equivalent to age = age + 1. The value of 'age' becomes 26.
age = 25
age += 1

# This is equivalent to countdown = countdown -1. The value of
# 'countdown' becomes 9.
countdown = 10
countdown -= 1

# This is equivalent to factor = factor * 10. The value of
# 'factor' becomes 120.
factor = 12
factor *= 10

# /= (Division Assignment)
# This is equivalent to half = half /2. The value of 'half'
# becomes 20.5
half = 41
half /= 2
print(half)

# //= (Floor Division Assignment)
# This is equivalent to less_precise_half = less_precise_half
# // 2. The value becomes 20
less_precise_half = 41
less_precise_half //= 2
print(less_precise_half)

# %= (Modulus Assignment)
# This is equivalent to remainder = remainder % 2. The remainder
# of 13 divided by 2 is 1.
remainder = 13
remainder %= 2
print(remainder)

# **= (Exponentiation Assignment)
# This is equivalent to power = power ** 3. The value of 'power'
# becomes 125 (5 raised to the power of 3).
power = 5
power **= 3
print(power)