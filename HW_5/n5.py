import matplotlib.pyplot as plt
import numpy as np


def x_to_y(x):
    if x < -5:
        return 2 * abs(x) - 1
    elif x > 5:
        return 2 * x
    else:
        return x ** 2


def main():
    x = list(i for i in range(-10, 11, 1))
    y = list(x_to_y(x[i]) for i in range(len(x)))
    plt.plot(x, y, 'go')
    plt.show()


main()