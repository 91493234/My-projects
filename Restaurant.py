# Restaurant 

print('\nWELCOME TO OUR RESTAURANT HONEYCOMB🍯🍔🍟🍕☕')
items = {"Coffee":49,'Pizza':19,'Tea':49,"Burger":99,'Frites':89}

print("\nPlease choose your order")
for x in items:
  print(f'{x}: ₹{items[x]}')

user_order = input('\nEnter your order: ').title()


if user_order in items:
    print("Order is added.")
    ask_again=input("\nDo you want any more: ").title()

    if ask_again == "Yes":
        order_2 = input('\nEnter your second order: ').title()
         
        if order_2 in items:
            print("Order is added.")
            print("Total amount is:" ,items[user_order]+items[order_2])
            exit()
        else:
            print("order is not available")
    else:
        print("Total amount is:" ,items[user_order])
        exit()        
else:
    print("order is not available")

