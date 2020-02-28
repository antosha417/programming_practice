def more_than_neigh(mas):
    count=0
    for i in range(1,len(mas)-1):
        if mas[i]>mas[i-1] and mas[i]>mas[i+1]:
            count+=1
    print(count)

st=input().split()
arr=[]
for k in st:
    arr.append(int(k))
more_than_neigh(arr)