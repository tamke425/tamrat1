#we create class Burger to access inputs if customer chooses burger to eat
#it has inputs interest_two will replaced by option_two
#and quantity_one will replaced by quantity of burgers
class Burger:
    our_lists = {"Big Burger":8 ,"Special Burger":13, "Chicken Burger":7, "Cheese Burger":5, "Double Burger":10, "Hum Burger":6}

    def __init__(self,interest_two,quantity_one):
        self.interest_two = interest_two
        self.quantity_one = quantity_one


    def __repr__(self):
        return "Good!, you choose {a} and the number of {a} you want is {b} ,The price for one is ${c} and the price for {b} is ${d}" . format(a=self.interest_two, 
        b = self.quantity_one , d = self.number_of_burgers() , c=self.choice_one())
#choice_one() takes the price of the burger from the dictionary above that the customer chooses

    def choice_one(self):
        price = 0
        for prices in self.our_lists.keys():
            if self.interest_two == prices:
                price += self.our_lists[prices]
                return price
#number_of_burgers() calculates the total price for  burgers

    def number_of_burgers(self):
        whole_price_one = self.quantity_one * self.choice_one()
        return whole_price_one
# option_two = ""
# while True:
#     choice_two= str(input("enter 1 or 2"))
#     if choice_two == str(1):
#         option_two += "Special Burger"
#         break
#     elif choice_two == str(2):
#         option_two += "Big Burger"
#         break
#     elif choice_two == str(3):
#         option_two += "Double Burger"
#         break
#     elif choice_two == str(4):
#         option_two += "Hum Burger"
#         break
#     elif choice_two == str(5):
#         option_two += "Chicken Burger"
#         break
#     elif choice_two == str(6):
#         option_two += "Cheese Burger"
#         break
#     else:
#         print ("please enter the correct options")
#         continue

# while True:
#     quantity_of_burgers = input("write the number of burgers?")
#     try:
#         quantity_of_burgers = int(quantity_of_burgers)
#         break
#     except:
#         print("enter only numbers please!")
#         continue

# customer_two=Burger(option_two,quantity_of_burgers)
# print(customer_two)
