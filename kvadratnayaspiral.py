import turtle as t


def polukvadrat(nach, kon):
    while nach != kon:
        t.forward(nach)
        t.left(90)
        t.forward(nach)
        t.left(90)
        nach += 4


x = 5
y = 150
polukvadrat(x, y)