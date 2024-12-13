import random

character = 'qwertyuioplkjhgfdsazxcvbnm[]{!@#$%^&*()|?/><,1234567890}'
ask_digit = input('How many digit password you want: ')
convert_in_int = int(ask_digit) 

password=''
while (len(password)<convert_in_int):
    password +=random.choice(character)
print(password)