import math
import random

number = 25
result = math.sqrt(number)
print(result)
print(math.pi)

import math as m

number = 25
result = m.sqrt(number)
print(result)

print(m.pi)
from math import sqrt

num = sqrt(64)
print(num)

from math import pi, sin, sqrt

value = sin(pi / 2)
print(value)

num = sqrt(64)
print(num)

from math import *

value = sin(pi / 2)
print(value)

num = sqrt(64)
print(num)

import math

print(dir(math))

print(math.factorial(5))
print(random.randint(10, 20))

import datetime


x = datetime.datetime.now()
print(x)
x = pow(4, 3)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x)  # returns 2
print(y)  # returns 1

import time
timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(" Area of the triangle is: ", area)
