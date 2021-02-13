#5.	Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список
# и выведите их в порядке возрастания (pythontutor.ru, занятие 10, «Пересечение множеств»)
a=[int(s) for s in input().split()]
b=[int(s) for s in input().split()]
c=sorted(list(set(a)&set(b)))

print(' '.join(map(str,c)))
