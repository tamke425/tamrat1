#we create class shewarma to access inputs if customer chooses shewarma to eat
#it has inputs interest_two will replaced by option_three
#and quantity_one will replaced by quantity of shewarma
class Shewarma:
    our_lists = {"Big Chicken Shewarma":12,"Midium Chicken Shewarma":10, "Small Chicken Shewarma":7,
     "Big Beef Shewarma":13, "Midium Beef Shewarma":11, "Small Beef Shewarma":8}

    def __init__(self,interest_two,quantity_one):
        self.interest_two = interest_two
        self.quantity_one = quantity_one

    def __repr__(self):
        return "Good!, you choose {a} and the number of {a} you want is {b} ,The price for one is ${c} and the price for {b} is ${d}" . format(a=self.interest_two, 
        b = self.quantity_one , d = self.number_of_shewarma() , c=self.choice_one())
#choice_one() takes the price of the shewarma from our dictionary above that the customer chooses
    def choice_one(self):
        price = 0
        for prices in self.our_lists.keys():
            if self.interest_two == prices:
                price += self.our_lists[prices]
                return price
#number_of_plate() calculates the total price for  shewarma
    def number_of_shewarma(self):
        whole_price_one = self.quantity_one * self.choice_one()
        return whole_price_one
# option_three = ""
# while True:
#     choice_three= str(input("enter 1 or 2"))
#     if choice_three == str(1):
#         option_three += "Small Chicken Shewarma"
#         break
#     elif choice_three == str(2):
#         option_three += "Midium Chicken Shewarma"
#         break
#     elif choice_three == str(3):
#         option_three += "Big Chicken Shewarma"
#         break
#     elif choice_three == str(4):
#         option_three += "Small Beef Shewarma"
#         break
#     elif choice_three == str(5):
#         option_three += "Midium Beef Shewarma"
#         break
#     elif choice_three == str(6):
#         option_three += "Big Beef Shewarma"
#         break
#     else:
#         print ("please enter the correct options")
#         continue

# while True:
#     quantity_of_shewarma = input("write the number of shewarma?")
#     try:
#         quantity_of_shewarma = int(quantity_of_shewarma)
#         break
#     except:
#         print("enter only numbers please!")
#         continue

# customer_three=Shewarma(option_three,quantity_of_shewarma)
# print(customer_three)
