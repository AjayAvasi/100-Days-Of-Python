import data

is_on = True
money = 0


def prompt_user():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(
            f"Water: {data.resources['water']}ml\nMilk: {data.resources['milk']}ml\nCoffee: {data.resources['coffee']}g\nMoney: ${money}")
    elif user_input == "off":
        global is_on
        is_on = False
    else:
        make_coffee(user_input)


def make_coffee(coffee_type):
    if check_resources(coffee_type) and payment_prompt(data.MENU[coffee_type]["cost"]):
        print(f"Thank you! Here is your {coffee_type} ☕")
        required_resources = data.MENU[coffee_type]["ingredients"]

        for resource in required_resources:
            data.resources[resource] -= data.MENU[coffee_type]["ingredients"][resource]


def payment_prompt(cost):
    print("Please Insert Coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    if total < cost:
        print("You did not provide enough money. Transaction cancelled. Money Refunded.")
        return False

    if cost < total:
        print(f"Here is ${total - cost} in change.")
    global money
    money += cost
    return True


def check_resources(coffee_type):
    required_resources = data.MENU[coffee_type]["ingredients"]

    for resource in required_resources:
        if required_resources[resource] > data.resources[resource]:
            print(f"Sorry! We don't have enough {resource}")
            return False
    return True


while is_on:
    prompt_user()
