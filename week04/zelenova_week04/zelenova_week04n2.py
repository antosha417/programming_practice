#2.	В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.
# (pythontutor.ru, занятие 7, «Переставить min и max»)

a=[int(s) for s in input().split()]

def reverce_min_max(a):
    '''reverce min max меняет местами минимальный и максимальный элемент в списке,
     при условии что все элементы списка различны.'''
    x=a.index(max(a))
    y=a.index(min(a))
    a[x], a[y]=min(a),max(a)


reverce_min_max(a)
print(' '.join(map(str,a)))