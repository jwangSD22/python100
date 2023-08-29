from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


class CoffeShop:
    def __init__(self):
        self.money_machine = MoneyMachine()
        self.coffee_maker = CoffeeMaker()
        self.menu = Menu()

    def open_shop(self):
        while True:
            selection = input(
                f"What would you like to order? \
                {self.menu.get_items()}"
            )

            if selection == "refill":
                clear_console()
                self.coffee_maker.refill()

            elif selection == "report":
                clear_console()
                self.coffee_maker.report()
                self.money_machine.report()

            elif selection == "off":
                break

            else:
                clear_console()
                get_drink_order = self.menu.find_drink(selection)
                if get_drink_order:
                    cost = get_drink_order.cost
                    resource_sufficient = self.coffee_maker.is_resource_sufficient(
                        get_drink_order
                    )
                    if resource_sufficient and self.money_machine.make_payment(cost):
                        self.coffee_maker.make_coffee(get_drink_order)


coffe_shop = CoffeShop()
coffe_shop.open_shop()
