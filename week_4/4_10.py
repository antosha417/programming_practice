str=""
d=dict()
while True:
    try:
        s=input()+" "
        str+=s
        if s==" ":
            break
        else:
            A=s.split()
            A[1]=int(A[1])
            if A[0] in d:
                d[A[0]]+=int(A[1])
            else:
                d[A[0]]=A[1]
    except EOFError:
        break
d.items()
D=sorted(d.items())
for i in range(len(D)):
    print(D[i][0], D[i][1])