import random

rand_num_1 = random.randint(0, 25)
rand_num_2 = random.randint(0, 25)
rand_num_3 = random.randint(0, 25)
rand_num_4 = random.randint(0, 25)
rand_num_5 = random.randint(0, 25)
rand_num_6 = random.randint(0, 25)
rand_character = 'qwertyuiopasdfghjklzxcvbnm'

rand_str = rand_character[rand_num_1] + rand_character[rand_num_2] + rand_character[rand_num_3]
rand_str_2 = rand_character[rand_num_4] + rand_character[rand_num_5] + rand_character[rand_num_6]


code_decode = input("what you want code/decode: ").title()

if code_decode == 'Code':
    user_input = input("Enter a word want to Code: ")
    length = len(user_input)

    if length > 3:
        reverse_user_input = ''.join(reversed(user_input))
        replace = reverse_user_input.replace(reverse_user_input[0],'')
        add = replace + reverse_user_input[0]
        add_rand_character = rand_str + add + rand_str_2
        print(add_rand_character)

    else:
        print(user_input[::-1]) 
    
elif code_decode == 'Decode':
    user_input_2 = input("Enter a word want to Decode: ")
    length_1 = len(user_input_2)
    if length_1 > 3:
        decode_1 = user_input_2[0:3]
        remove = user_input_2.replace(decode_1,'')
        rereverse = remove[:: -1]
        decode_2 = rereverse[0:4]
        remove_1 = rereverse.replace(decode_2,'')
        add_character =  remove_1 + user_input_2[-4] 
        print(add_character)
    else:
        print(user_input_2[::-1])
else:
    print("You doesn't choose code/decode")

