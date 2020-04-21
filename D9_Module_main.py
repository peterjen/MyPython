# https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9

import D9_Module as d9m
from  D9_Module import find_func
from  D9_Module import find_func, a_test

list = ['Math', 'Chinese', 'LAL']

print(d9m.find_func('Chinese',list)) # 1
print(d9m.find_func('f','abcdefg')) # 5

a_test()



import sys
# print(sys.path)

import random
random_course = random.choice(list)
print(random_course)

import math
print(math.radians(45))
print(math.sin(90))

import datetime
import calendar

print(datetime.date.today())
print(calendar.isleap(2019))

import os
print(os.getcwd())
print(os.__file__)









