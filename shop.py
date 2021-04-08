print("Welcome to the MyProtein, you can pick the following products \noption 1: whey_protein - £8.99 \noption 2: nprotein_bar - £1.50 \noption 3: workout_leggings - £42.00 \noption 4: mp_t_shirt - £15.00\noption 5: multivitamin_tablets - £7.99 \noption 6: cycling_shorts - £19.99 \noption 7: shaker - 5.00 \noption 8: pre_workout - £39.99 \noption 9: sugar_free_syrup - £6.49 \nopyion 10: protein_spread - £6.99 \n")

buy_flag = 1
total_cost = float(0)

while buy_flag != 0:
    option = int(input("Which option would you like to purchase?: "))

    if option == 1:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 8.99
        print("The price is: " + str(total))
    elif option == 2:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 1.50
        print("The price is: " + str(total))
    elif option == 3:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 42.00
        print("The price is: " + str(total))
    elif option == 4:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 15.00
        print("The price is: " + str(total))
    elif option == 5:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 7.99
        print("The price is: " + str(total))
    elif option == 6:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 19.99
        print("The price is: " + str(total))
    elif option == 7:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 5.00
        print("The price is: " + str(total))
    elif option == 8:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 39.99
        print("The price is: " + str(total))
    elif option == 9:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 6.49
        print("The price is: " + str(total))
    elif option == 10:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 6.99
        print("The price is: " + str(total))
    elif option >= 11:
        total = 0
        print("sorry not a valid option")
    elif option == 0:
        total = 0
        print("sorry not a valid option")


    total_cost += total


    buy_flag = int(input("Would you like another item? enter Yes (1) or No (0):"))

discount = total_cost * 0.15
final_cost = total_cost - discount

print("You saved £", round(discount, 2), sep="",end="")
print("! The total price of your basket is: £", round(final_cost, 2), sep="")
