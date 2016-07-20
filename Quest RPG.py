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
    def landedOnStore():
        global food
        global water
        global gold
        global max_food
        global max_water
        global max_gold
        global inventory
        while True:
            options = []
            optionDisplay = ''
            foodAvailable = (food == max_food)
            waterAvailable = (water == max_water)
            canteenAvailable = True
            canteenNumber = 0
            for i in range(0, len(inventory) - 1):
                if canteenNumber == 3:
                    canteenAvailable = False
                    break
                if inventory[i] == 'canteen':
                    canteenNumber += 1
            lunchBoxAvailable = True
            lunchBoxNumber = 0
            for i in range(0, len(inventory) - 1):
                if lunchBoxNumber == 3:
                    lunchBoxAvailable = False
                    break
                if inventory[i] == 'lunchbox':
                    lunchBoxNumber += 1
            bigBagAvailable = True
            bigBagNumber = 0
            for i in range(0, len(inventory) - 1):
                if bigBagNumber == 3:
                    bigBagAvailable = False
                    break
                if inventory[i] == 'big bag':
                    bigBagNumber += 1
            swordAvailable = True
            for i in range(0, len(inventory) - 1):
                if inventory[i] == 'sword':
                    swordAvailable = False
            if foodAvailable:
                options.append('food')
                optionDisplay += '\n Food: 5 Gold'
            if waterAvailable:
                options.append('water')
                optionDisplay += '\n Water: 5 Gold'
            if canteenAvailable:
                options.append('canteen')
                optionDisplay += '\n Canteen: 25 Gold'
            if lunchBoxAvailable:
                options.append('lunchbox')
                optionDisplay += '\n Lunchbox: 25 Gold'
            if bigBagAvailable:
                options.append('big bag')
                optionDisplay += '\n Big Bag: 50 Gold'
            if swordAvailable:
                options.append('sword')
                optionDisplay += '\n Sword: 50 Gold'
            print('Welcome to the store! Here\'s what\'s available:' + optionDisplay)
            choice = input('What would you like? Type \'help\' for help. ')
            chosenItem = ''
            for i in range(0, len(options) - 1):
                if options[i] == choice.lower():
                    chosenItem = options[i]
            if choice.lower() == 'help':
                print('''To buy something, type the name of it, or type 'leave' to leave the store.
Canteens let you carry more water.
Lunchboxes let you carry more food.
Big Bags let you carry more gold.''')
            if choice.lower() == 'leave':
                return
            if chosenItem == 'food':
                if gold < 5:
                    print('You don\'t have enough gold.')
                    continue
                gold -= 5
                food += 1
                print('You bought 1 food.')
                continue
            if chosenItem == 'water':
                if gold < 5:
                    print('You don\'t have enough gold.')
                    continue
                gold -= 5
                water += 1
                print('You bought 1 water.')
            if chosenItem == 'canteen':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('canteen')
                gold -= 25
                max_water += 15
                print('You bought a canteen. You can hold 15 more water!')
            if chosenItem == 'lunchbox':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('lunchbox')
                gold -= 25
                max_food += 15
                print('You bought a lunchbox. You can hold 15 more food!')
            if chosenItem == 'big bag':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('big bag')
                gold -= 50
                max_gold += 50
                print('You bought a big bag. You can hold 50 more gold!')
            if chosenItem == 'sword':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('sword')
                gold -= 50
                print('You bought a sword. Now you can battle monsters in ruins!')
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
            if landed_space == 'S':
                landedOnStore()
        if turn.upper() == 'MOVE(N)':
            for i in range(0, len(landscape) - 1):
                if landscape[i] == 'O':
                    loc = i
                    move = i - 15
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
            print("You moved 1 space north.")
            print(landscape2)
            food -= 1
            water -= 1
            endurance -= 1
            if landed_space == 'S':
                landedOnStore()
    again = input('Play again? (y/n) ')
    if again == 'y':
        continue
    elif again == 'n':
        playing = False
    else:
        print('Try again.')
        continue

            
            
                      
        
    
                
    
    
        
        
    
            
        
    




    
