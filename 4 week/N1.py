"""
how much a[i] > a[i (+&-) 1]
"""
count = 0
a = input()
a = a.split(' ')
for i in range(1, len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        count+=1
print(count)