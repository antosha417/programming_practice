import turtle as t


def krug(n):
    t.right(n)
    for i in range(360):
        t.forward(1)
        t.right(1)


k = 0
while k != 360:
    krug(k)
    k += 30