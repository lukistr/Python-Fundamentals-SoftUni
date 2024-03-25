rooms = int(input())
chairs, visitors, free, room_num = 0, 0, 0, 0
game_on = True
for i in range(rooms):
    room_num += 1
    data = input().split(' ')
    chairs = int(len(data[0]))
    visitors = int(data[1])
    free += (chairs - visitors)
    if visitors > chairs:
        print(str(visitors - chairs), 'more chairs needed in room', room_num)
        game_on = False
if game_on:
    print('Game On,', free, 'free chairs left')
