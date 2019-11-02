n = int(input())
d = dict()
for i in range(n):
    s = input()
    A = s.split()
    for j in range(len(A)):
        if A[j] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
lst = []
for key in d:
    lst.append(d[key])
print(max(lst))