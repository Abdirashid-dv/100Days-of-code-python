from art import logo

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """This function will back True if the resource is sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
             print(f"Sorry there is not enough {item}.")
             return is_enough == False
    return is_enough

def is_transaction_successfull(money_recevied,drink_cost):
    """Return True when payment is accepted and return False if money is insufficient"""
    if money_recevied > drink_cost:
        change = round(money_recevied - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
         print("Sorry that's not enough money. Money refunded.")
         return False

def process_coin():
    """Returns the total calculated from coin inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?:"))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredient from a resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
print(logo)
while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]) :
            payment = process_coin()
            drink_cost = drink['cost']
            if is_transaction_successfull(payment,drink_cost):
                make_coffee(choice,drink["ingredients"])
            
