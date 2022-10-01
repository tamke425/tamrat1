#We are importing classes from the modules listed below
from Menu import Menu
from Sandwich import Sandwich
from Burger import Burger
from Shewarma import Shewarma
from Plate import Plate
#we declare variable which are goin to replace choices based on our customer's interests
option = ""
option_one = ""
option_two = ""
option_three = ""
option_four = ""
total = 0
#we have one large while loop and several nested loops inside it. We create this while loop to accept
#orders from customers
print("                 WELCOME TO FOOD ZONE!")
print("        You can place your orders here, please follow the instructions.") 
while True:
#This loop below will connect with class Menu and it will provide the customer information about what options are in our restaursnt
    while True:
        
        choice = str(input("We have two catagories for our foods we provide\n Enter\n \"1\" for \"SANDWICHES\"\n \"2\" for \"PLATES\"\n"))
        if choice == str(1):
            
            option += "sandwiches"
            break
        elif choice == str(2):
            option += "plates"
            break
        else:
            print ("please enter the correct options")
            continue
    
    customer = Menu(option)
    print(customer)
#Below the while loop will process if only option_one is sandwich means if we enter "1" on the above input
#and it will give us choce from burger or shewarma 
    while True:
        if option == "sandwiches":
            
            choice_one = str(input("GREAT! Our SANDWICHES:\n Enter\n \"1\" for \"BURGERS\"\n \"2\" for \"SHEWARMA\"\n"))
            if choice_one == str(1):
                
                option_one += "Burger"
                break
            elif choice_one == str(2):
                option_one += "Shewarma"
                break
            else:
                print ("please enter the correct options")
                continue

            customer_one = Sandwich(option_one)
            print(customer_one)
        else:
            break

#this loop will run if we choose burger from our sandwich choice, and it will give as choices from our dictionary in burger class 
#plus it accepts our choice
#it processes our input inside Burger class 
    while True:
        if option_one == "Burger":
            
            choice_two= str(input('''Cool! OUR BURGERS ARE:
                                    LIST               PRICE      
                                1.SPECIAL BURGER     $13
                                2.BIG BURGER         $8
                                3.DOUBLE BURGER      $10
                                4.HUM BURGER         $6
                                5.CHICKEN BURGER     $7
                                6.CHEESE BURGER      $5
                         Please,Enter the corresponding number of your choice!\n'''))
            if choice_two == str(1):
                
                option_two += "Special Burger"
                break
            elif choice_two == str(2):
                option_two += "Big Burger"
                break
            elif choice_two == str(3):
                option_two += "Double Burger"
                break
            elif choice_two == str(4):
                option_two += "Hum Burger"
                break
            elif choice_two == str(5):
                option_two += "Chicken Burger"
                break
            elif choice_two == str(6):
                option_two += "Cheese Burger"
                break
            else:
                print ("please enter the correct options")
                continue
        else:
            break

#if our chice is burger  this code will calculate total price by taking input(how many) from the user      
    while True:
        if option_one == "Burger":
            quantity_of_burgers = input("How many {burgers} you want?\n" .format(burgers = option_two))
            try:
                quantity_of_burgers = int(quantity_of_burgers)
                customer_two=Burger(option_two,quantity_of_burgers)
                total += customer_two.number_of_burgers()
                print(customer_two)
                break
            except:
                print("enter only number of Burger please!")
                continue
        else:
            break

#this loop will run if we choose shewarma from options in sandwich, and it will give as choices from our dictionary shewarma class
# plus it accepts our choice
#it processes our input inside Shewarma class 
    while True:
        if option_one == "Shewarma":
            
            choice_three= str(input('''GREAT! OUR SHEWARMAS ARE:
                                     LISTS                     PRICE
                                1.SMALL CHICKEN SHEWARMA     $7
                                2.MIDIUM CHICKEN SHEWARMA    $10
                                3.BIG CHICKEN SHEWARMA       $12
                                4.SMALL BEEF SHEWARMA        $8
                                5.MIDIUM BEEF SHEWARMA       $11
                                6.BIG BEEF SHEWARMA          $13
                        Please,Enter the corresponding number of your choice!\n'''))
            if choice_three == str(1):
                option_three += "Small Chicken Shewarma"
                break
            elif choice_three == str(2):
                option_three += "Midium Chicken Shewarma"
                break
            elif choice_three == str(3):
                option_three += "Big Chicken Shewarma"
                break
            elif choice_three == str(4):
                option_three += "Small Beef Shewarma"
                break
            elif choice_three == str(5):
                option_three += "Midium Beef Shewarma"
                break
            elif choice_three == str(6):
                option_three += "Big Beef Shewarma"
                break
            else:
                print ("please enter the correct options")
                continue
        else:
            break

#if our choice is shewarma  this code will calculate total price by taking input(how many) from the user  
    while True:
        if option_one == "Shewarma":    
            quantity_of_shewarma = input("How many {shewarma} you want you want?\n" .format(shewarma = option_three))
            try:
                    
                quantity_of_shewarma = int(quantity_of_shewarma)
                customer_three=Shewarma(option_three,quantity_of_shewarma)
                total += customer_three.number_of_shewarma()
                print(customer_three)
                break
            except:
                print("enter only number of shewarma please!")
                continue

        else:
            break
#this loop will run if we choose plates from our first option, and it will give as choices from our dictionary in plate class
# plus it accepts our choice
#it processes our input inside plate class
    while True:
        if option == "plates":
            
            choice_four= str(input('''Cool! OUR PLATE FOODS ARE:
                                    LISTS                PRICE
                                1.LAZAGNA ITALIANO       $25
                                2.CHICKEN SPAGHETTI      $21
                                3.CHICKEN RICE           $20
                                4.SALAD RICE             $16
                                5.SALAD                  $10
                                6.SPECIAL PLATE          $30
                            Please,Enter the corresponding number of your choice!\n'''))
            if choice_four == str(1):
                option_four += "Lazagna Italiano"
                break
            elif choice_four == str(2):
                option_four += "Chicken Spaghetti"
                break
            elif choice_four == str(3):
                option_four += "Chicken Rice"
                break
            elif choice_four == str(4):
                option_four += "Salad Rice"
                break
            elif choice_four == str(5):
                option_four += "Salad"
                break
            elif choice_four == str(6):
                option_four += "Special Plate"
                break
            else:
                print ("please enter the correct options")
                continue
        else:
            break

#if our choice is plate  this code will calculate total price by taking input(how many) from the user  
    while True:
        if option == "plates":
            quantity_of_plate = input("How many {plates} you want?\n" .format(plates = option_four))
            try:
                quantity_of_plate = int(quantity_of_plate)
                customer_four = Plate(option_four,quantity_of_plate)
                total += customer_four.number_of_plates()
                print(customer_four)
                break
            except:
                print("enter only number of plates please!")
                continue

        else:
            break
 #Hear we are assigning our variables again because if we are working inside our loop the variables must be same like the first
 #to excute in a right way   
    option = ""
    option_one = ""
    option_two = ""
    option_three = ""
    option_four = ""
#We are asking the user toput more orders,if the user want to put more order the loop will start again,else it will break from the loop
    while True:
        Add_more = str(input('''IS THAT ALL?
                                 1.NO   2.YES
                            ENTER THE CORRESPONDING NUMBER PLEASE.\n'''))
        if Add_more == str(1):
            break
        elif Add_more == str(2):
            break
        else:
            print("enter only 1 or 2")
            continue

    if Add_more == str(1):
        continue
    if Add_more == str(2):
        break

print("You have to pay ${total}" .format(total = total))
#After finishing taking orders ,the program will ask the user to make payment 
#it uses while loop and it works like others in the above
while True:
        payment_method = str(input('''You want to pay by card or cash?
                                 1.CARD   2.CASH   3.CANCEL
                            ENTER THE CORRESPONDING NUMBER PLEASE.\n'''))
        if payment_method == str(1):
            pin = input("ENTER YOUR PASSWORD,THEN PRESS ENTER\n")
            print("Processing...........")
            print("Take your receipt please.")
            print("Thank you,enjoy your meal.")
            break
        elif payment_method == str(2):
            print("Please go to cashier window to pay")
            break
        elif payment_method == str(3):
            total = 0
            print("This order is cancelled")
            break
        else:
            print("Enter the correct option please.")
            continue

       
