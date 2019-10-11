"""
count pairs of equal elem
"""

count = 0
a = input()
a = a.split()
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i]== a[j]:
            count+=1
print(count)