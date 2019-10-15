lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
st = set(lst)
for i in range(len(lst)):
    if (lst[i] in st) == True:
        print('No')
        st.discard(lst[i])
    else:
        print('Yes')


