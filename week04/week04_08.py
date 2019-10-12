"""Занятие 11. Словари
Задача «Словарь синонимов»
Условие
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним."""

N = int(input())
l = []
d = {}
for i in range(N):
    l = list(map(str, input().split()))
    d[l[0]] = l[1]

d_invert = {v: k for k, v in d.items()} # invert dictionary
key = input()
if key in d.keys():
    print(d[key])
else:
    print(d_invert[key])