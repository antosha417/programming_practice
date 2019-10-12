#Задача «Переставить min и max»
#Условие
#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
l = list(map(int, input().split()))
small = l[0]
big = l[0]
small_index = 0
big_index = 0

for i in range(len(l)):
    if l[i] > big:
        big = l[i]
        big_index = i
for i in range(len(l)):
    if l[i] < small:
        small = l[i]
        small_index = i


l[big_index] = small
l[small_index] = big

print(*l)

