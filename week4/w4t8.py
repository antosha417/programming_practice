n = int(input())
dict_syn = {}
for i in range(n):
    s = list(map(str, input().split()))
    dict_syn[s[0]] = s[1]
word = str(input())
if dict_syn.get(word) is not None:
    print(dict_syn[word])
else:
    for key, value in dict_syn.items():
        if value == word:
            print(key)