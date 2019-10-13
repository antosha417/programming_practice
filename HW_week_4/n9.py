dict0 = {}
list0 = []
list_of_frequent_words = []
for _ in range(int(input())):
    string = list(map(str, input().split()))
    for i in string:
        if i not in dict0:
            dict0[i] = 0
        dict0[i] += 1
for i in dict0:
    list0.append(dict0[i])
    list_max = max(list0)
for i in dict0:
    if dict0[i] == list_max:
        list_of_frequent_words.append(i)
list_of_frequent_words.sort()
print(list_of_frequent_words[0])