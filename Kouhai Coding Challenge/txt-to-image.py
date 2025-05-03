import numpy as np
import math
import png

f = open("first-challenge.txt", "r")
oneline = f.readline()
f.close()
side = math.ceil(math.sqrt(len(oneline)))
array = np.chararray((side,side))
for i in range(0,side,1):
    for j in range(0,side):
        try:
            array[i][j] = oneline[i*side+j]
        except:
            array[i][j] = "_"
img = array.tolist()
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j] = ord(img[i][j])

with open('image.png', 'wb') as f:
    w = png.Writer(side, side)
    w.write(f, img)