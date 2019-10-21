n = int(input())
text = set()
for i in range(n):
    s = input().split()
    for elem in s:
        text.add(elem)
print(len(text))