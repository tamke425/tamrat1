#We are creating Sandwich class with an input interest one
#interest one will replaced by option_one
class Sandwich:
    def __init__(self,interest_one):
        self.interest_one = interest_one

    def __repr__(self):
            return "Wow!, You can try one of our {x} that are listed below" . format (x=self.interest_one)

# option_one = ""
# while True:
#     choice_one = str(input("enter 1 or 2"))
#     if choice_one == str(1):
#         option_one += "Burger"
#         break
#     elif choice_one == str(2):
#         option_one += "Shewarma"
#         break
#     else:
#         print ("please enter the correct options")
#         continue
    
# customer_one = Sandwich(option_one)
# print(customer_one)



