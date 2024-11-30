print("Press 'e' to exit")
print("Calculator")


while True:
    num_1 = input()

    if num_1.lower() == "e":
        break

    # evaluate = eval(num_1) # convert string to integer and use eval() to evaluate the expression


    try :
        print(eval(num_1))
    except :
        print("ERROR")

