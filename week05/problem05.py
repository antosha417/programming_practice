import matplotlib.pyplot as mpl


def f(x):
    if x > 5:
        return 2 * x
    elif x < -5:
        return 2 * abs(x) - 1
    else:
        return x ** 2


if __name__ == '__main__':
    x = []
    y = []
    for i in range(-10, 11, 1):
        x.append(i)
    for i in x:
        y.append(f(i))
    mpl.plot(x, y)
    mpl.show()
