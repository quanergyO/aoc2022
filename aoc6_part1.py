def check_marker(marker: str):
    lst = []
    for i in range(len(marker)):
        if marker[i] in lst:
            lst = []
            continue
        else:
            lst.append(marker[i])

        if len(lst) == 4:
            return i


with open('data6.txt', 'r') as file:
    marker = file.read()
    index = check_marker(marker)
    print(index)

