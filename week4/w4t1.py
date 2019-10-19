arr = []
amount = 0
num = int(input())
for i in range(num):
    arr.append(int(input()))
for i in range(1, num - 1):
    if arr[i] >  arr[i - 1] and arr[i] > arr[i + 1]:
        amount += 1
print(amount)