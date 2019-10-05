import turtle as t


def duga(n):
    for i in range(180):
        t.forward(n)
        t.right(1)


t.left(90)
k = 10
while k != 0:
    duga(1)
    duga(0.1)
    k -= 1