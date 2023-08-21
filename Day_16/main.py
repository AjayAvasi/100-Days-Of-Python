from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    user_input = input(f"What drink would you like? ({menu.get_items()}): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "new item":
        name = input("What is the name of this item?: ")
        milk = int(input("How much milk is in this item?: "))
        water = int(input("How much water is in this item?: "))
        coffee = int(input("How much coffe is in this item?: "))
        cost = int(input("How much does this item cost?: "))
        new_item = MenuItem(name, water, milk, coffee, cost)
        menu.add_item(new_item)
    else:
        drink_data = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink_data):
            if money_machine.make_payment(drink_data.cost):
                coffee_maker.make_coffee(drink_data)
