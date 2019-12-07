a = []
counts = int(input())
for i in range(counts):
    string_with_words = input()
    b = string_with_words.split()
    a = a + b
a = list(set(a))
t = len(a)
print(t)


