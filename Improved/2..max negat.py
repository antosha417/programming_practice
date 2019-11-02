huge = -9998
big = -9999
a = int(input())
while a < 0:


    if a > big and a > huge:
        big = huge
        huge = a

    if a > big and a < huge:
        big = a
    a = int(input())
print(big)