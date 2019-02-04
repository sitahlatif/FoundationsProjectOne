####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Sitah's shop"
signature_flavors = ["tuna", "salmon", "red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("Our menu:")
    for key , value in menu.items(): 
       
        print ('- "%s" (KD %s)' %(key, value))
        



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for lst in original_flavors:
        print ('- "%s"' % (lst))

    # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for lst in signature_flavors:
        print ('- "%s"' % (lst))
    # your code goes here!


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    for o in menu :
        if (o == order):
            return True
      
    for o in original_flavors :
        if (o == order):
            return True 
       

    for o in signature_flavors :
        if (o == order):
            return True 
            
    return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    
    # your code goes here!
    #order = input("What's your order? (Enter The exact spelling of the item you want.Type 'Exit' to end your order.)")
   # while order != "Exit":
    #    if 
     #  print (order)
      # order_list.append(order);
       #user += 1
    print ("What's your order? (Enter The exact spelling of the item you want.Type 'Exit' to end your order.")
    
    while True:
        user = input()
        if (user == "Exit" or user == "exit"):
         break
        elif is_valid_order(user):
             order_list.append(user)
        else :
            print("Invalid it's not in the menu")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!

    if total > 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    
    for olst in order_list:
        if olst in menu :
            total += menu[olst]
        elif olst in original_flavors:
            total += original_price
        else:
            total += signature_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
   
    print("Your order is:")
    for l in order_list:
        print("- %s" %(l))

    # your code goes here!
    total = get_total_price(order_list)
    print ("Total price is %s"%(total))
    if accept_credit_card(total):
        print("Your Order is eligiable by cash or credit card")
    else:
        print("You can bye by cash only ")
    print ("Thank you for shopping at Sitah's Shop")
