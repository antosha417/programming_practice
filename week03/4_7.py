str=""
while True:
    try:
        s=input()+" "
        str+=s
    except EOFError:
        break
    if s==" ":
        break
A=str.split()
B=set(A)
print(len(B))