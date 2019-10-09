A=[]
a=int(input())
while a!=0:
    A.append(a)
    a=int(input())
for i in range( len(A)):
    if i %2==0:
        print(A[i])
