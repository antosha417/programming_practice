def zaelo(phrase, x):
    result = (', ' + phrase) * n
    return result

text = input()
n = int(input())
phrase = zaelo(text, n)
print('Hello' + phrase)
