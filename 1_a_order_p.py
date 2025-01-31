"""
Description: Order of Operations
Author: KSG
Date: Jan 25
Usage: 
"""

# The first expression uses parentheses to control the order of operations.
# 1. (10 + 5) is evaluated first, resulting in 15.
# 2. Then, 15 * 2 is evaluated, resulting in 30.
# 3. Next, 30 / 3 is evaluated, resulting in 10.0.
# 4. Finally, 10.0 - 1 is evaluated, resulting in 9.0.
result = ((10 + 5) * 2) / 3 - 1
print(result) # Outputs: 9.0

# The second expression follows the default order of operations
# (no parentheses).
# 1. First, 5 * 2 is evaluated, resulting in 10.
# 2. Then 10 / 3 is evaluated, resulting in approximately 3.333.
# 3. Next, 10 + 3.333 is evaluated, resulting in 13.333.
# 4. Finally, 13.333 - 1 is evaluated, resulting in approximately 12.333.
result = 10 + 5 * 2 / 3 - 1
print(result) # Outputs: 12.333333333333334


