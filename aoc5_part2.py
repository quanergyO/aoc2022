my_inp = [['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'], ['D', 'Q', 'L'], ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
          ['L', 'C', 'D', 'H', 'B', 'Q', 'G'], ['V', 'G', 'L', 'F', 'Z', 'S'], ['D', 'G', 'N', 'P'],
          ['D', 'Z', 'P', 'V', 'F', 'C', 'W'], ['C', 'P', 'D', 'M', 'S'], ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]


commands = []
for i in range(501):
    commands.append(input())


for command in commands:
    a = command.split(' from ')
    count = int(a[0].split()[1])
    stack_from = int(a[1].split(' to ')[0])
    stack_to = int(a[1].split(' to ')[1])
    elements = []
    for i in range(count):
        element = my_inp[stack_from - 1].pop()
        elements.append(element)
    my_inp[stack_to - 1] += elements[::-1]


for i in range(len(my_inp)):
    n = len(my_inp[i]) - 1
    print(my_inp[i][n], end='')
