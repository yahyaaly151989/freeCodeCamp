# =========================== Modules ===========================
# 1- What is Python module with example?
# ---> A Python module is a file containing Python definitions and statements. 
#      A module can define functions, classes, and variables. A module can also include runnable code. 
#      Grouping related code into a module makes the code easier to understand and use.


# 2- Importing Modules:

# ---> First Method:
import random 

# print(random)

# print(dir(random))
a = random.random()
b = random.randint(1, 10)
print(a)
print(b)
print("=" * 75)

# ---> Second Method:
from random import randint, random
a = random()
b = randint(1, 10)
print(a)
print(b)
print("=" * 75)


# ---> Third Method:
from random import *
a = random()
b = randint(1, 10)
print(a)
print(b)
print("=" * 75)

# ---> Fourth Method:
import random as rn
a = rn.random()
b = rn.randint(1, 10)
print(a)
print(b)
print("=" * 75)

import my_module

print(my_module.one())

# import sys

# sys.path.append(r"C:\Users\Administrator\Desktop")

# for path in sys.path:
#     print(path)
    

# import yehya

# print(yehya.yehya())

import numpy

print(numpy)


import pandas

print(pandas)

