'''
ычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом,
равным 1. {y = x^2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5; y = 2x при x > 5}.
Вычисление значения функции оформить в виде программной функции, которая принимает значение x,
а возвращает полученное значение функции (y). Нарисуйте с помощью matplotlib график этой функции.1
'''
from matplotlib import pyplot as plt
import numpy as np
def f(x):
    if x > 5:
        return 2*x
    elif abs(x) <= 5:
        return x*x
    else:
        return 2*abs(x)-1
X1 = np.linspace(-10, -5.001, 100)
Y1 = [f(x) for x in X1]
X2 = np.linspace(-4.99, 5, 100)
Y2 = [f(x) for x in X2]
X3 = np.linspace(5.001, 10, 100)
Y3 = [f(x) for x in X3]
plt.plot(X1, Y1)
plt.plot(X2, Y2)
plt.plot(X3, Y3)
plt.show()