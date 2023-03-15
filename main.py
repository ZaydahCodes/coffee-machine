import sys


def actions():
    prompt = input(">")
    if prompt == "report":
        print(f"Water: {resources['water']}ml \n {resources['milk']}ml, \n {resources['coffee']}g \n ${Money}")
    elif prompt == "off":
        sys.exit()
    else:
        print("invalid input : type 'report' to get available resources or 'off' to switch off coffee machine")


def check_resource(coffee_choice):
    if MENU[coffee_choice]["ingredients"]["water"] > resources["water"]:
        return "Sorry, there is not enough water"
    if MENU[coffee_choice]["ingredients"]["coffee"] > resources["coffee"]:
        return "Sorry, there is not enough coffee"
    if coffee_choice == "latte" or coffee_choice == "cappuccino":
        if MENU[coffee_choice]["ingredients"]["milk"] > resources["milk"]:
            return "Sorry, there is not enough milk"
    actions()


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

coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
check_resource(coffee_choice)