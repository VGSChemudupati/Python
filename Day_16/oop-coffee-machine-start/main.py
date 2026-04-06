from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeestar_menu = Menu()
coffeestar_maker = CoffeeMaker()
coffeestar_money = MoneyMachine()


is_on = True

while is_on:
    options = coffeestar_menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report": 
        coffeestar_maker.report()
        coffeestar_money.report()
    else:
        drink = coffeestar_menu.find_drink(choice)
        if coffeestar_maker.is_resource_sufficient(drink) and coffeestar_money.make_payment(drink.cost):
            coffeestar_maker.make_coffee(drink)


