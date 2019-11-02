A=[]
a=int(input())
while a!=0:
    A.append(a)
    a=int(input())
max_A=0
max2_A=0
for i in range(len(A)):
    if A[i]>max_A:
        max_A=A[i]
for i in range(len(A)):
    if A[i]>max2_A and A[i]!=max_A:
        max2_A=A[i]
print(max2_A)