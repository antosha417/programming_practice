'''
Выведите все четные элементы списка.
При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
'''
a = []
n = int(input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
for k in range(n):
    if a[k]%2 == 0:
        print (a[k])