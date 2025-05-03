for i in range(1, 101):
    out = ""
    out += "fizz" if i % 3 == 0 else ""
    out += "buzz" if i % 5 == 0 else ""
    print(i if out == "" else out)

for i in range(1, 101):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)