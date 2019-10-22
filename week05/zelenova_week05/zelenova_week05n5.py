#5 Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# {y = x^2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5; y = 2x при x > 5}.
# Вычисление значения функции оформить в виде программной функции,
# которая принимает значение x, а возвращает полученное значение функции (y).
# Нарисуйте с помощью matplotlib график этой функции.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
for i in range(20):
    x.append(int(i-10))
for i in range(20):
    if x[i]<(-5):
       y.append(int(x[i]*x[i]))
    if -5<=x[i]<=5:
       y.append(2*abs(x[i])-1)
    if x[i]>5:
       y.append(2*x[i])
print('x',x)
print('y',y)
plt.figure(figsize=(200,100))
plt.plot(y,color='blue',linewidth=3)
plt.title('Кусочно заданная функция', fontsize=18)
plt.grid(True)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)

plt.plot(-10,10)

plt.show()
