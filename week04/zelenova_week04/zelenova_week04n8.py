#8.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для слова из словаря, записанного в последней строке, определите его синоним.
# (pythontutor.ru, занятие 11, «Словарь синонимов»)
n=int(input())
sinom= dict(input().split() for k in range(n))
word = input()
try:
  if sinom.get(word) !=-1:
    print(sinom[word])
except KeyError:
             for i in sinom:
                   if sinom[i]==word:
                       print(i)


