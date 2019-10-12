n=int(input())
A=[]
count=0
for i in range(n):
    new_element = int(input())
    A.append(new_element)
for i in range(n):
    if i!=(n-1):
        for j in range(i+1,n):
            if (A[i]==A[j]):
                count+=1
print(count)