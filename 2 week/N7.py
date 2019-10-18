"""
Выведите все элементы списка с четными индексами
"""

arr = input()
arr = arr.split()

for i in range(len(arr)):
    if i%2 == 0:
        print (arr[i], end = ' ')
