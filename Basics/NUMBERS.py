"""
- maximum representable int: sys.maxsize
    Actually, ints in python is unbounded, so this is the interpreter's word size
- random.randrange(start, stop, step)
"""


# MOD
-3 % 10  # 7
# Power
2 ** 3  # 8
# XOR
2 ^ 3  # 1


# RANDOM
import random
# .randrange(start, stop, step) - return int
random.randrange(1, 3)  # 1 or 2
# .randint(start, stop) - return int, inclusive bounds
random.randint(1, 3)  # 1 or 2 or 3

import math
from math import floor
floor(1.89)  # 1


# DIVISION
4 / 3 = 1   # for integers, / works as floor division
float(5) / 4 = 1.25   # / is accurate div for floats
float(5) // 4 = 1   # // is the real floor div
