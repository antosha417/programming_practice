text = input()
n = int(input())
new_text = (text + ', ') * (n - 1)
print('Hello, ' + new_text + text)