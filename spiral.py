import turtle as t


def krug(n):
    for i in range(180):
        t.forward(n)
        t.right(1)


def duga(x, y):
    while x != y:
        krug(x)
        x += 0.1


t.speed(0)
x = 1
y = 10
duga(x, y)