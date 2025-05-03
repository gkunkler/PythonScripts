import numpy as np
import math
import png
import qrcode
import random
import segno

side = 100

# generate base string
minvalue = 80
maxvalue = 126

random_string = ""
for i in range(side):
    for j in range(side):
        random_string = random_string + chr(random.randint(minvalue, maxvalue))

# convert to square
array = np.chararray((side,side))
for i in range(0,side,1):
    for j in range(0,side):
        array[i][j] = random_string[i*side+j]
array = array.tolist()
for i in range(0,side,1):
    for j in range(0,side):
        array[i][j] = str(array[i][j])[2:3]

# add instructions
square = "Turn me into a square file "
for i in range(len(square)):
    array[0][i] = square[i]

turn = "Turn me into a greyscale image ascii as brightness "
for i in range(len(turn)):
    array[i][0] = turn[i]
    
for i in range(len(turn)-1):
    array[i+1][1] = " "

img = array.copy()
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j] = ord(img[i][j])

# qrcode

with open('second-challenge-encoded.txt', 'r') as f:
    second_challenge = f.read()

qr = qrcode.QRCode(box_size = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   border = 0)

qr.add_data(second_challenge)
qr.make(fit = True)
qrimg = qr.make_image(fill_color="black", back_color="white")

# qrimg=segno.make_qr(second_challenge, )
qrimg.save('qr.png')

#use qrcode in text
with open('qr.png', 'r') as f:
    r = png.Reader("qr.png")
    image_data = r.asDirect()

qrside = image_data[0]
rows = list(image_data[2])

qrvalues = np.chararray((qrside,qrside))

for i in range(len(rows)):
    for j in range(0, len(rows[i])):
        qrvalues[i][j] = rows[i][j]

x = 5
y = 5

outputimg = img.copy()

for i in range(x,qrside+x):
    for j in range(y,qrside+y):
        if qrvalues[i-x][j-y] == b'0':
            outputimg[i][j] = random.randint(35, 45)

# convert to image

with open('image.png', 'wb') as f:
    w = png.Writer(side, side)
    w.write(f, outputimg)

# convert to first challenge text
output_text = ""
for i in range(len(outputimg)):
    for j in range(len(outputimg[i])):
        output_text = output_text + str(chr(min(outputimg[i][j], 125)))

with open('first-challenge.txt', 'w') as f:
    f.flush()
    f.write(output_text)