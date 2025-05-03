import numpy as np
import math
import png

f = open("first-challenge.txt", "r")
oneline = f.readline()
f.close()
print(oneline)
side = math.ceil(math.sqrt(len(oneline)))
print(side)
array = np.chararray((side,side))
for i in range(0,side,1):
    for j in range(0,side):
        array[i][j] = oneline[i*side+j]
array = array.tolist()
for i in range(0,side,1):
    for j in range(0,side):
        array[i][j] = str(array[i][j])[2:3]
    print(''.join(array[i][:]))