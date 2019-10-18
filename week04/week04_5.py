s1 = input()
lst1 = s1.split()
s2 = input()
lst2 = s2.split()
ans = []

for num1 in lst1:
    for num2 in lst2:
        if num1 == num2:
            ans.append(num1)

for i in range(len(ans)):
    ans[i] = int(ans[i])
n = 1
while n < len(ans):
    for i in range(len(ans) - n):
        if ans[i] > ans[i + 1]:
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
    n += 1

# ans = sorted(ans)
print(ans)
