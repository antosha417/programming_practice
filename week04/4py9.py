def most_frequent_word(n):
    words = {}
    for i in range(n):
        s = input().split()
        for word in s:
            words[word] = words.get(word, 0) + 1
    mx = max(words.values())
    mas = []
    for key, value in words.items():
        if value == mx:
            mas.append(key)
    mas = sorted(mas)
    print(mas[0])

N = int(input())
most_frequent_word(N)