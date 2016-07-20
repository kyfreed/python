from random import randint
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
    max_endurance = 10
    health = 15
    max_health = 15
    inventory = []
    swordUpgrades = 0
    landscape = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','X','-','S','-','-','-','-','-','-','-','-','-','-','-','S','-','-','S','-','-','-','-','-','R','-','M','-','-','-','S','-','-','-','-','-','-','-','-','^','-','-','-','-','-','^','-','-','-','-','-','-','-','-','S','-','-','-','-','S','-','-','-','-','I','-','-','I','-','-','-','-','-','R','-','-','-','^','^','^','^','^','^','^','^','^','^','^','^','^','^','^','-','-','^','-','-','^','-','-','-','-','^','-','-','-','-','-','-','S','-','-','S','-','S','-','-','S','S','-','-','-','R','R','R','R','R','R','R','R','R','R','R','R','R','R','R','M','-','I','-','-','-','I','-','-','M','-','-','I','-','-','^','M','S','-','-','S','-','M','-','S','-','^','-','-','-','-','S','-','S','-','-','S','-','-','-','-','S','-','-','-','-','I','-','-','^','^','-','I','-','-','-','-','-','^','-','O','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
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
        global max_endurance
        global endurance
        food -= 1
        water -= 1
        endurance -= 1
        print('Welcome to the store!')
        while True:
            options = []
            optionDisplay = ''
            foodAvailable = (food != max_food)
            waterAvailable = (water != max_water)
            canteenAvailable = True
            canteenNumber = 0
            for i in range(0, len(inventory)):
                if canteenNumber == 3:
                    canteenAvailable = False
                    break
                if inventory[i] == 'canteen':
                    canteenNumber += 1
            lunchBoxAvailable = True
            lunchBoxNumber = 0
            for i in range(0, len(inventory)):
                if lunchBoxNumber == 3:
                    lunchBoxAvailable = False
                    break
                if inventory[i] == 'lunchbox':
                    lunchBoxNumber += 1
            bigBagAvailable = True
            bigBagNumber = 0
            for i in range(0, len(inventory)):
                if bigBagNumber == 3:
                    bigBagAvailable = False
                    break
                if inventory[i] == 'big bag':
                    bigBagNumber += 1
            swordAvailable = True
            for i in range(0, len(inventory)):
                if inventory[i] == 'sword':
                    swordAvailable = False
            shieldAvailable = True
            for i in range(0, len(inventory)):
                if inventory[i] == 'shield':
                    shieldAvailable = False
            sleepingBagAvailable = True
            sleepingBagNumber = 0
            for i in range(0, len(inventory)):
                if sleepingBagNumber == 3:
                    sleepingBagAvailable = False
                if inventory[i] == 'sleeping bag':
                    sleepingBagNumber += 1
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
            if shieldAvailable:
                options.append('shield')
                optionDisplay += '\n Shield: 50 Gold'
            if sleepingBagAvailable:
                options.append('sleeping bag')
                optionDisplay += '\n Sleeping Bag: 25 Gold'
            print('Here\'s what\'s available:' + optionDisplay)
            choice = input('What would you like? Type \'help\' for help. ')
            chosenItem = ''
            for i in range(0, len(options)):
                if options[i] == choice.lower():
                    chosenItem = options[i]
            if choice.lower() == 'help':
                print('''To buy something, type the name of it, or type 'leave' to leave the store. Use checkstats() to check stats.
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
                continue
            if chosenItem == 'canteen':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('canteen')
                gold -= 25
                max_water += 15
                print('You bought a canteen. You can hold 15 more water!')
                continue
            if chosenItem == 'lunchbox':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('lunchbox')
                gold -= 25
                max_food += 15
                print('You bought a lunchbox. You can hold 15 more food!')
                continue
            if chosenItem == 'big bag':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('big bag')
                gold -= 50
                max_gold += 50
                print('You bought a big bag. You can hold 50 more gold!')
                continue
            if chosenItem == 'sword':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('sword')
                gold -= 50
                print('You bought a sword. If you get the shield, you can battle monsters in ruins!')
                continue
            if chosenItem == 'shield':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    continue
                inventory.append('shield')
                gold -= 50
                print('You bought a shield. If you get the sword, you can battle monsters in ruins!')
                continue
            if chosenItem == 'sleeping bag':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    continue
                gold -= 25
                inventory.append('sleeping bag')
                max_endurance += 15
                print('You bought a sleeping bag. Your max endurance has been increased by 15!')
                continue
            if choice.lower() == 'checkstats()':
                print('Food: ' + str(food) + '\n' + 'Water: ' + str(water) + '\n' + 'Gold: ' + str(gold))
    def landedOnInn():
        global max_gold
        global gold
        global max_health
        global max_endurance
        global health
        global endurance
        global randint
        print('You stayed at an inn. Your endurance and health have been restored to max.')
        if randint(0, 2) == 1:
            print('The staff have given you golden to help you on your way!')
            if max_gold - gold < 50:
                gold = max_gold
            else:
                gold += 50
        endurance = max_endurance
        health = max_health
        if randint(0, 9) == 7:
            print('You also found a health container. Your max health has been increased by 3 and replenished!')
            max_health += 3
            health = max_health
        
    def landedOnMagic():
        global swordUpgrades
        global inventory
        global gold
        hasASword = False
        for i in range(0, len(inventory)):
            if inventory[i] == 'sword':
                hasASword = True
        if hasASword == False:
            print('You don\'t have a sword? You have no business here! Begone with you!')
            return
        if swordUpgrades == 0:
            swordBuy = input('The Basic Sword Upgrade is available for 25 gold. Would you like to buy?(y/n) ')
            if swordBuy.lower() == 'y':
                if gold < 25:
                    print('You don\'t have enough gold.')
                    return
                gold -= 25
                swordUpgrades = 1
                return
            else:
                return
        if swordUpgrades == 1:
            swordBuy = input('The Intermediate Sword Upgrade is available for 50 gold. Would you like to buy?(y/n) ')
            if swordBuy.lower() ==  'y':
                if gold < 50:
                    print('You don\'t have enough gold.')
                    return
                gold -= 50
                swordUpgrades = 2
                return
            else:
                return
        if swordUpgrades == 2:
            swordBuy= input('The Advanced Sword Upgrade is available for 75 gold. Would you like to buy?(y/n) ')
            if swordBuy.lower() == 'y':
                if gold < 75:
                    print('You don\'t have enough gold.')
                    return
                gold -= 75
                swordUpgrades = 3
                return
        if swordUpgrades == 3:
            print('There are no more sword upgrades available.')
            return
                
    print('''You have found a treasure map.\n''' + landscape2 +'''
    O = You are here
    X = Treasure
    ^ = Mountain (Must consume 2 Food, 2 Water, and 3 Endurance to get over)
    R = Ruin (Contains Monsters that must be fought with a Sword)
    S = Store (Things can be bought with Gold here)
    I = Inn (Endurance and Health will be restored to max here. However, takes 5 gold to stay)
    M = Magic House (You can upgrade your sword here)

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
            if landed_space == 'S':
                landedOnStore()
            elif landed_space == 'I':
                landedOnInn()
            elif landed_space == '^':
                food -= 2
                water-= 2
                endurance -= 3
            elif landed_space == 'M':
                landedOnMagic()
            else:
                food -= 1
                water -= 1
                endurance -= 1
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
            if landed_space == 'S':
                landedOnStore()
            elif landed_space == 'I':
                landedOnInn()
            elif landed_space == '^':
                food -= 2
                water -= 2
                endurance -= 3
            elif landed_space == 'M':
                landedOnMagic()
            else:
                food -= 1
                water -= 1
                endurance -= 1
    again = input('Play again? (y/n) ')
    if again == 'y':
        continue
    elif again == 'n':
        playing = False

            
            
                      
        
    
                
    
    
        
        
    
            
        
    




    
