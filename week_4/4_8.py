n=int(input())
d=dict()
for i in range(n):
    s=input()
    A=s.split()
    d[A[0]]=A[1]
    d[A[1]]=A[0]
s2=input()
if s2 in d:
    print(d[s2])