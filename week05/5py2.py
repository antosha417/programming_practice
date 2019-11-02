def max_common_div(arr):
    A=set()
    for i in range(N):
        a=arr[i]
        for j in range(i+1,N):
            b=arr[j]
            minelem=min(a,b)
            for k in range(minelem,-1,-1):
                if ((a%k==0) and (b%k==0)):
                    A.add(k)
                    break

    return A
mas=[]
N=int(input())
for i in range(N):
    a=int(input())
    mas.append(a)
B=max_common_div(mas)
for elem in B:
    print(elem, ' ')


