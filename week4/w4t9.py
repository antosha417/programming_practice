n = int(input())
amount = {}
text = []
maximum = 0
word_max = ''
for i in range(n):
    s = list(map(str, input().split()))
    for j in range(len(s)):
        text.append(s[j])
for i in range(len(text)):
    if amount.get(text[i]) == None:
        amount[text[i]] = 1
    else:
        amount[text[i]] += 1
    if amount[text[i]] > maximum:
        maximum = amount[text[i]]
        word_max = text[i]
    elif amount[text[i]] == maximum and text[i] < word_max:
        maximum = amount[text[i]]
        word_max = text[i]
print(amount) #бонусное задание посчитать сколько раз встречается каждое слово
for i in range(len(text)):
    if text[i] == word_max:
        print(text[i])
        break