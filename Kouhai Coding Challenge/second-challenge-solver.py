with open('second-challenge-encoded.txt', 'r') as f:
    file = f.readlines()

print(file)

cipher_number = 6
output = []
for line in file:
    currentLine = ""
    for char in line:
        print(char)
        
        ascii = ord(char)
        if (ascii>=65 and ascii<=77):
            ascii += (77-ascii)*2+1
        elif (ascii>=78 and ascii<=90):
            ascii += (78-ascii)*2-1
        elif (ascii>=97 and ascii<=109):
            ascii += (109-ascii)*2+1
        elif (ascii>=110 and ascii<=122):
            ascii += (110-ascii)*2-1
        print(chr(ascii))
        currentLine += str(chr(ascii))
    output.append(currentLine)

print(output)

with open('second-challenge-solved.txt', 'w') as f:
    file = f.writelines(output)