def count_sum(matrix,flag):
    s=0
    for i in range(N):
        for j in range(N):
            if flag:
                if i==j:
                    s+=matrix[i][j]
            elif i+j==N-1:
                s += matrix[i][j]
    return s

N=int(input())
arr=[]
for i in range(N):
    line=input().split()
    for j in range(N):
        line[j]=int(line[j])
    arr.append(line)
print('Main or side diagonal?')
s=input()
k=True
if s=='main':
    k=True
elif s=='side':
    k=False
print(count_sum(arr,k))
