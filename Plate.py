#we create class plate to access inputs if customer chooses plate to eat
#it has inputs interest_two will replaced by option_four
#and quantity_one will replaced by quantity of plate
class Plate:
    our_lists = {"Lazagna Italiano":25,"Salad":10, "Chicken Rice":20,
     "Chicken Spaghetti":21, "Salad Rice":16, "Special Plate":30}

    def __init__(self,interest_two,quantity_one):
        self.interest_two = interest_two
        self.quantity_one = quantity_one

    def __repr__(self):
        return "Good!, you choose {a} and the number of {a} you want is {b} ,The price for one is ${c} and the price for {b} is ${d}" . format(a=self.interest_two, 
        b = self.quantity_one , d = self.number_of_plates() , c=self.choice_one())
#choice_one() takes the price of the plate from our dictionary above that the customer chooses
    def choice_one(self):
        price = 0
        for prices in self.our_lists.keys():
            if self.interest_two == prices:
                price += self.our_lists[prices]
                return price
#number_of_plates() calculates the total price for  plate
    def number_of_plates(self):
        whole_price_one = self.quantity_one * self.choice_one()
        return whole_price_one
# option_four = ""
# while True:
#     choice_four= str(input("enter 1 or 2"))
#     if choice_four == str(1):
#         option_four += "Lazagna Italiano"
#         break
#     elif choice_four == str(2):
#         option_four += "Chicken Spaghetti"
#         break
#     elif choice_four == str(3):
#         option_four += "Chicken Rice"
#         break
#     elif choice_four == str(4):
#         option_four += "Salad Rice"
#         break
#     elif choice_four == str(5):
#         option_four += "Salad"
#         break
#     elif choice_four == str(6):
#         option_four += "Special Plate"
#         break
#     else:
#         print ("please enter the correct options")
#         continue

# while True:
#     quantity_of_plate = input("write the number of plate?")
#     try:
#         quantity_of_plate = int(quantity_of_plate)
#         break
#     except:
#         print("enter only numbers please!")
#         continue

# customer_four=Plate(option_four,quantity_of_plate)
# print(customer_four)
