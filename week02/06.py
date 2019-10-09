maks = int(input())
prev = int(input())
if maks < prev:
    maks, prev = prev, maks
n = int(input())
while n != 0:
    if n > maks:
        prev, maks = maks, n
    elif n > prev:
        prev = n
    n = int(input())
print(prev)
