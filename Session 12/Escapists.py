out = {
    "x": 3,
    "y": 2,
}
key = {
    "x": 2,
    "y": 1,
}
player = {
    "x": 1,
    "y": 2,
}

for y in range(4):
    for x in range(4):
        if(player['x'] == x and player['y'] == y):
            print("P", end=" ")
        elif (key['x'] == x and key['y'] == y):
            print("K", end=" ")
        elif (out['x'] == x and out['y'] == y):
            print("E", end=" ",)
        else:
            print("-", end=" ")
    print()
check = 0
while True:
    move = input("Your Move: ").upper()
    if(move == "D"):
        player['x'] += 1
        if  player['x'] <= 3:
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
        elif player['x'] > 3:
            player['x'] = 3
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
    elif(move == "W"):
        player['y'] -= 1
        if player['y'] >= 0:
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
        elif player['y'] < 0:
            player['y'] = 0
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
    elif(move == "A"):
        player['x'] -= 1
        if 0 <= player['x']:
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
        elif player['x'] < 0:
            player['x'] = 0
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
    elif(move == "S"):
        player['y'] += 1
        if player['y'] <= 3:
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
        elif player['y'] >3:
            player['y'] = 3
            for y in range(4):
                for x in range(4):
                    if(player['x'] == x and player['y'] == y):
                        print("P", end=" ")
                    elif (key['x'] == x and key['y'] == y):
                        print("K", end=" ")
                    elif (out['x'] == x and out['y'] == y):
                        print("E", end=" ",)
                    else:
                        print("-", end=" ")
                print()
    elif(move == "QUIT"):
        break
    if player['x'] == key['x'] and player['y'] == key['y']:
        print('You have the key!')
        check = 1
        key['x'] = 4
        key['y'] = 4
    if player['x'] == out['x'] and player ['y'] == out['y']:
        if check == 1:
            print('Winner Winner Chicken Dinner!')
            print('Credits: MeinSpaghett as Author')
            break
        else:
            print('Locked! Please find a key first')
