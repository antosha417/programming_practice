n = int(input())
dict_syn = {}
for i in range(n):
    word, synonym = input().split()
    dict_syn[word] = synonym
    dict_syn[synonym] = word
word_orig = str(input())
print(dict_syn[word_orig])