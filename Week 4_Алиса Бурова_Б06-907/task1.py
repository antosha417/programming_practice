a = list(map(int, input().split()))
index = 1
bigneighbor = 0
while index < len(a)-1:
    if a[index-1] < a[index] > a[index+1]:
        bigneighbor += 1
        index += 2
    else:
        index += 1
print(bigneighbor)