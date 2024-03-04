from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()

money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()

is_going = True
while is_going == True:
    user_choice = input("What would you like? latte, cappuccino, espresso")
    if user_choice == "off":
        is_going = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":
        user_selected_coffee = coffee_menu.find_drink(user_choice)
        is_sufficient = coffee_maker.is_resource_sufficient(user_selected_coffee)
        if is_sufficient == True:
            money_machine.make_payment(user_selected_coffee.cost)
            coffee_maker.make_coffee(user_selected_coffee)







