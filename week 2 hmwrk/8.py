s = input()
a = s.split()
for elem in a:
    b = int(elem)
    if b % 2 == 0:
        print(b)
