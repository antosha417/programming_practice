text = set()
quantity=int(input())


for _ in range(quantity):
    text.update(input().split())
print(len(text))

