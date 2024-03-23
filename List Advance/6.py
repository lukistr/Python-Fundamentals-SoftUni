electrons = int(input())
shell = []
shell_row = 1
if electrons > 2:
    while True:
        row = 2 * (shell_row ** 2)
        if electrons > row:
            shell.append(row)
        else:
            shell.append(electrons)
            break
        electrons -= row
        shell_row += 1
else:
    shell.append(electrons)
print(shell)