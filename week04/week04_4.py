s = input()   # уникальные элементы
lst = s.split()
ans = []
lst = s.split()
ans = []

for num in lst:
    if lst.count(num) == 1:
        ans.append(num)
print(" ".join(ans))
