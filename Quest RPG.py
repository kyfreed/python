playing = True
rows = 15
cols = 15
while playing:
    landed_space = '-'
    food = 10
    max_food = 10
    water = 10
    max_water = 10
    gold = 75
    max_gold = 75
    endurance = 10
    health = 15
    inventory = []
    landscape = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','X','-','S','-','-','-','-','-','-','-','-','-','-','-','S','-','-','S','-','-','-','-','-','R','-','-','-','-','-','S','-','-','-','-','-','-','-','-','^','-','-','-','-','-','^','-','-','-','-','-','-','-','-','S','-','-','-','-','S','-','-','-','-','I','-','-','I','-','-','-','-','-','R','-','-','-','^','^','^','^','^','^','^','^','^','^','^','^','^','^','^','-','-','^','-','-','^','-','-','-','-','^','-','-','-','-','-','-','S','-','-','S','-','S','-','-','S','S','-','-','-','R','R','R','R','R','R','R','R','R','R','R','R','R','R','R','-','-','I','-','-','-','I','-','-','-','-','-','I','-','-','^','-','S','-','-','S','-','-','-','S','-','^','-','-','-','-','S','-','S','-','-','S','-','-','-','-','S','-','-','-','-','I','-','-','^','^','-','I','-','-','-','-','-','^','-','O','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
    landscape2 = ''
    for i in range(0, rows):
        for j in range(0, cols):
            k = j + (rows * i)
            landscape2 += str(landscape[k])
        landscape2 += '\n'
    print('''You have found a treasure map.\n''' + landscape2 +'''
    O = You are here
    X = Treasure
    ^ = Mountain (Must consume 2 Food and 2 Water to get over)
    R = Ruin (Contains Monsters that must be fought with a Sword)
    S = Store (Things can be bought with Gold here)
    I = Inn ( Endurance and Health will be restored to max here. However, takes 5 gold to stay)

    You are currently only able to pack 10 food, 10 water, and 75 gold.
    Your quest begins now.''')

    while True:
        if food == 0:
            print('You starved! Game over!')
            break
        if water == 0:
            print('You have no water! Game over!')
            break
        if endurance == 0:
            print('You collapsed with exhaustion! Game over!')
            break
        if health == 0:
            print('You died! Game over!')
            break
        turn = input('Enter your choice. Type \'help()\' for help ')
        if turn.upper() == 'HELP()':
            print('''checkstats(): Check statistics
    move(dir): Move one space in direction dir
    (acceptable parameters are n, e, s, and w)
    rest(): Rest for one turn
    (You will recover 1 Endurance but 1 Food and 1 Water will still be consumed)
    checklandscape(): Check landscape
    help(): Display this menu
    giveup(): Give up''')
        if turn.upper() == 'CHECKSTATS()':
            print('Food: ' + str(food) + '\nWater: ' + str(water) + '\nGold: ' + str(gold) + '\nEndurance: ' + str(endurance) + '\nHealth: ' + str(health))
        if turn.upper() == 'REST()':
            food -= 1
            water -= 1
            endurance += 1
            print('You rested for 1 turn.')
        if turn.upper() == 'GIVEUP()':
            print('You gave up! Game over!')
            break
        if turn.upper() == 'CHECKLANDSCAPE()':
            print(landscape2)
        if turn.upper() == 'MOVE(E)':
            for i in range(0, len(landscape) - 1):
                if landscape[i] == 'O':
                    loc = i
                    move = i + 1
                    landscape[loc] = landed_space
                    landed_space = landscape[move]
                    landscape[move] = 'O'
                    landscape2 = ''
                    break
            for i in range(0, rows):
                for j in range(0, cols):
                    k = j + (rows * i)
                    landscape2 += str(landscape[k])
                landscape2 += '\n'
            print("You moved 1 space east.")
            print(landscape2)
            food -= 1
            water -= 1
            endurance -= 1
    again = input('Play again? (y/n) ')
    if again == 'y':
        continue
    elif again == 'n':
        playing = False
    else:
        print('Try again.')
        continue
        
    




    
