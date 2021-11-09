import time

def print_message(message_to_print):
    print(message_to_print)
    time.sleep(1)

def main_menu():
    print_message("*********************Dear Customer*********************\n")
    print_message("**********Welcome To pizza shop Main Menu**********\n")
    option = input("Select Option:\n"
                   "1.  Order the Pizza\n"
                   "2.  Exit the Program\n")
    if  option == '1':
        pizza_type()
    elif    option == '2':
        print("We Were Happy To Serve You, Most Welcomed Next Time!!!")

def pizza_type ():
    option = input("Select Pizza Type:\n"
                   "1.  Pepperoni\n"
                   "2.  Margherita\n"
                   "3.  Vegetarian\n"
                   "4.  Neapolitan")
    if  option == '1':
        pizza_size("Pepperoni")

def pizza_size (type):
    option = input("Select Pizza Type:\n"
                   "1.  Large (50 AED)\n"
                   "2.  Medium (40 AED)\n"
                   "3.  Small (30 AED)")
    if  option == '1':
        price = '50'
    elif    option == '2':
        price = '40'
    elif    option == '3':
        price = '30'
    else:
        print("Invalid Option Try Again")
        pizza_size()

def select_pizza_topping():
    print("Select Topping Here")
    option = input("Select Pizza Type:\n"
                     "1.  Olives\n"
                     "2.  Tomatoes\n"
                     "3.  Mushrooms\n"
                     "4.  Jalapenos")
    value = 0

    while True:
        pizza_topping(option)
        if (value < 3):
            continue

def pizza_topping (option):
    if option == '1':
        return "olives"
    elif option == '2':
        return "tomatoes"
    elif option == '3':
        return "mushrooms"
    elif option == '4':
        return "jalapenos"
    else:
        print("Invalid Option Please Try Again")
        select_pizza_topping()

if __name__ == '__main__':
    main_menu()