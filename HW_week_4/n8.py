dict0 = {'Давка' : 'Толкотня', 'Жизнь' : 'Существование', 'Преподаватель' : 'Учитель', 'Худой' : 'Тощий',
         'Шкаф' : 'Гардероб'}
word = input()
some_num = 0
for i in dict0:
    if i == word:
        print(dict[i])
        some_num += 1
if some_num == 0:
    for i in dict0:
        if dict0[i] == word:
            print(i)