def check_marker(marker: str):
    lst = []
    lst_i = []

    for i in range(len(marker)):
        if marker[i] in lst:
            index_to_delete = lst.index(marker[i]) + 1
            lst = lst[index_to_delete:]
            lst_i = lst_i[index_to_delete:]
            lst.append(marker[i])
            lst_i.append(i)
            continue
        else:
            lst.append(marker[i])
            lst_i.append(i)

        if len(lst) == 14:
            return i

        if i + 1 == len(marker):
            return len(marker) - len(lst)


with open('data6.txt', 'r') as file:
    marker = file.read()
    index = check_marker(marker)
    print(index)




