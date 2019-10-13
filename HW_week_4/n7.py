dict0 = {}
for _ in range(int(input())):
    string = list(map(str, input().split()))
    for i in string:
        if i not in dict0:
            dict0[i] = 0
        dict0[i] += 1
print(len(dict0))