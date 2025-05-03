with open('second-challenge-decoded.txt', 'r') as f:
    file = f.readlines()

ciphermap = {
    'a':'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t',
    'h':'s',
    'i':'r',
    'j':'q',
    'k':'p',
    'l':'o',
    'm':'n',
    'n':'m',
    'o':'l',
    'p':'k',
    'q':'j',
    'r':'i',
    's':'h',
    't':'g',
    'u':'f',
    'v':'e',
    'w':'d',
    'x':'c',
    'y':'b',
    'z':'a',
    'A':'Z',
    'B':'Y',
    'C':'X',
    'D':'W',
    'E':'V',
    'F':'U',
    'G':'T',
    'H':'S',
    'I':'R',
    'J':'Q',
    'K':'P',
    'L':'O',
    'M':'N',
    'N':'M',
    'O':'L',
    'P':'K',
    'Q':'J',
    'R':'I',
    'S':'H',
    'T':'G',
    'U':'F',
    'V':'E',
    'W':'D',
    'X':'C',
    'Y':'B',
    'Z':'A',
    ' ':' ',
    '.':'.',
    '!':'!',
    ',':',',
    '\n':'\n',
    '(':'(',
    ')':')',
    '\'':'\''
}

cipher_number = 6
output = []
for line in file:
    currentLine = ""
    for char in line:
        currentLine += ciphermap[char]
        # ascii = ord(char)
        # if (ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122):
        #     ascii -= cipher_number
        #     if not ((ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122)):
        #         ascii += 26
        # currentLine += str(chr(ascii))
    output.append(currentLine)

print(output)

with open('second-challenge-encoded.txt', 'w') as f:
    file = f.writelines(output)