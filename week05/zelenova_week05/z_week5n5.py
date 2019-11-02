#5 Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# {y = x^2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5; y = 2x при x > 5}.
# Вычисление значения функции оформить в виде программной функции,
# которая принимает значение x, а возвращает полученное значение функции (y).
# Нарисуйте с помощью matplotlib график этой функции.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def funcxy(x):
    if x < (-5):
        return abs(x)*2-1
    elif x > 5:
        return x*2
    else:
        return x*x

x=list(i for i in range (-10,11,1))
y=list(funcxy(x[i]) for i in range(len(x)))

plt.plot(x,y,color='blue',linewidth=3)
plt.title('Кусочно заданная функция', fontsize=18)
plt.grid(True)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)

plt.show()
