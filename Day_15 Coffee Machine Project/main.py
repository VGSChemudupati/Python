MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO:1 print report of all coffee resources
#TODO:2 Ask and get what coffee they need (espresso/latte/cappuccino). "Off" is the secret word to turn off the machine.
#TODO:3 When user asks for a drink, resources should be checked.
#TODO:4 If resources are good, then ask for coins. Say money is short if its short. Or give back extra.
#TODO:5 Make the coffee (calculate resources deduction and present the report after).

def check_resources(type):
    for item in MENU[type]["ingredients"]:
        if MENU[type]["ingredients"][item] > resources[item]:
            return False
    return True

def resources_print(text):
    for key in resources.keys():
        print(f"{key}: {resources[key]}")

def check_change(type):
    print("Please insert coins ")
    quarters = float(input("\nHow many Quarters: ")) *0.25
    if quarters < MENU[type]["cost"]:
        dimes = float(input("\nHow many Dimes: ")) *0.10
        if quarters+dimes < MENU[type]["cost"]:
            nickles = float(input("\nHow many Nickles: ")) *0.05
            if quarters+dimes+nickles < MENU[type]["cost"]:
                pennies = float(input("\nHow many Pennies: ")) *0.01
            else:
                pennies = 0
        else:
            nickles = 0
            pennies = 0
    else:
        dimes = 0
        nickles = 0
        pennies = 0
    total = quarters + dimes + nickles + pennies
    Gtotal = total - MENU[type]["cost"]
    loopup = True
    while loopup == True:

        if Gtotal == 0:
            return True
        elif Gtotal > 0:
            print(f"\nHere is the change :${round(Gtotal, 2)}.")
            return True
        else:
            print(f"\nInsufficient funds.")
            x = float(input(f"Enter the difference amount of ${abs(Gtotal)}. "))
            if x >= abs(Gtotal):
                total += x
                Gtotal += x
            else:
                return_total = total + x
                print(f"You haven't provided right amount of money. So cancelling this transaction and take your total money back ${return_total}.")
                return False

def give_coffee(type):
    print(f"Here is your {type} ☕️. Enjoy!")
    for item in MENU[type]["ingredients"]:
        resources[item] = resources[item] - MENU[type]["ingredients"][item]
    return

choice = input(f"What would you like? \nespresso  ${MENU["espresso"]["cost"]}\nlatte  ${MENU["latte"]["cost"]} \ncappuccino  ${MENU["cappuccino"]["cost"]}\n")
if choice in ["espresso", "latte", "cappuccino"]:
    if(check_resources(choice)) is True:
        if (check_change(choice)) is True:
            give_coffee(choice)

    elif (check_resources(choice)) is False:
        print("Not enough resources. Choose another one")
    else:
        print("Invalid choice. Enter again")


resources_print(input("Do you like to print the resources left? "))


