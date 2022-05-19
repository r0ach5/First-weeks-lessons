MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

coin_values = {
    "quarters": .25,
    "dimes": .10,
    "nickles": .05,
    "pennies": .01,
}


def check_resources(coffee_choice):
    check_resources_dict = MENU[coffee_choice]["ingredients"]
    if check_resources_dict["water"] <= resources["water"]:
        if check_resources_dict["coffee"] <= resources["coffee"]:
            if check_resources_dict["milk"] <= resources["milk"]:
                return True
    return False


def coffee_machine():
    caffeine_addiction = True
    profitz = 0
    change_return = 0
    total_spent = 0
    while caffeine_addiction:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        money_holder = 0
        if coffee_choice == "off":
            caffeine_addiction = False
            return
        elif coffee_choice == "report":
            print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profitz}')

        elif check_resources(coffee_choice) is True:
            for i in resources:
                resources[i] -= MENU[coffee_choice]["ingredients"][i]
            print("Please insert coins.")
            for i in coin_values:
                spent_coins = int(input(f"how many {i}?"))
                total_spent += coin_values[i] * spent_coins
            total_spent = round(total_spent, 2)
            if total_spent >= MENU[coffee_choice]["cost"]:
                change_return = round(total_spent - MENU[coffee_choice]["cost"], 2)
                profitz = total_spent - change_return
                money_holder += profitz
                print(f"Here is {change_return} in change.")
                print(f"Here is your {coffee_choice} ☕, Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")


coffee_machine()
"\n"
