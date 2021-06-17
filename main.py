'''
Coffee Machine program. Choose coffee type, put coins in, get coffee.
'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources_units ={
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}
program_on = True

def get_coins(type):
    print(f"Insert coins (Cost of {type}: ${MENU[type]['cost']})")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

def make_coffee(type):
    for ingredient_name, ingredient_amount in MENU[type]["ingredients"].items():
        resources[ingredient] -= ingredient_amount

while program_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if choice == 'report':
        for key, value in resources.items():
            print(key.capitalize() + ": " + str(value) + resources_units[key])
        print(f"Money: ${profit}")

    elif choice == 'off':
        program_on = False

    elif choice == 'espresso':

        for ingredient, ingredient_required in MENU["espresso"]["ingredients"].items():
            # Checking if not enough resource
            if  ingredient_required > resources[ingredient]:
                print(f"Sorry, not enough {ingredient}")

            # If enough resources
            else:
                total_coins = get_coins(choice)

                if total_coins < MENU["espresso"]["cost"]:
                    print(f"Sorry, not enough coins.Cost:{MENU['espresso']['cost']}). Amount given: {total_coins}")
                    break
                else:
                    change = total_coins - MENU["espresso"]["cost"]
                    profit += MENU["espresso"]["cost"]

                    print(f"You gave ${total_coins}. Your change: ${change}")

                    make_coffee(choice)

                    print("Here's your {choice}, enjoy")

    elif choice == 'latte':
        for ingredient, ingredient_required in MENU["latte"]["ingredients"].items():
            # Checking if not enough resource
            if  ingredient_required > resources[ingredient]:
                print(f"Sorry, not enough {ingredient}")

            # If enough resources
            else:
                total_coins = get_coins(choice)

                if total_coins < MENU["latte"]["cost"]:
                    print(f"Sorry, not enough coins.Cost:{MENU['latte']['cost']}). Amount given: {total_coins}")
                    break
                else:
                    change = total_coins - MENU["latte"]["cost"]
                    profit += MENU["espresso"]["cost"]

                    print(f"You gave ${total_coins}. Your change: ${change}")

                    make_coffee(choice)

                    print("Here's your {choice}, enjoy")

    elif choice == 'cappuccino':
        for ingredient, ingredient_required in MENU["cappuccino"]["ingredients"].items():
            # Checking if not enough resource
            if  ingredient_required > resources[ingredient]:
                print(f"Sorry, not enough {ingredient}")

            # If enough resources
            else:
                total_coins = get_coins(choice)

                if total_coins < MENU["cappuccino"]["cost"]:
                    print(f"Sorry, not enough coins.Cost:{MENU['cappuccino']['cost']}). Amount given: {total_coins}")
                    break
                else:
                    change = total_coins - MENU["cappuccino"]["cost"]
                    profit += MENU["espresso"]["cost"]

                    print(f"You gave ${total_coins}. Your change: ${change}")

                    make_coffee(choice)

                    print("Here's your {choice}, enjoy")

    # TODO 1: print report
    # TODO 2: check resources sufficient?
    # TODO 3: process coins
    # TODO 4: check transaction successfull
    # TODO 5: make coffee 