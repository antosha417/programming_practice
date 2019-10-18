def find_2nd_max(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    max2=0
    for i in range(len(arr)):
        if ((arr[i]>max2) and (arr[i]<max)):
            max2=arr[i]
    print(max2)

mas=[]
a=int(input())
while a!=0:
    mas.append(a)
    a=int(input())
find_2nd_max(mas)