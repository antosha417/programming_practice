n = int(input())
synonym = {}
for _ in range(n):
    word1, word2 = input().split(' ')
    synonym[word1] = word2
x = input()
for i in synonym:
    if synonym[i] == x:
        print(i)
    elif i == x:
        print(synonym[i])
