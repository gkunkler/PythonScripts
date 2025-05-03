x=-1
while x==-1:
    try:
        x = int(input("Please enter an integer:\n"))
    except ValueError:
        x = -1
a = 0
b = 1
for _ in range(x):
    a += b
    b = a - b
print(a)
