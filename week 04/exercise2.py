'''
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
'''

a = [int(s) for s in input().split()]
inf_numb = 0
sup_numb = 0
for i in range(1, len(a)):
    if a[inf_numb] > a[i]:
        inf_numb = i
    elif a[sup_numb] < a[i]:
        sup_numb = i

a[inf_numb], a[sup_numb] = a[sup_numb], a[inf_numb]
print(' '.join([str(i) for i in a]))
