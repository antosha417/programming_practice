def count_sum(matrix,flag):
    s=0
    for i in range(N):
        for j in range(N):
            if flag>0 and i==j:
                s+=matrix[i][j]
            elif flag<0 and i+j==N-1:
                s += matrix[i][j]
    return s

N=input()
arr=[]
if not N.isdigit():
    print('Type int value')
else:
    N=int(N)
    for i in range(N):
        line=input().split()
        for j in range(N):
            line[j]=int(line[j])
        arr.append(line)
    print('Main or side diagonal?')
    s=input()
    k=0
    if isinstance(s,str):
        if s=='main':
            k=1
        elif s=='side':
            k=-1
    else:
        print('Type str value')
    print(count_sum(arr,k))
