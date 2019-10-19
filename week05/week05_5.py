"""Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
{y = x^2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5; y = 2x при x > 5}. Вычисление значения функции оформить
в виде программной функции, которая принимает значение x, а возвращает полученное значение функции (y).
Нарисуйте с помощью matplotlib график этой функции."""



xx = []
for i in range (21):
    xx.append(i-10)

yy = []

for x in range(-10, 11):

    if x > 5 and x <= 10:
        yy.append(2*x)

    if x >= -10 and x< -5:
        yy.append(2*abs(x) - 1)
    if x >= -5 and x <= 5:
        yy.append(x**2)




import matplotlib.pyplot as plt


plt.plot(xx, yy)
plt.grid()
plt.draw()

plt.show()