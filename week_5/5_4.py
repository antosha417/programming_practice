def diagonal(A, str):
    sum=0
    if str == "main":
        for i in range(n):
            sum+=A[i][i]
    elif str == "side":
        for i in range (n):
            sum += A[i][n-1-i]

    return sum


n = int(input())
A0 = []
for i in range(n):
    s = list(map(int, input().split()))
    A0.append(s)
print("Choose the diagonal's type:")
str0 = input()
print(diagonal(A0, str0))