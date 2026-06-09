import random
rolls = []
dice_type = 0
continuity = 'Y'
while continuity == 'Y' or continuity == 'y':
    while dice_type == 0:
        dice_type = int(input('\t--- Dice Roller ---\n\tWelcome!\nChoose a type of dice:\n[1] D2\n[2] D4\n[3] D6\n[4] D8\n[5] D10\n[6] D12\n[7] D20\n- '))
        times = int(input('How many dices?\n- '))
        mod = int(input('Any modifier?\n- '))
        if dice_type == 1:
            faces = [random.randint(1, 2) for _ in range(times)]
        elif dice_type == 2:
            faces = [random.randint(1, 4) for _ in range(times)]
        elif dice_type == 3:
            faces = [random.randint(1, 6) for _ in range(times)]
        elif dice_type == 4:
            faces = [random.randint(1, 8) for _ in range(times)]
        elif dice_type == 5:
            faces = [random.randint(1, 10) for _ in range(times)]
        elif dice_type == 6:
            faces = [random.randint(1, 12) for _ in range(times)]
        elif dice_type == 7:
            faces = [random.randint(1, 20) for _ in range(times)]
        print('Rolling...')
        print(faces)
        rolls.extend(faces)
        print('This were your rolls: ')
        print(rolls)
        if times > 2:
            total = sum(rolls)
            print('Your total roll was...')
            print (total + mod)
        elif times == 2:
            total = sum(rolls)
            print('Your total roll was...')
            print (total + mod)
        else:
            print('Your total roll was...')
            print (faces)
    print('Wish to continue? [Y/N]')
    continuity = input('- ')
if continuity == 'N' or continuity == 'n':
    print('Ok! ending rolls...')
    exit()
elif continuity == 'Y' or continuity == 'y':
        dice_type = 0
        rolls = []

