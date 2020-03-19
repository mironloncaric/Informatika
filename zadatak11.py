from random import random
import math
n = int(input())
m = 0
for i in range(n) :
    if math.sqrt(random()**2 + random()**2) <= 1 :
        m += 1
print(4 * m / n)