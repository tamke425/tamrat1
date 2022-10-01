#We are creating Menu class with an input interest
#interest will be replaced by option
class Menu:
    def __init__(self,interest):
        self.interest = interest

    def __repr__(self):
            return "Great Choice!, we have the best {x} in the city" . format (x=self.interest)


# option = ""
# while True:
#     choice = str(input("enter 1 or 2"))
#     if choice == str(1):
#         option += "sandwiches"
#         break
#     elif choice == str(2):
#         option += "plates"
#         break
#     else:
#         print ("please enter the correct options")
#         continue
    
# customer = Menu(option)
# print(customer)
