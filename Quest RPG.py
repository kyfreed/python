playing = True
while playing:
    food = 10
    max_food = 10
    water = 10
    max_water = 10
    gold = 75
    max_gold = 75
    endurance = 10
    health = 15
    inventory = []
    landscape = [['-,-,-,-,-,-,-,-,-,-,-,-,-,-,X'] ,['-,S,-,-,-,-,-,-,-,-,-,-,-,S,-'] ,['-,S,-,-,-,-,-,R,-,-,-,-,-,S,-'] ,['-,-,-,-,-,-,-,^,-,-,-,-,-,^,-'] ,['-,-,-,-,-,-,-,S,-,-,-,-,S,-,-'] ,['-,-,I,-,-,I,-,-,-,-,-,R,-,-,-'] ,['^,^,^,^,^,^,^,^,^,^,^,^,^,^,^'] ,['-,-,^,-,-,^,-,-,-,-,^,-,-,-,-'] ,['-,-,S,-,-,S,-,S,-,-,S,S,-,-,-'] ,['R,R,R,R,R,R,R,R,R,R,R,R,R,R,R'] ,['-,-,I,-,-,-,I,-,-,-,-,-,I,-,-'] ,['^,-,S,-,-,S,-,-,-,S,-,^,-,-,-'] ,['-,S,-,S,-,-,S,-,-,-,-,S,-,-,-'] ,['-,I,-,-,^,^,-,I,-,-,-,-,-,^,-'] ,['O,-,-,-,-,-,-,-,-,-,-,-,-,-,-']]
    landscape2 = "\n".join(["".join(sublst) for sublst in landscape])
    landscape3 = landscape2.replace(',','')
    print('''You have found a treasure map.\n''' + landscape3 +'''
    O = You are here
    X = Treasure
    ^ = Mountain (Must consume 2 Food and 2 Water to get over)
    R = Ruin (Contains Monsters that must be fought with a Sword)
    S = Store (Things can be bought with Gold here)
    I = Inn ( Endurance and Health will be restored to max here.)

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
            print('You can\'t go any farther! Game over!')
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
            print(landscape3)
        if turn.upper() == 'MOVE(E)':
            for i in landscape:
                if 'O' in landscape[i]:
                    loc = landscape[i].index('O')
                    move = loc + 1
                    player = landscape.pop(loc)
                    landscape[i].insert(loc, '-')
                    landscape[].insert(move, player)
                    break
    again = input('Play again? (y/n) ')
    if again == 'y':
        continue
    elif again == 'n':
        playing = False
    else:
        print('Try again.')
        continue
        
    




    
