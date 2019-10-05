import turtle as t


def krug(n, k):
    t.right(n)
    for i in range(360):
        t.forward(k)
        t.right(1)


t.speed(0)
t.right(90)
p = 10
r = 1
gradus = 0
while p != 0:
    gradus %= 360
    krug(gradus, r)
    krug(180 - gradus, r)
    r += 0.1
    p -= 1