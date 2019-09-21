x = int(input())
y = 0
while x > 1439:
    x -= 1440
else:
    x += 0
while x > 59:
    x -= 60
    y += 1
else:
    print('y, x')
