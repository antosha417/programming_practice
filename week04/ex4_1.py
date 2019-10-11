lst = [1, 3, 6, 5, 7, 3, 8, 9, 10, 4, 5, 1]
a = 0
for i in range(1, len(lst)-1):
    if lst[i]>lst[i+1] and lst[i]>lst[i-1]:
        a += 1
print(a)
