class CoffeeMachine:
    DRINK_TYPES = {"espresso": {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'cost': 4},
                   "latte": {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'cost': 7},
                   "cappuccino": {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'cost': 6}
                   }

    def __init__(self):
        """Initialize a coffee machine with the standard starting ingredient counts"""
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def display_state(self):
        print("The coffee machine has: ")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def calculate_cup_availability(self, drink_type: str) -> bool:
        """Iterating through the drink type's necessary ingredients with the machine's current ingredient state.
        Return False if any of the ingredients are below the threshold for the given drink type."""
        return all([self.water >= self.DRINK_TYPES[drink_type]['water'],
                    self.milk >= self.DRINK_TYPES[drink_type]['milk'],
                    self.beans >= self.DRINK_TYPES[drink_type]['beans']],
                   self.cups >= self.DRINK_TYPES[drink_type]['cups'])

    def buy(self, drink_type: str) -> None:
        self.water -= self.DRINK_TYPES[drink_type]['water']
        self.milk -= self.DRINK_TYPES[drink_type]['milk']
        self.beans -= self.DRINK_TYPES[drink_type]['beans']
        self.money += self.DRINK_TYPES[drink_type]['cost']
        self.cups -= 1

    def fill(self, water: int, milk: int, beans: int, cups: int) -> None:
        if water > 0:
            self.water += water
        if milk > 0:
            self.milk += milk
        if beans > 0:
            self.beans += beans
        if cups > 0:
            self.cups += cups

    def take(self):
        temp_money = self.money
        self.money = 0
        return temp_money


class UserInterface:
    DRINK_CHOICES = {1: "espresso", 2: "latte", 3: "cappuccino"}

    def __init__(self):
        self.machine = CoffeeMachine()

    def main(self) -> None:
        self.machine.display_state()
        print()
        self._get_action()
        print()
        self.machine.display_state()

    def _get_action(self):
        print("Write action (buy, fill, take): ")
        choice = input().lower()
        if choice not in ["buy", "fill", "take", 'exit']:
            self._get_action()
        else:
            if choice == 'buy':
                self._buy_drink()
            elif choice == 'fill':
                water, milk, beans, cups = self._fill_amounts()
                self.machine.fill(water, milk, beans, cups)
            elif choice == 'take':
                self._take_money()

    def _buy_drink(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        choice = self._validate_input(input())
        if choice in self.DRINK_CHOICES:
            self.machine.buy(self.DRINK_CHOICES[choice])
        else:
            print("Please enter a correct choice")
            self._buy_drink()

    def _take_money(self):
        money = self.machine.take()
        print(f"I gave you ${money}")

    def _fill_amounts(self) -> tuple:
        print("Write how many ml of water you want to add:")
        water = self._validate_input(input())
        print("Write how many ml of milk you want to add:")
        milk = self._validate_input(input())
        print("Write how many grams of coffee beans you want to add:")
        beans = self._validate_input(input())
        print("Write how many disposable coffee cups you want to add:")
        cups = self._validate_input(input())
        if None in [water, milk, beans, cups]:
            self._get_amounts()
        else:
            return water, milk, beans, cups

    def _check_availability(self, drink_choice: int) -> bool:
        return self.machine.calculate_cup_availability(drink_choice)

    def _reset_machine(self) -> CoffeeMachine:
        """Start a new machine with the default ingredient counts"""
        self.machine = CoffeeMachine()

    @staticmethod
    def _validate_input(user_input: str) -> int:
        try:
            num_input = int(user_input)
            return num_input
        except ValueError:
            print("Please only provide integers")
            return None


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
