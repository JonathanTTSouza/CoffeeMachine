'''
Coffee Machine program. Choose coffee type, put coins in, get coffee.
'''

profit = 0

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
        resources[ingredient_name] -= ingredient_amount


def enough_ingredients(type):
    for ingredient, ingredient_required in MENU["espresso"]["ingredients"].items():
            # Checking if not enough resource
        if  ingredient_required > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return False
    return True

def enough_coins(type, coins):
    if coins < MENU[type]["cost"]:
        print(f"Sorry, not enough coins.Cost:{MENU[type]['cost']}). Amount given: {coins}")
        return False
    else:
        change = coins - MENU[type]["cost"]
        change = round(change, 2)
        global profit
        profit += MENU[type]["cost"]

        print(f"You gave ${coins}. Your change: ${change}")
        return True
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


while program_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if choice == 'report':
        for key, value in resources.items():
            print(key.capitalize() + ": " + str(value) + resources_units[key])
        print(f"Money: ${profit}")

    elif choice == 'off':
        program_on = False

    elif choice == 'espresso':
        if enough_ingredients(choice):
            total_coins = get_coins(choice)

            if enough_coins(choice, total_coins):
                make_coffee(choice)

                print(f"Here's your {choice}, enjoy")

    elif choice == 'latte':
        if enough_ingredients(choice):
            total_coins = get_coins(choice)

            if enough_coins(choice, total_coins):
                make_coffee(choice)

                print(f"Here's your {choice}, enjoy")

    elif choice == 'cappuccino':
        if enough_ingredients(choice):
            total_coins = get_coins(choice)

            if enough_coins(choice, total_coins):
                make_coffee(choice)

                print(f"Here's your {choice}, enjoy")

    # TODO 1: print report
    # TODO 2: check resources sufficient?
    # TODO 3: process coins
    # TODO 4: check transaction successfull
    # TODO 5: make coffee 