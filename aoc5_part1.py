from collections import deque

my_stacks = [deque(['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V']), deque(['D', 'Q', 'L']),
             deque(['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B']), deque(['L', 'C', 'D', 'H', 'B', 'Q', 'G']),
             deque(['V', 'G', 'L', 'F', 'Z', 'S']), deque(['D', 'G', 'N', 'P']),
             deque(['D', 'Z', 'P', 'V', 'F', 'C', 'W']), deque(['C', 'P', 'D', 'M', 'S']),
             deque(['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C'])]
commands = []
for i in range(501):
    commands.append(input())

for command in commands:
    a = command.split(' from ')
    count = int(a[0].split()[1])
    stack_from = int(a[1].split(' to ')[0])
    stack_to = int(a[1].split(' to ')[1])
    for i in range(count):
        element = my_stacks[stack_from - 1].pop()
        my_stacks[stack_to - 1].append(element)

for i in range(len(my_stacks)):
    n = len(my_stacks[i]) - 1
    print(my_stacks[i][n], end='')
