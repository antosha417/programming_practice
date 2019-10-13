'''
выведите все элементы списка с четными индексами (то есть lst[0], lst[2], lst[4], ...).
'''
a = []
n = int(input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
for k in range(n):
    if k%2 == 0:
        print (a[k])