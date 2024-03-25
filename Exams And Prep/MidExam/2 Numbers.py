numberList = input().split()

while True:
    commandList = input().split()
    if commandList[0] == 'Finish':
        break
    elif commandList[0] == 'Add':
        numberList.append(commandList[1])
    elif commandList[0] == 'Remove':
        for i in reversed(numberList):
            if i == commandList[1]:
                numberList.remove(i)
                break
    elif commandList[0] == 'Replace':
        for i in range(len(numberList)):
            if numberList[i] == commandList[1]:
                numberList[i] = commandList[2]
                break
    elif commandList[0] == 'Collapse':
        for i in range(len(numberList) - 1, -1, -1):
            if int(numberList[i]) < int(commandList[1]):
                numberList.pop(i)

print(' '.join(numberList))
