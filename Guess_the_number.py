import random

random_num = random.randint(1, 100)
attempt = 0
print('Guess the number between 1 and 100')

while True:
    
    attempt += 1
    user_guess = int(input("Guess the number: "))
    if user_guess < random_num:
        print('Too Low!')
    elif user_guess == random_num:
        print(f'You guess number in {attempt} attempts.')
        break
    else:
        print('Too High!')

