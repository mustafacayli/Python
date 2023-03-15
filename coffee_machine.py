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
    """Siparişin olumlu ya da olumsuz olduğu bilgisini verir"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
    return True


def process_coins():
    """Toplam ücreti hesaplar ve çıktı olarak verir"""
    print("Please insert the coin")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickels?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total


def is_transaction_successfully(money_received, drink_cost):
    """Para yeterliyse olumlu yetersizse olumsuz olarak yanıt verir"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """Kullanılan ürünleri sahip olunan ürünlerden çıkarır ve bilgilendirir"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name}☕️ enjoy.")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml️ .")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffe: {resources['coffee']}g.")
        print(f"Money: ${profit}.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfully(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
