u = input()
t = input()
x = u * t
while x < 0:
    x += 109
else:
    x += 0
while x >= 109:
    x -= 109
else:
    x += 0
x = round(x)
print(x)
