#4Напишите функцию, которая на вход принимает квадратную матрицу (например, в виде списка списков).
# Вычисляет сумму элементов главной или побочной диагонали в зависимости от выбора пользователя.
# Сумма элементов любой диагонали должна вычисляться в одной и той же отдельной функции.
from z_week05n1 import checknumint

num = 0

def diagonal_sum(column):
    sum=0
    for i in range(a):
        line=column[i]
        sum+=line[n*i]
    return sum

print('Введите порядок матрицы')
a=checknumint(num)
column=[]
print('Введите матрицу по-строчно')
for i in range(a):
              line=[int(s) for s in input().split()]
              column.append(line)

_ = 1
while _:
       print('Если вы хотите узнать сумму главной диагонали введите 1,для определения суммы побочной диагонали введите -1')
       n=checknumint(num)
       if n in [-1,1]:
           print('Сумма выбранной диагонали равна' diagonal_sum(column))
           _ = 0
       else:
           print('Вы ввели не корректное значение')

