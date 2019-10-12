def find_2nd_max(arr):
    mx=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>mx:
            mx=arr[i]
    mx2=0
    for i in range(len(arr)):
        if ((arr[i]>mx2) and (arr[i]<mx)):
            max2=arr[i]
    print(mx2)

mas=[]
a=int(input())
while a!=0:
    mas.append(a)
    a=int(input())
find_2nd_max(mas)