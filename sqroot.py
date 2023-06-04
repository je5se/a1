import math
x = float(input("enter a number, i will calculate the square root"))

import random
g = random.randint(1,x-1)

while abs(x - g*g) > 1e-5:
    g = (g+ x/g) /2

print(g)
