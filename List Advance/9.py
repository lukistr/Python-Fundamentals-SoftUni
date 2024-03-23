def merge_elements(data, start, end):
    start_index = max(0, min(start, len(data) - 1))
    end_index = max(0, min(end, len(data) - 1))
    merged = ''.join(data[start_index:end_index + 1])
    data[start_index:end_index + 1] = [merged]

def divide_element(data, index, partitions):
    element = data[index]
    partition_length = len(element) // partitions
    extra_chars = len(element) % partitions
    divided = [element[i:i+partition_length] for i in range(0, len(element), partition_length)]
    if extra_chars:
        divided[-1] += element[-extra_chars:]
    data[index:index + 1] = divided

def process_commands(data, commands):
    for command in commands:
        if command == "3:1":
            print(' '.join(data))
            break
        operation, *args = command.split()
        if operation == "merge":
            start, end = map(int, args)
            merge_elements(data, start, end)
        elif operation == "divide":
            index, partitions = map(int, args)
            divide_element(data, index, partitions)

data = input().split()
commands = []
while True:
    command = input()
    if command == "3:1":
        commands.append(command)
        break
    commands.append(command)

process_commands(data, commands)
