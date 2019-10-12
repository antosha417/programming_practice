n=int(input())
A=[]
c=0;
for i in range(n):
    new_element = int(input())
    A.append(new_element)
for i in range(n):
    count=0;
    for j in range(n):
        if (A[i]==A[j]) and (i!=j):
            count+=1
    if count==0:
        c+=1
print(c)