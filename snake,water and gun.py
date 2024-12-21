# snake, water and gun game
import random

print('\nWelcome to snake, water and gun game')
print('Press ctrl+c to exit')
print("NOTE: CHOOSE ONLY NUMBERS\n")
game_list = {'Snake':0, 'Water':1, 'Gun':2}
choose = [0, 1, 2]
for i in game_list.keys():
    print(f'{i}: {game_list[i]}')


try:    
    while True:    
        computer_choose = random.choice(choose)
        player_choose = int(input('Player choose: '))
        print(f'Computer choose: {computer_choose}')
        if player_choose == computer_choose:
            print('Tie\n')
        elif (player_choose == 0) and (computer_choose == 2):
            print('Loose\n')
        elif (player_choose == 0) and (computer_choose == 1):
            print('Win\n')
        elif (player_choose == 1) and (computer_choose == 0):
            print('Loose\n')
        elif (player_choose == 1) and (computer_choose == 2):
            print('Loose\n')
        elif (player_choose == 2) and (computer_choose == 2):
            print('Win\n')
        elif (player_choose == 2) and (computer_choose == 1):
            print('Loose\n')
        else:
            print('Player NOT choose/WRONG\n')
            continue
except:
    print('Exit\n')