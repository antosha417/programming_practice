#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a = list(map(int, input().split()))
b = list(a)
b[a.index(min(a))] = max(a)
b[a.index(max(a))] = min(a)

for i in range(len(b)):
    print(b[i])