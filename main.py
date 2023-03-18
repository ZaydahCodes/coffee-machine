import sys


def actions():
    prompt = input(">")
    if prompt == "report":
        print(f"Water: {resources['water']}ml \n Milk: {resources['milk']}ml, "
              f"\n Coffee: {resources['coffee']}g \n Money: ${Money}")
    elif prompt == "off":
        sys.exit()
    else:
        print("invalid input : type 'report' to get available resources or 'off' to switch off coffee machine")


def check_resource(coffee_choice, can_make_order):
    if MENU[coffee_choice]["ingredients"]["water"] > resources["water"]:
        can_make_order = False
        return "Sorry, there is not enough water"
    elif MENU[coffee_choice]["ingredients"]["coffee"] > resources["coffee"]:
        can_make_order = False
        return "Sorry, there is not enough coffee"
    elif coffee_choice == "latte" or coffee_choice == "cappuccino":
        can_make_order = False
        if MENU[coffee_choice]["ingredients"]["milk"] > resources["milk"]:
            return "Sorry, there is not enough milk"
    else:
        can_make_order = True


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

Money = 0
can_make_order = True
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
check_resource(coffee_choice, can_make_order)


if can_make_order:
    coins_quarters = int(input("please input the number of quarters:"))
    coins_dime = int(input("please input the number of dime:"))
    coins_nickel = int(input("please input the number of nickels:"))
    coins_pennies = int(input("please input the number of pennies:"))
    amount_paid = (coins_quarters * 0.25) + (coins_dime * 0.1) + (coins_nickel * 0.05) + (coins_pennies * 0.01)
    if amount_paid < MENU[coffee_choice]["cost"]:
        print("Sorry, that's not enough money. Money refunded")
        actions()
    else:
        Money += amount_paid
        if amount_paid > MENU[coffee_choice]["cost"]:
            change = amount_paid - MENU[coffee_choice]["cost"]
            print(f"Here is ${change} in change ")
        resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]
        if coffee_choice == "latte" or "cappuccino":
            resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]
        print(f"Here is your {coffee_choice}. Enjoy!")

