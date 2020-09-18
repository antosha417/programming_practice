s = input()
lst = s.split()
maks = 0
minim = 0
for i in range(len(lst)):
    if lst[i] < lst[minim]:
        minim = i
for j in range(len(lst)):
    if lst[j] > lst[maks]:
        maks = j
lst[maks], lst[minim] = lst[minim], lst[maks]

ans = " ".join(lst)
print(ans)
