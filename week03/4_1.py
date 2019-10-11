n=int(input())
A=[]
count=0;
for i in range(n):
    new_element = int(input())
    A.append(new_element)
for i in range(1,n-1):
    if (A[i]>A[i-1]) and (A[i]>A[i+1]):
        count+=1
print(count)