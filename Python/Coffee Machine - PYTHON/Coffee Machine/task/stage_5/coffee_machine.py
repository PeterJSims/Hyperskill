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
        """Show every ingredient in the machine's current state"""
        print()
        print("The coffee machine has: ")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()

    def determine_enough_ingredients(self, drink_type: str) -> bool:
        """Iterating through the drink type's necessary ingredients against the machine's current ingredient state.
        Return False if any of the ingredients are below the threshold for the given drink type."""
        return all([self.water >= self.DRINK_TYPES[drink_type]['water'],
                    self.milk >= self.DRINK_TYPES[drink_type]['milk'],
                    self.beans >= self.DRINK_TYPES[drink_type]['beans'],
                    self.cups >= self.DRINK_TYPES[drink_type]['cups']])

    def get_missing_ingredients(self, drink_type: str) -> list:
        """Return a list of the necessary drink ingredients that are larger than the machine's ingredient state."""
        missing_ingredients = []
        if self.water < self.DRINK_TYPES[drink_type]['water']:
            missing_ingredients.append('water')
        elif self.water < self.DRINK_TYPES[drink_type]['milk']:
            missing_ingredients.append('milk')
        elif self.beans < self.DRINK_TYPES[drink_type]['beans']:
            missing_ingredients.append('beans')
        elif self.cups < self.DRINK_TYPES[drink_type]['cups']:
            missing_ingredients.append('cups')
        return missing_ingredients

    def buy(self, drink_type: str) -> None:
        """Remove the ingredients and add the money to the current state for the corresponding drink"""
        self.water -= self.DRINK_TYPES[drink_type]['water']
        self.milk -= self.DRINK_TYPES[drink_type]['milk']
        self.beans -= self.DRINK_TYPES[drink_type]['beans']
        self.money += self.DRINK_TYPES[drink_type]['cost']
        self.cups -= 1

    def fill(self, water: int, milk: int, beans: int, cups: int) -> None:
        """Add ingredients for any ingredients above 0"""
        if water > 0:
            self.water += water
        if milk > 0:
            self.milk += milk
        if beans > 0:
            self.beans += beans
        if cups > 0:
            self.cups += cups

    def take(self) -> int:
        """Return the amount of money in the machine and set its state to 0"""
        temp_money = self.money
        self.money = 0
        return temp_money


class UserInterface:
    DRINK_CHOICES = {1: "espresso", 2: "latte", 3: "cappuccino"}

    def __init__(self):
        """Start with a default CoffeeMachine. Call reset_machine to return to original state."""
        self.machine = CoffeeMachine()

    def main(self) -> None:
        self._get_action()

    def _get_action(self):
        """Determine the user's action, execute the necessary methods, and recursively call _get_action again until 'exit' is chosen."""
        print("Write action (buy, fill, take, remaining, exit): ")
        choice = input().lower()
        if choice not in ["buy", "fill", "take", "remaining", 'exit']:
            self._get_action()
        else:
            if choice == 'buy':
                self._buy_drink()
                print()
                self._get_action()
            elif choice == 'fill':
                water, milk, beans, cups = self._fill_amounts()
                self.machine.fill(water, milk, beans, cups)
                print()
                self._get_action()
            elif choice == 'take':
                self._take_money()
                print()
                self._get_action()
            elif choice == 'remaining':
                self.machine.display_state()
                print()
                self._get_action()
            elif choice == 'exit':
                return None

    def _buy_drink(self):
        """Get the user's choice or return to the main menu. Depending on the choice, availability will be calculated and displayed."""

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()

        if choice == 'back':
            return None

        drink_choice = self._validate_input(choice)
        if drink_choice in self.DRINK_CHOICES:
            drink_name = self.DRINK_CHOICES[drink_choice]
            if self.machine.determine_enough_ingredients(drink_name):
                print("I have enough resources, making you a coffee!")
                self.machine.buy(drink_name)
            else:
                missing_ingredients = self.machine.get_missing_ingredients(drink_name)
                print(f"Sorry, not enough {', nor'.join(missing_ingredients)}!")
        else:
            print("Please enter a correct choice")
            self._buy_drink()

    def _take_money(self):
        """Display the money taken from the machine's take() method"""
        money = self.machine.take()
        print(f"I gave you ${money}")

    def _fill_amounts(self) -> tuple:
        """Determine the amount of each ingredient to add, verify the format, and add it to the current machine's state"""
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

    def _check_missing_ingredients(self, drink_choice: int) -> bool:
        """Determine if the given drink has a requirement above the currently available inventory"""
        return self.machine.determine_enough_ingredients(drink_choice)

    def reset_machine(self) -> CoffeeMachine:
        """Start a new machine with the default ingredient counts"""
        self.machine = CoffeeMachine()

    @staticmethod
    def _validate_input(user_input: str) -> int:
        """For integer based choices, validate that the given input can be cast to integer and return said integer"""
        try:
            num_input = int(user_input)
            return num_input
        except ValueError:
            print("Please only provide integers")
            return None


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
