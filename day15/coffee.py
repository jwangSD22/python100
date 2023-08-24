import os
from resource import menu
from resource import resources


def clear_console():
    os.system('cls')


# TODO 1 prompt user by asking ' what would u like' espresso latte cappuccino

def initialize_machine():
    # initialize machine with predetermined fill of water/milk/coffee
    this_machine_resources = resources.copy()
    current_choice = None
    this_machine_money = 0
    money_inserted = float(0)
    check_enough_resources = False

    while True:
        selection = input('What would you like to order? (espresso, latte, or cappuccino) ')

        if selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
            current_choice = selection
            check_enough_resources = check_resources(this_machine_resources, current_choice, menu)
            if not check_enough_resources:
                continue
            else:
                money_inserted = insert_coins()
                this_machine_money = make_drink(current_choice, money_inserted, this_machine_resources, this_machine_money)

        elif selection == 'refill':
            clear_console()
            this_machine_resources = resources.copy()

        # TODO 3 print report of what resources are left and current money
        elif selection == 'report':
            # run function to show report with parameters that include this_machine_resources
            # after that functino is complete can continue this function into the while loop to go
            # back and ask what you would like to order
            print_report(this_machine_resources, this_machine_money)

        # TODO 2 add secret 'off' prompt that allows u to exit program
        elif selection == 'off':
            break


def make_drink(drink, money_inserted, this_machine_resources, this_machine_money):
    clear_console()
    change = money_inserted - menu[drink]['cost']
    if change < 0:
        clear_console()
        print(money_inserted)
        print(change)
        return print('Sorry, not enough money inserted! Please try again')

    drink_ingredients = menu[drink]['ingredients']
    for item in drink_ingredients:
        this_machine_resources[item] -= drink_ingredients[item]

    print(f'You inserted ${money_inserted}')
    print(f'Here is your change ${round(change, 2)}')
    print(f'Here is your {drink}. Enjoy!')

    return this_machine_money + menu[drink]['cost']


def print_report(this_machine_resources, this_machine_money):
    clear_console()
    print(f'Water: {this_machine_resources["water"]}ml')
    print(f'Milk: {this_machine_resources["milk"]}ml')
    print(f'Coffee: {this_machine_resources["coffee"]}ml')
    print(f'Money: ${this_machine_money}')


# TODO 4 check resources sufficient?
def check_resources(current_resources, drink, menu):
    current_requirements = menu[drink]['ingredients']
    resource_check = True

    for item in current_requirements:
        if current_resources[item] < current_requirements[item]:
            print(f'Not enough {item}! Please refill!')
            resource_check = False

    return resource_check


# TODO 5 process coins
def insert_coins():
    quarters = int(input('How many quarters inserted?'))
    dimes = int(input('How many dimes inserted?'))
    nickles = int(input('How many nickles inserted?'))
    pennies = int(input('How many pennies inserted?'))

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


initialize_machine()
