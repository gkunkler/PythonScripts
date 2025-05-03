import numpy as np
import math
import png

with open('image.png', 'r') as f:
    r = png.Reader("image.png")
    image_data = r.asDirect()

side = image_data[0]
rows = list(image_data[2])

array = np.chararray((side,side))

for i in range(len(rows)):
    for j in range(0, len(rows[i]),4):
        array[i][j//4] = chr(min(rows[i][j],120))

print(array)

array = array.tolist()
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = str(array[i][j])[2:3]

# set instructions
square = "Turn me into a square file"
for i in range(len(square)):
    array[0][i] = square[i]

turn = "Turn me into greyscale image ascii as brightness"
for i in range(len(turn)):
    array[i][0] = turn[i]

ascii = "ascii as brightness"
for i in range(len(ascii)):
    array[19][i] = ascii[i]
    array[25][i] = ascii[i]

line = ""
for i in range(len(array)):
    for j in range(len(array[i])):
        line = line + array[i][j]

print(array)

#generate final image
img = array.tolist()
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j] = ord(img[i][j])

with open('image.png', 'wb') as f:
    w = png.Writer(side, side)
    w.write(f, img)
