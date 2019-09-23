def even_or_not(a):
    even_elem = []
    for elem in a:
        if (elem % 2 == 0):
            even_elem.append(elem)
    return even_elem

list = [int(s) for s in input().split()]
result_list = even_or_not(list)
for elem in result_list:
    print(elem, end=' ')
