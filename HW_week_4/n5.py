list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 8, 6, 4, 2]
set1 = set(list1)
set2 = set(list2)
intersection_list = sorted(list(set1 & set2))
print(intersection_list)