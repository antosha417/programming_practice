"""Занятие 7. Списки
Задача «Уникальные элементы»
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить
в том порядке, в котором они встречаются в списке."""
def occurredOnce(l, n):
    mp = dict()
    # Store all the elements in the
    # map with their occurrence
    for i in range(n):
        if l[i] in mp.keys():
            mp[l[i]] = -100
        else:
            mp[l[i]] = i

    # invert mapping
    mp_invert = {v: k for k, v in mp.items()}

    delete = [key for key in mp_invert if key == -100]

    for key in delete: del mp_invert[key]

    for t in mp_invert:
        print(mp_invert[t], end=" ")


l = list(map(int, input().split()))
n = len(l)

occurredOnce(l, n)
