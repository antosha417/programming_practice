n=int(input())
A=[]
i_min=0
i_max=0
for i in range(n):
    new_element = int(input())
    A.append(new_element)
for i in range(n):
    if(A[i]==min(A)):
        i_min=i;
    if(A[i]==max(A)):
        i_max=i;
B=[];
for i in range(n):
    if(i==i_max):
        B.append(min(A))
    elif i==i_min:
        B.append(max(A))
    else:
        B.append(A[i])
for i in range(n):
    print(B[i])