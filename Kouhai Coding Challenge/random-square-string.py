import numpy as np
import math
import random

side = 50

minvalue = 60
maxvalue = 120

output = ""
for i in range(side):
    for j in range(side):
        output = output + chr(random.randint(minvalue, maxvalue))

with open('first-challenge.txt', 'w') as f:
    f.flush()
    f.write(output)