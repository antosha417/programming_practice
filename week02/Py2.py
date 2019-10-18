def print_string(t,n):
    a=[]
    a.append('Hello')
    for i in range(n):
        a.append(t)
    print(', '.join([a[i] for i in range(n+1)]))

text=input()
n=int(input())
print_string(text,n)
