#Даны два списка чисел.
#Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
a = list(set([int(i) for i in input().split()]) & set([int(i) for i in input().split()]))
for element in sorted(a):
    print(element, end=' ')