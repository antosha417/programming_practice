s=list(map(int,input().split()))
A=set()
for i in range(len(s)):
    l1=len(A)
    A.add(s[i])
    l2=len(A)
    if l1==l2:
        print("YES")
    else:
        print("NO")