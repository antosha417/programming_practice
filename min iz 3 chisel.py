a = int(input())
b = int(input())
c = int(input())

if a <= b:
    small = a
else:
    small = b

if c <= small:
    small = c

print(small)