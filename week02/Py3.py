def find_min(a,b,c):
    min_elem=a
    if b<min_elem:
        min=b
    if c<min_elem:
        min=c
    print(min_elem)
a=int(input())
b=int(input())
c=int(input())
find_min(a,b,c)