huge = 1
big = 0
a = 1
while a > 0:
    a = int(input())

    if a > big and a > huge:
        big = huge
        huge = a

    if a > big and a < huge:
        big = a

print(big)